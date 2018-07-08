#! /usr/bin/env

"""These are helper functions for the Basic Programs with Python3 workshop. The
goal is to use only the standard library, to avoid complications of package
installations.

More information at http://github.com/ningyuansg/basic-python3

All helper functions are defined in this one file for ease of import. To help
you navigate this file, the functions are divided into categories, each with
their own headers in a multiline comment. The headers (exact), and their
descriptions are:

    {HEADER NAME} - {DESCRIPTION}

    GENERAL       - General helper functions
    TELEGRAM API  - Functions which interact with the telegram API
    WEATHER API   - Functions which interact with the NEA air-temperature API

"""

import json, random, time, urllib.parse, urllib.request

'''
GENERAL
'''

def mean(seq):
    r"""Calculate the mean of a sequence of int/floats

    Parameters
    ----------
    seq : list or iterable of int or floats

    Returns
    -------
    float
        The arithmetic mean of the sequence

    Raises
    ------
    TypeError
        If the parameter given is not an iterable, e.g. not a list
    AssertionError
        If the sequence elements are not int or floats (i.e. not numbers)

    """

    assert all([
        isinstance(x, int) or isinstance(x, float) for x in seq
    ]), 'The elements of the list must be a number'
    return sum(seq) / len(seq)

'''
TELEGRAM API
'''

telegram_url = 'https://api.telegram.org/bot{key}/{method}'

def telegram_whoami(key):
    r"""GET telegram method getMe to retrieve the first_name and username.

    Parameters
    ----------
    key : string
        Token for the telegram bot from @botfather.

    Returns
    -------
    list
        A list of two elements, where the first element is the 'first_name' of
        the user, and the second is the username. Both are strings.

    Raises
    ------
    AssertionError
        If the parameters are of the wrong type.
    Exception
        A relevant `urllib` exception may be raised.

    """

    assert type(key) == str, 'The argument must be of type str'
    url = telegram_url.format(key=key, method='getMe')
    resp = urllib.request.urlopen(url)
    body = resp.readline().decode()
    result = json.loads(body)['result']
    return [result['first_name'], result['username']]

def telegram_send(key, chat_id, text):
    r"""POST telegram method sendMessage to send a message.

    parse_mode is set to telegram's Markdown: *bold*, _italics_, `inline code`

    Parameters
    ----------
    key : string
        Token for the telegram bot from @botfather.
    chat_id : int
        Telegram chat id to send this message to.
    text : string
        Content of the message to be sent, can be markdown.

    Returns
    -------
    bool
        True, if successful.

    Raises
    ------
    AssertionError
        If the parameters are of the wrong type.
    Exception
        A relevant `urllib` exception may be raised.

    """

    assert type(key) == str, 'The argument must be of type str'
    assert type(chat_id) == int, 'The argument must be of type int (number)'
    assert type(text) == str, 'The argument must be of type str'
    url = telegram_url.format(key=key, method='sendMessage')
    url = '{base}?chat_id={chat_id}&text={text}&parse_mode=Markdown'.format(
        base=url, chat_id=chat_id, text=urllib.parse.quote(text)
    )
    return urllib.request.urlopen(url).status == 200

def telegram_get_updates(key, interval=5):
    """Get a stream of user ids of new telegram updates.

    Only considers updates with a message key in it's JSON response.

    Parameters
    ----------
    key : string
        Token for the telegram bot from @botfather.
    interval : int or float, optional
        Interval, in seconds, between calls to the telegram getUpdates API.
        Defaults to `5`.

    Yields
    -------
    list
        A list of unique user ids of new updates since the last yielded value.
        Can be an empty list, if there are no new updates.

    Raises
    ------
    AssertionError
        If the parameters are of the wrong type.
    Exception
        A relevant `urllib` exception may be raised.

    Examples
    --------

    >>> for updates in telegram_get_updates('T3L3GR4M_K3Y'):
    ...    for user_id in updates:
    ...        telegram_send_message('T3L3K3Y', user_id, 'Hi!')

    """

    assert type(key) == str, 'The argument must be of type str'
    offset = 0
    try:
        while True:
            time.sleep(interval)
            next_offset, user_ids = get_updates(key, offset)
            offset = max((next_offset + 1, offset))
            yield user_ids
    except KeyboardInterrupt:
        raise StopIteration

def get_updates(key, offset):
    url = telegram_url.format(key=key, method='getUpdates')
    scheme, netloc, path, _, _, _ = urllib.parse.urlparse(url)
    query = make_query({
        'offset': str(offset)
    })
    url = urllib.parse.urlunparse((scheme, netloc, path, '', query, ''))
    resp = urllib.request.urlopen(url)
    return parse_resp(resp)

def make_query(kv):
    pairs = []
    for k, v in kv.items():
        k = urllib.parse.quote(k)
        v = urllib.parse.quote(v)
        pairs.append('{}={}'.format(k, v))
    return '&'.join(pairs)

def parse_resp(resp):
    ''' Parses a urllib response

    TODO: return a list of userids '''
    body = resp.readlines()
    body = ''.join([ l.decode() for l in body ])
    body = json.loads(body)
    assert body['ok']
    updates = body['result']
    return parse_updates(updates)

def parse_updates(updates):
    ''' Parses a dictionary representing a telegram update

    Returns a two-element list.

    The first element is an integer of the largest update_id, or 0 if
    the updates list (after filtering only messages) is empty.

    The second is a unique list of user ids, or an empty list if the updates
    list (after filtering only messages) is empty '''
    updates = filter_only_messages(updates)

    update_ids = list(map(lambda update: update['update_id'], updates))
    max_update_id = max(update_ids) if update_ids != [] else 0

    user_ids = map(lambda update: update['message']['from']['id'], updates)
    unique_user_ids = list(set(user_ids))

    return [max_update_id, unique_user_ids]

def filter_only_messages(updates):
    ''' Can't get the allowed_updates option of telegram getUpdates to work,
    so implementing a filter for just messages here.'''
    return list(filter(lambda update: 'message' in update.keys(), updates))

"""
WEATHER API
"""

weather_url = 'https://api.data.gov.sg/v1/environment/air-temperature?{param}={time}'

def weather_get_now():
    r"""GET the latest weather data using the NEA weather API.

    Returns
    -------
    list
        A list of readings (`int` or `float`) of the air temperature from
        various weather stations across Singapore.

    Raises
    ------
    Exception
        A relevant `urllib` exception may be raised.

    """

    url = weather_url.format(param='datetime', time=_strftime_now())
    resp = urllib.request.urlopen(url)
    body = resp.readline().decode()
    result = json.loads(body)
    readings = result['items'][0]['readings']
    temperatures = map(lambda x: x['value'], readings)
    return list(temperatures)

def weather_get_rand():
    r"""Simulates a call to the function `weather_get_now`.

    In case the NEA weather API fails, this function provides a list of randomly
    generated air temperature readings.

    Returns
    -------
    list
        A list of readings (`float`) of randomly generated air temperatures.

    See Also
    --------
    weather_get_now

    """

    return [ random.randint(250, 300) / 10 for _ in range(random.randint(1, 10)) ]

def _strftime_now():
    r"""Returns current time in the format specified by the NEA weather api

    Returns
    -------
    string
        Current date and time in the format YYYY-MM-DD[T]HH:mm:ss

    """

    return _strftime(time.localtime())

def _strftime(time_tuple):
    r"""Returns given time tuple in the format specified by the NEA weather api

    Parameters
    ----------
    time_tuple : tuple
        A six element 'time tuple'

    See Also
    --------
    time.strftime

    Returns
    ------
    string
        Current date and time in the format YYYY-MM-DD[T]HH:mm:ss

    """

    return time.strftime('%Y-%m-%dT%H:%M:%S', time_tuple)

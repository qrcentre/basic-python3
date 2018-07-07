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

    TELEGRAM API  - Functions which interact with the telegram API
    WEATHER API   - Functions which interact with the NEA air-temperature API

"""

import json, random, time, urllib.parse, urllib.request

'''
TELEGRAM API
'''

telegram_url = 'https://api.telegram.org/bot{key}/{method}'
weather_url = 'https://api.data.gov.sg/v1/environment/air-temperature?{param}={time}'

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

"""
WEATHER API
"""

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

    url = weather_url.format(param='datetime', time=strftime_now())
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

def strftime_now():
    r"""Returns current time in the format specified by the NEA weather api

    Returns
    -------
    string
        Current date and time in the format YYYY-MM-DD[T]HH:mm:ss

    """

    return strftime(time.localtime())

def strftime(time_tuple):
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

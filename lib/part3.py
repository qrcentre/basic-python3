from basic_python3 import *

# In order to access our telegram bot, we need it's token (a.k.a. key). In order
# for our telegram bot to send messages to us, it needs to know our user id.

telegram_key= 'T3L3GR4M_K3Y'
telegram_chat_id = 1234567

# Let's get the bot to tell us our script has just started up.

telegram_send(telegram_key, telegram_chat_id, 'Everything is going extremely well')

# Then, we iterate through the updates to our telegram bot.

for updates in telegram_get_updates(telegram_key):
    # Noting that updates is a list of user_ids that can be empty, we need to
    # iterate through updates, sending a message to each user_id.
    for user_id in updates:
        temp_list = weather_get_now()
        temp_avg = mean(temp_list)
        telegram_send(
            telegram_key,
            telegram_chat_id,
            'It is ' + str(temp_avg) + ' C tonight'
        )

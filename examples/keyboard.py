import apigram

#token already invalid, bro :^)
token = '1361020830:AAEqj3jxeJkIjgG9CSJbs7LkBeqdbhs3u6g'

bot = apigram.session(token)
api = apigram.get_api(bot)

#bot is follow for all updates at server
for event in bot.listen():
    #is it message?
    if 'message' in event:
        #is message have a text?
        if 'text' in event['message']:
            #is it a command?
            if event['message']['text'] == '/test' or event['message']['text'] == f'/test@{bot.username}':
                name = event['message']['from']['first_name']
                text = f'<i>Keyboard test</i>, {name}'

                # Creating a keyboard
                kb = apigram.keyboard.inline_keyboard()
                kb.add_button(apigram.keyboard.inline_keyboard_button('test')())
                kb.add_button(apigram.keyboard.inline_keyboard_button('test 2')())
                kb.add_line()
                kb.add_button(apigram.keyboard.inline_keyboard_button('test 3')())
                
                # Sending a message
                api.sendMessage(
                    chat_id = event['message']['chat']['id'], 
                    parse_mode = 'HTML', # for HTML tags <i>Keyboard test</i>
                    text = text, 
                    reply_markup = kb())

import apigram

token = '1361020830:AAEqj3jxeJkIjgG9CSJbs7LkBeqdbhs3u6g'

bot = apigram.session(token)
api = apigram.get_api(bot)


for event in bot.listen():
    if 'message' in event:
        if 'text' in event['message']:
            if event['message']['text'] == '/test' or event['message']['text'] == f'/test@{bot.username}':
                name = event['message']['from']['first_name']
                text = f'<i>Keyboard test</i>, {name}'

                # Создание клавиатуры
                kb = apigram.keyboard.inline_keyboard()
                kb.add_button(apigram.keyboard.inline_keyboard_button('test')())
                kb.add_button(apigram.keyboard.inline_keyboard_button('test 2')())
                kb.add_line()
                kb.add_button(apigram.keyboard.inline_keyboard_button('test 3')())

                api.sendMessage(chat_id = event['message']['chat']['id'], parse_mode = 'HTML', text = text, reply_markup = kb())
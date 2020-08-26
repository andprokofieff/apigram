import apigram

bot = apigram.session('token')
api = apigram.get_api(bot)

# Получаем данные о боте через метод getme > https://core.telegram.org/bots/api#getme
print(api.getMe())

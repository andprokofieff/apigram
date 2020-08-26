import apigram

bot = apigram.session('123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11')
api = apigram.get_api(bot)

# How to get bot's info via simplest method getMe(): https://core.telegram.org/bots/api#getme
print(api.getMe())

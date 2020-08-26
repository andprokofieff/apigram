import apigram

bot = apigram.session('token')
api = apigram.get_api(bot)

# How to get bot's info via simplest method getMe(): https://core.telegram.org/bots/api#getme
print(api.getMe())

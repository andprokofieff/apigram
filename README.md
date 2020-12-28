
**Apigram** – Simple Python Telegram Bot API wrapper

* [Examples](./examples) (python3)
* [Sources](./apigram) (python3)
* [Telegram Bot API Manual](https://core.telegram.org/bots/api)

* [Contact with me](https://t.me/kensoi_fuji) [RU]

```python
import apigram

bot = apigram.session('123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11')
api = apigram.get_api(bot) #take an apigram.session(token) object

print(api.getMe()) #info
```

Install
------------
    $ pip install apigram


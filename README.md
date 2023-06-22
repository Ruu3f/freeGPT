[![PyPI version](https://badge.fury.io/py/freeGPT.svg)](https://badge.fury.io/py/freeGPT)
[![Downloads](https://static.pepy.tech/personalized-badge/freeGPT?period=month&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/freeGPT)
[![License](https://img.shields.io/badge/License-GPLv3-bright&green.svg)](LICENSE)
# freeGPT
freeGPT is a Python package that gives free access to GPT3 and GPT4 and more models.
<br>
Get started by installing the package:
```
py -m pip install --upgrade freeGPT
```
***Or add our [Discord bot](https://dsc.gg/freegpt), its [Open Sourced!](https://github.com/Ruu3f/freeGPT/tree/main/discord-bot)***
<br>
Join my [Discord Server](https://discord.gg/XH6pUGkwRr) for live chat and support or if you have any issues with this package.

## Source:
*GPT-3 has internet access.*
<br>
| Models            | Websites                                             |
| ----------------- | -----------------------------------------------------|
| gpt3              | [you.com](https://you.com/)                          |
| gpt4              | [ava-ai-ef611.web.app](https://ava-ai-ef611.web.app/)|
| alpaca_7b         | [chatllama.baseten.co](https://chatllama.baseten.co/)|

### TODO-List:
- [x] Make the library well-documented.
- [x] Make the over-all library easier to use.
- [x] Make the over-all library easier to understand.
- [x] Replace you.com with theb.ai for less failed responses.
- [x] Make GPT-3 & GPT-4 models with web access.
- [x] Add a non-GPT model.
- [x] Make a discord bot.
- [ ] Add a image generation model.

## Support this repository:
- Star this repository! :D
- Add the [Discord Bot](https://dsc.gg/freeGPT) :D
- Join my [Discord Server](https://discord.gg/XH6pUGkwRr):

[![DiscordWidget](https://discordapp.com/api/guilds/1120833966035976273/widget.png?style=banner2)](https://discord.gg/XH6pUGkwRr)

## Discord bot:
- Add the official freeGPT discord bot [here](https://dsc.gg/freegpt)
- This bot has ALL the models in this repository available.
- Its interactive, fast and overall easy to use.
- And lastly its [Open Sourced](https://github.com/Ruu3f/freeGPT/tree/main/discord-bot)!

## Examples:

#### GPT-3:
```python
from freeGPT import gpt3

while True:
    prompt = input("👦 > ")
    try:
        # Remove the 'proxy' variable and the 'proxies' parameter if you don't want to use a proxy.
        proxy = "Your proxies IP"
        resp = gpt3.Completion.create(prompt=prompt, chat=[], proxies={"https": "http://" + proxy})
        print(f"🤖 > {str(resp['text'])}")
    except Exception as e:
        print(f"🤖 > {str(e)}")
```
#### GPT-4:
```python
from freeGPT import gpt4

while True:
    prompt = input("👦 > ")
    try:
        resp = gpt4.Completion.create(prompt=prompt)
        print(f"🤖 > {str(resp)}")
    except Exception as e:
        print(f"🤖 > {str(e)}")
```

#### Alpaca-7b:
```python
from freeGPT import alpaca_7b

while True:
    prompt = input("👦 > ")
    try:
        resp = alpaca_7b.Completion.create(prompt=prompt)
        print(f"🤖 > {str(resp)}")
    except Exception as e:
        print(f"🤖 > {str(e)}")
```

## Star History:
[![Star History Chart](https://api.star-history.com/svg?repos=Ruu3f/freeGPT&type=Date)](https://github.com/Ruu3f/freeGPT/stargazers)


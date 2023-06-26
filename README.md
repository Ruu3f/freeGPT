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
| Models            | Websites                                             |
| ----------------- | ---------------------------------------------------- |
| c_a_l             | [you.com](https://you.com/)                          |
| gpt3              | [chat9.yqcloud.top](https://chat9.yqcloud.top/)      |
| gpt4              | [ava-ai-ef611.web.app](https://ava-ai-ef611.web.app/)|
| alpaca_7b         | [chatllama.baseten.co](https://chatllama.baseten.co/)|

### TODO-List:
- [x] Make the library well-documented.
- [x] Make the over-all library easier to use.
- [x] Make the over-all library easier to understand.
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

## Example:

```python
import freeGPT

while True:
    prompt = input("👦 > ")
    try:
        model = freeGPT.MODELNAME # Replace MODELNAME with the model you want to use.
        resp = model.Completion.create(prompt) # Also, there are `chat` and `proxies` parameters in c_a_l.
        print(f"🤖 > {resp}")
    except Exception as e:
        print(f"🤖 > {e}")
```

## Star History:
[![Star History Chart](https://api.star-history.com/svg?repos=Ruu3f/freeGPT&type=Date)](https://github.com/Ruu3f/freeGPT/stargazers)


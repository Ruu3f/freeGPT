[![PyPI](https://img.shields.io/pypi/v/freeGPT)](https://pypi.org/project/freeGPT)
[![Downloads](https://static.pepy.tech/badge/freeGPT)](https://pypi.org/project/freeGPT)
[![Status](https://img.shields.io/pypi/status/freeGPT)](https://pypi.org/project/freeGPT)

# freeGPT

freeGPT provides free access to GPT3, GPT4 and more models.

## Get started:

```
py -m pip install --upgrade freeGPT
```

**Or add the [freeGPT Discord bot](https://dsc.gg/freegpt), it's [open-sourced](https://github.com/Ruu3f/freeGPT/tree/main/discord-bot)!**

Join my [Discord server](https://discord.gg/XH6pUGkwRr) for live chat, support, or if you have any issues with this package.

## Source:

| Models   | Websites                                                |
| -------- | ------------------------------------------------------- |
| gpt3     | [<ava-ai-ef611.web.app>](https://ava-ai-ef611.web.app/) |
| gpt4     | [<you.com>](https://you.com/)       |
| alpaca_7b| [<chatllama.baseten.co>](https://chatllama.baseten.co/) |

## Support this repository:

- Star this repository :D
- Add the [freeGPT Discord bot](https://dsc.gg/freeGPT).
- Join my [Discord Server](https://discord.gg/XH6pUGkwRr):

[![DiscordWidget](https://discordapp.com/api/guilds/1120833966035976273/widget.png?style=banner2)](https://discord.gg/XH6pUGkwRr)

## TODO List:

- [x] Make the library well-documented.
- [x] Make the overall library easier to use.
- [x] Make the overall library easier to understand.
- [x] Add a non-GPT model.
- [x] Make a discord bot.
- [ ] Add an image generation model.

## Discord bot:

- Add the [freeGPT Discord bot](https://dsc.gg/freegpt).
- This bot has all the models in this repository available.
- It's interactive, overall fast, and easy to use.
- And lastly, it's [open-sourced](https://github.com/Ruu3f/freeGPT/tree/main/discord-bot).

## Example:

```python
import freeGPT

while True:
    prompt = input("👦: ")
    try:
        model = getattr(freeGPT, "Model Name here.")
        resp = model.Completion.create(prompt)
        print(f"🤖: {resp}")
    except Exception as e:
        print(f"🤖: {e}")
```

## Star History Chart:

[![Star History Chart](https://api.star-history.com/svg?repos=Ruu3f/freeGPT&type=Date)](https://github.com/Ruu3f/freeGPT/stargazers)

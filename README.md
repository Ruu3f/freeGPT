[![PyPI](https://img.shields.io/pypi/v/freeGPT)](https://pypi.org/project/freeGPT)
[![Downloads](https://static.pepy.tech/badge/freeGPT)](https://pypi.org/project/freeGPT)
[![Status](https://img.shields.io/pypi/status/freeGPT)](https://pypi.org/project/freeGPT)

# freeGPT

freeGPT provides free access to text and image generation models.

## Getting Started:

```
python -m pip install -U freeGPT
```

Join my [Discord server](https://dsc.gg/devhub-rsgh) for live chat, support, or if you have any issues with this package.

## Sources:

### Text Generation:
| Model      | Website                                               |
| ---------- | ----------------------------------------------------- |
| gpt3       | [chat9.yqcloud.top](https://chat9.yqcloud.top/)       |
| gpt4       | [you.com](https://you.com/)                           |
| alpaca_7b  | [chatllama.baseten.co](https://chatllama.baseten.co/) |
| falcon_40b | [gpt-gm.h2o.ai](https://gpt-gm.h2o.ai/)               |

### Image Generation:
| Model        | Website                                     |
| ------------ | ------------------------------------------- |
| prodia       | [prodia.com](https://prodia.com/)           |
| pollinations | [pollinations.ai](https://pollinations.ai/) |


## Support this repository:
- ⭐ **Star the project:** Star this and the [freeGPT-discord repository](https://github.com/Ruu3f/freeGPT-discord). It means a lot to me! 💕
- 🎉 **Join my Discord Server:** Chat with me and others. [Join here](https://dsc.gg/devhub-rsgh):

[![DiscordWidget](https://discordapp.com/api/guilds/1137347499414278204/widget.png?style=banner2)](https://dsc.gg/devhub-rsgh)

## TODO List:

- [x] Make the library well-documented.
- [x] Make the overall library easier to use.
- [x] Make the overall library easier to understand.
- [x] Add a non-GPT model.
- [x] Make a discord bot.
- [x] Add an image generation model.
- [x] Add more models.

## Discord bot:
- This bot has all the models in this repository available.
- It's interactive, overall fast, and easy to use.
- And lastly, it's [open-sourced](https://github.com/Ruu3f/freeGPT-discord-bot).

## Examples:

**Text Completion:**
```python
import freeGPT
from asyncio import run


async def main():
    while True:
        prompt = input("👦: ")
        try:
            resp = await getattr(freeGPT, "MODEL NAME").Completion().create(prompt)
            print(f"🤖: {resp}")
        except Exception as e:
            print(f"🤖: {e}")


run(main())
```

**Image Generation:**
```python
import freeGPT
from PIL import Image
from io import BytesIO
from asyncio import run


async def main():
    while True:
        prompt = input("👦: ")
        try:
            resp = await getattr(freeGPT, "MODEL NAME").Generation().create(prompt)
            Image.open(BytesIO(resp)).show()
            print(f"🤖: Image shown.")
        except Exception as e:
            print(f"🤖: {e}")


run(main())
```

## Star History Chart:

[![Star History Chart](https://api.star-history.com/svg?repos=Ruu3f/freeGPT&type=Date)](https://github.com/Ruu3f/freeGPT/stargazers)

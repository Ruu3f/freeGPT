[![PyPI version](https://badge.fury.io/py/freeGPT.svg)](https://badge.fury.io/py/freeGPT)
[![Downloads](https://static.pepy.tech/personalized-badge/freeGPT?period=month&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/freeGPT)
[![License](https://img.shields.io/badge/License-GPLv3-bright&green.svg)](LICENSE)
# freeGPT
A Python package that gives access to GPT3 &amp; GPT4 models for free.
<br>
*Get started by doing: `pip install freeGPT`*

## Source:
*Models with .web have internet access on.*
<br>
| Models            | Websites                                 |
| ----------------- | -----------------------------------------|
| gpt3              | [theb.ai](https://theb.ai)               |
| gpt3web           | [you.com](https://you.com)               |
| gpt4              | [usesless.com](https://ai.usesless.com)  |
| gpt4web           | [forefront.ai](https://chat.forefront.ai)|

### TODO-List:
- [x] Add GPT-4.
- [x] Make the library well-documented.
- [x] Make the over-all library easier to use.
- [x] Make the over-all library easier to understand.
- [x] Replace you.com with theb.ai for less failed responses.
- [x] Add a internet search model for GPT-3 & GPT-4
- [ ] Add a text to image generation model
- [ ] Make a discord bot

## Support me:
- Join my [Discord Server](https://discord.gg/NcQ26PrNDp) :D
- Star this repository :D

## Examples:

#### GPT-3:

```python
from freeGPT import gpt3 # If you want to use web just replace `gpt3` with `gpt3web as gpt3` and no other changes needed.

prompt = input("👦 > ")
resp = gpt3.Completion.create(prompt=prompt)
print(f"🤖 > {resp.text}")
```
#### GPT-4:

```python
from freeGPT import gpt4  # If you want to use web just replace `gpt4` with `gpt4web as gpt4` and no other changes needed.

token = gpt4.Account.create(logging=True) # Don't forget to remove this if you want to use web.
prompt = input("👦 > ")
resp = gpt4.Completion.create(prompt=prompt, token=token) # Don't forget to remove the token parameter here if you want to use web.
print(f"🤖 > {resp.text}")
```

## Star History:
[![Star History Chart](https://api.star-history.com/svg?repos=Ruu3f/freeGPT&type=Date)](https://github.com/Ruu3f/freeGPT/stargazers)


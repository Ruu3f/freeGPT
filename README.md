#### *Latest: 5 MORE STARS FOR INTERNET SEARCH GPT MODELS*
[![PyPI version](https://badge.fury.io/py/freeGPT.svg)](https://badge.fury.io/py/freeGPT)
[![Downloads](https://static.pepy.tech/personalized-badge/freeGPT?period=month&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/freeGPT)
# freeGPT
A Python package that gives access to GPT3 &amp; GPT4 models for free.
<br>
*Get started by doing: `pip install freeGPT`*

## Examples:

#### GPT-3:

```python
from freeGPT import gpt3

def send_prompt():
    try:
        prompt = input("> ")
        response = gpt3.Completion.create(prompt=prompt)
        print("Response:", response.text)
    except Exception as e:
        print("Error:", str(e))

while True:
    send_prompt()
```
#### GPT-4:

```python
from freeGPT import gpt4

token = gpt4.Account.create(logging=True)
print("Token:", token) 

def send_prompt():
    try:
        prompt = input("> ")
        for response in gpt4.Completion.create(prompt=prompt, token=token):
            print("Response:", response.text)
    except Exception as e:
        print("Error:", str(e))

while True:
    send_prompt()
```

## Source:
*Models with .web have internet access on.*
<br>
| Models            | Websites                                 |
| ----------------- | -----------------------------------------|
| gpt3              | [theb.ai](https://theb.ai)               |
| gpt3.web          | [you.com](https://you.com)               |
| gpt4              | [useless.com](https://ai.useless.com)    |
| gpt4.web          | [forefront.ai](https://chat.forefront.ai)|

### TODO-List:
- [x] Add GPT-4.
- [x] Make the library well-documented.
- [x] Make the over-all library easier to use.
- [x] Make the over-all library easier to understand.
- [x] Replace you.com with theb.ai for less failed responses.
- [ ] Add a internet search model for GPT-3 & GPT-4
- [ ] Make a discord bot
- [ ] Add text to image generation

## Star History:
[![Star History Chart](https://api.star-history.com/svg?repos=Ruu3f/freeGPT&type=Date)](https://github.com/Ruu3f/freeGPT/stargazers)

## Discord Server:
#### Join my server to support me :D
#### -> [discord.gg/NcQ26PrNDp](https://discord.gg/NcQ26PrNDp)


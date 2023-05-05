# freeGPT
A Python package that gives access to GPT3 &amp; GPT4 models for free
## Examples
### [gpt3 (you.com)](https://you.com)
```python
from freeGPT import gpt3

chat = []

while True:
    prompt = input("> ")
    response = gpt3.Completion.create(
        prompt=prompt,
        chat=chat)
    print("Response:", response.text)
    chat.append({"question": prompt, "answer": response.text})
```
### [gpt4 (null)](null)
```python
from freeGPT import gpt4

# IN PROGRESS
```

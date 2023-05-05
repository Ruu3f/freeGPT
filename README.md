# freeGPT
A Python package that gives access to GPT3 &amp; GPT4 models for free
## Docs
### Example: `usesless` <a name="example-usesless"></a>

```python
from gpt4free import usesless

message_id = ""
while True:
    prompt = input("Question: ")
    if prompt == "!stop":
        break

    req = usesless.Completion.create(prompt=prompt, parentMessageId=message_id)

    print(f"Answer: {req['text']}")
    message_id = req["id"]
```

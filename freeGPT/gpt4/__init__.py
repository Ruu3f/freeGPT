import requests
import json


class Completion:
    headers = {
        "authority": "ai.usesless.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.5",
        "cache-control": "no-cache",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0",
    }

    @staticmethod
    def create(
        prompt: str = "",
        systemMessage: str = "You are a helpful assistant",
        parentMessageId: str = "",
        presence_penalty: float = 1,
        temperature: float = 1,
    ):
        print(parentMessageId, prompt)
        
        json_data = {
            "openaiKey": "",
            "prompt": prompt,
            "options": {
                "parentMessageId": parentMessageId,
                "systemMessage": systemMessage,
                "completionParams": {
                    "presence_penalty": presence_penalty,
                    "temperature": temperature,
                    "model": "gpt4",
                },
            },
        }

        url = "https://ai.usesless.com/api/chat-process"
        request = requests.post(url, headers=Completion.headers, json=json_data)
        content = request.content
        
        class Response:
            def __init__(self, content):
                self.content = content

            @property
            def text(self):
                return self.content.decode("utf-8")

        return Response(content)

if response.text is None:
    raise Exception("Unable to get the response, please try again later.")

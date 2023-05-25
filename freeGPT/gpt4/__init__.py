import requests
import json


class Completion:
    """
    A class for making requests to the AI completion API and retrieving responses.
    """

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
        """
        Creates a request to the AI completion API with the specified parameters.

        Args:
            prompt (str): The text prompt for the AI model.
            systemMessage (str): The system message for the conversation.
            parentMessageId (str): The ID of the parent message.
            presence_penalty (float): Controls the level of randomness in the AI model's responses based on previous messages.
            temperature (float): Controls the randomness of the AI model's responses.

        Returns:
            Response: An object containing the API response.
        """
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
            """
            Represents the response from the AI completion API.
            """

            def __init__(self, content):
                self.content = content

            @property
            def text(self):
                """
                Get the text content of the response.

                Returns:
                    str: The text content of the response.
                """
                return self.content.decode("utf-8")

        return Response(content)


if response.text is None:
    raise Exception("Unable to get the response, please try again later.")

from enum import Enum
from freeGPT import gpt3, gpt4

__author__ = "Ruu3f"
__version__ = "1.1.1"

class Provider(Enum):
    GPT3 = 'gpt3'
    GPT4 = 'gpt4'


class Completion:
    @staticmethod
    def create(provider: Provider, prompt: str, **kwargs) -> str:
        if provider == Provider.GPT3:
            return Completion.__gpt3_service(prompt, **kwargs)
        elif provider == Provider.GPT4:
            return Completion.__gpt4_service(prompt, **kwargs)
        else:
            raise Exception("Provider doesn't exist. Please check it again.")

    @staticmethod
    def __gpt3_service(prompt: str) -> str:
        resp = gpt3.Completion.create(prompt=prompt)
        return resp['text']

    @staticmethod
    def __gpt4_service(prompt: str) -> str:
        return gpt4.Completion.create(prompt=prompt).text

from enum import Enum
from freeGPT import gpt3, gpt3web, gpt4, gpt4web

__author__ = "Ruu3f"
__version__ = "1.0.8"

class Provider(Enum):
    GPT3 = 'gpt3'
    GPT3WEB = 'gpt3web'
    GPT4 = 'gpt4'
    GPT4WEB = 'gpt4web'


class Completion:
    @staticmethod
    def create(provider: Provider, prompt: str, **kwargs) -> str:
        if provider == Provider.GPT3:
            return Completion.__gpt3_service(prompt, **kwargs)
        elif provider == Provider.GPT3WEB:
            return Completion.__gpt3web_service(prompt, **kwargs)
        elif provider == Provider.GPT4:
            return Completion.__gpt4_service(prompt, **kwargs)
        elif provider == Provider.GPT4WEB:
            return Completion.__gpt4web_service(prompt, **kwargs)
        else:
            raise Exception("Provider doesn't exist. Please check it again.")

    @staticmethod
    def __gpt3_service(prompt: str) -> str:
        return gpt3.Completion.create(prompt=prompt).text

    @staticmethod
    def __gpt3web_service(prompt: str) -> str:
        return gpt3web.Completion.create(prompt=prompt).text

    @staticmethod
    def __gpt4_service(prompt: str) -> str:
        return gpt4.Completion.create(prompt=prompt).text

    @staticmethod
    def __gpt4web_service(prompt: str) -> str:
        return gpt4web.Completion.create(prompt=prompt).text

from enum import Enum
from freeGPT import gpt3, gpt4

__author__ = "Ruu3f"
__version__ = "1.0.1"

class Provider(Enum):
    gpt3 = 1
    gpt4 = 2

class Completion:

    @staticmethod
    def create(provider: Provider, prompt: str, **kwargs) -> str:

        if provider == Provider.gpt3:
            return Completion.__gpt3_service(prompt, **kwargs)
        elif provider == Provider.gpt4:
            return Completion.__gpt4_service(prompt, **kwargs)
        else:
            raise ValueError("Invalid provider value")

    @staticmethod
    def __gpt3_service(prompt: str, **kwargs) -> str:
        return gpt3.Completion.create(prompt, **kwargs).text

    @staticmethod
    def __gpt4_service(prompt: str, **kwargs) -> str:
        return gpt4.Completion.create(prompt=prompt, **kwargs).text
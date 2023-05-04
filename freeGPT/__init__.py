from freeGPT import gpt3

__author__ = "Ruu3f"
__email__ = "ruu3f0@gmail.com"
__version__ = "1.0.0"

class Completion:
    @staticmethod
    def create(prompt: str, **kwargs) -> str:
        return gpt3.Completion.create(prompt, **kwargs).text
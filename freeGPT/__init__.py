from enum import Enum
from freeGPT import gpt3, gpt4

__author__ = "Ruu3f"
__version__ = "1.1.2"
__all__ = ["Provider", "Completion"]


class Provider(Enum):
    """Enum class representing the available GPT providers."""

    GPT3 = "gpt3"
    GPT4 = "gpt4"


class Completion:
    """Class for generating completions using different GPT providers."""

    @staticmethod
    def create(provider: Provider, prompt: str, **kwargs) -> str:
        """
        Generates a completion using the specified provider.

        Args:
            provider (Provider): The GPT provider to use.
            prompt (str): The prompt text for completion.
            **kwargs: Additional keyword arguments specific to the provider.

        Returns:
            str: The generated completion text.

        Raises:
            Exception: If the provider doesn't exist.
        """
        if provider == Provider.GPT3:
            return Completion.__gpt3_service(prompt, **kwargs)
        elif provider == Provider.GPT4:
            return Completion.__gpt4_service(prompt, **kwargs)
        else:
            raise Exception("Provider doesn't exist. Please check it again.")

    @staticmethod
    def __gpt3_service(prompt: str) -> str:
        """
        Generates a completion using the GPT-3 provider.

        Args:
            prompt (str): The prompt text for completion.

        Returns:
            str: The generated completion text.
        """
        resp = gpt3.Completion.create(prompt=prompt)
        return resp["text"]

    @staticmethod
    def __gpt4_service(prompt: str) -> str:
        """
        Generates a completion using the GPT-4 provider.

        Args:
            prompt (str): The prompt text for completion.

        Returns:
            str: The generated completion text.
        """
        return gpt4.Completion.create(prompt=prompt).text

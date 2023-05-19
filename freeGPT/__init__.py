"""
Package for text completions using GPT-3 and GPT-4 models.

This package provides a convenient interface for generating text completions
using the GPT-3 and GPT-4 models. It includes a `Provider` enum for selecting
the desired model and a `Completion` class for creating text completions.
"""

from enum import Enum
from .freeGPT import gpt3, gpt4

__author__ = "Ruu3f"
__version__ = "1.0.1"

__all__ = ["Provider", "Completion"]


class Provider(Enum):
    """Enum class representing the available GPT providers."""

    GPT3 = 1
    GPT4 = 2


class Completion:
    """Class for generating text completions using GPT models."""

    @staticmethod
    def create(provider: Provider, prompt: str, **kwargs) -> str:
        """
        Create a text completion using the specified GPT provider.

        Args:
            provider (Provider): The GPT provider (GPT3 or GPT4).
            prompt (str): The prompt for text completion.
            **kwargs: Additional keyword arguments to pass to the GPT provider.

        Returns:
            str: The generated text completion.

        Raises:
            ValueError: If an invalid provider value is provided.
        """
        if provider == Provider.GPT3:
            return Completion._gpt3_service(prompt, **kwargs)
        elif provider == Provider.GPT4:
            return Completion._gpt4_service(prompt, **kwargs)
        else:
            raise ValueError("Invalid provider value")

    @staticmethod
    def _gpt3_service(prompt: str, **kwargs) -> str:
        """
        Create a text completion using GPT-3 model.

        Args:
            prompt (str): The prompt for text completion.
            chat (list): The list for storing the questions and the GPT response.
            **kwargs: Additional keyword arguments to pass to the GPT-3 model.

        Returns:
            str: The generated text completion.
        """
        return gpt3.Completion.create(prompt, **kwargs).text

    @staticmethod
    def _gpt4_service(prompt: str, **kwargs) -> str:
        """
        Create a text completion using GPT-4 model.

        Args:
            token (account): The created accounts token.
            prompt (str): The prompt for text completion.
            **kwargs: Additional keyword arguments to pass to the GPT-4 model.

        Returns:
            str: The generated text completion.
        """
        return gpt4.Completion.create(prompt=prompt, **kwargs).text

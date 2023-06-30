from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    README = f.read()

setup(
    name="freeGPT",
    version="1.2.1",
    description="freeGPT provides free access to GPT3, GPT4 and more models.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Ruu3f/freeGPT",
    author="Ruu3f",
    license="GPLv3",
    keywords=[
        "artificial-intelligence",
        "machine-learning",
        "deep-learning",
        "gpt4free",
        "chatbot",
        "freegpt",
        "chatgpt",
        "python",
        "openai",
        "llama",
        "free",
        "gpt4",
        "gpt3",
        "gpt",
        "ai",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    packages=find_packages(),
    install_requires=[
        "requests",
        "fake-useragent",
    ],
    project_urls={
        "Source": "https://github.com/Ruu3f/freeGPT",
        "Issues": "https://github.com/Ruu3f/freeGPT/issues",
        "Discord": "https://discord.gg/XH6pUGkwRr",
    },
)

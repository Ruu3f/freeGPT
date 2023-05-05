#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as readme_file:
    readme = readme_file.read()

with open("HISTORY.md", encoding="utf-8") as history_file:
    history = history_file.read()

requirements = [
    "websocket-client",
    "requests",
    "tls-client",
    "pypasser",
    "fake-useragent",
    "pydantic",
]

test_requirements = ['pytest>=3', ]

setup(
    author="Reza Shakeri",
    author_email='rzashakeri@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    description="decentralising the Ai Industry, just some language model api's...",
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords=[
        "gpt4free",
        "ChatGPT",
        "Free",
        "FreeChatGPT",
        "Ai"
    ],
    name='freeGPT',
    packages=find_packages(include=['freeGPT', 'freeGPT.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/Ruu3f/freeGPT',
    version='1.0.2',
    zip_safe=False,
    project_urls={
        "Homepage": "https://github.com/Ruu3f/freeGPT",
        "Issue tracker": "https://github.com/Ruu3f/freeGPT/issues",
        "Release notes": "https://github.com/Ruu3f/freeGPT/releases",
        "Source": "https://github.com/Ruu3f/freeGPT",
        "Discussions": "https://github.com/Ruu3f/freeGPT/discussions",
    },
)

import os

from setuptools import setup

NAME = "chatgptxblock"
VERSION = "0.1"
AUTHOR = "Oppa The Great, Viesse The Destroyer"
AUTHOR_EMAIL = "s.r.developervishal@gmail.com"
DESCRIPTION = "A XBlock for chatting with GPT-3."
KEYWORDS = "xblock chat gpt3"
URL = "https://github.com/SRDeveloperVishal/ChatGPT-XBlock"
CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
]
LICENSE = "Apache 2.0"
PACKAGES = [NAME]
INSTALL_REQUIRES = [
    "XBlock",
    "xblock-utils>=1.0.7",
    "requests",
]

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

with open("requirements.txt", "r") as fh:
    REQUIREMENTS = fh.readlines()

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    keywords=KEYWORDS,
    url=URL,
    classifiers=CLASSIFIERS,
    license=LICENSE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    packages=PACKAGES,
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    entry_points={
        "xblock.v1": [
            f"{NAME} = {NAME}.{NAME}:ChatGptXBlock",
        ],
    },
)

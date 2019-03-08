import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="everytime-parser",
    version="0.1.4",
    author="zaeval",
    author_email="zaeval@among.software",
    description="everytime-parser and it serve some utility",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zaeval/everytime-parser",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    zip_safe=False,
    install_requires=[
        "requests",
        "bs4",
    ],
)

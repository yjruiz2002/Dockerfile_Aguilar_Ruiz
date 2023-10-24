#!/usr/bin/python

from setuptools import setup
from setuptools import find_packages

def get_version():
    with open("cn_p2_simple_ws/__init__.py") as f:
        for line in f:
            if line.startswith("__version__"):
                return eval(line.split("=")[-1])

def get_requires():
    requirements_list = []
    with open("requirements.txt") as f:
        for line in f:
            requirements_list.append(line)
    return requirements_list

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name="cn_p2_simple_ws",
    version=get_version(),
    description="cn_p2_simple_ws",
    long_description=readme,
    author="Rómulo Rodríguez",
    packages=find_packages(),
    install_requires=get_requires(),
    include_package_data=True,
)

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run()

#!/usr/bin/env python
import os
import sys
from flask_script import Manager

from cn_p2_simple_ws import create_app

app = create_app()
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
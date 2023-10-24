#!/usr/bin/python
from setuptools import setup, find_packages

def get_requires():
    requirements_list = []
    with open("requirements.txt") as f:
        for line in f:
            requirements_list.append(line.strip())
    return requirements_list

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name="cn_p2_simple_ws",
    version='1.0.0',
    description="cn_p2_simple_ws",
    long_description=readme,
    author="Rómulo Rodríguez",
    packages=find_packages(),
    install_requires=get_requires(),
    include_package_data=True,
)
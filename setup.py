from setuptools import find_packages, setup

with open("REDME.md", "r") as fh:
    long_description = fh.read()

setup(
    name="dspt9-nastyalolpro",
    version="0.0.1", 
    author="Anastasia Lysenko",
    author_email="nastya@lysenko.ms",
    description="A set of helper functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="someurl"
    packages=find_packages()
)
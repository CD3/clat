from setuptools import setup
import os

VERSION = "1.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="clat",
    description="Command Line Analysis Tools: A collection of tools for doing data analysis.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="CD Clark III",
    url="https://github.com/CD3/clat",
    project_urls={
        "Issues": "https://github.com/CD3/clat/issues",
        "CI": "https://github.com/CD3/clat/actions",
        "Changelog": "https://github.com/CD3/clat/releases",
    },
    license="MIT",
    version=VERSION,
    packages=["clat"],
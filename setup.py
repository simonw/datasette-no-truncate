from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-no-truncate",
    description="Tiny Datasette plugin to disable text truncation in table displays",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-no-truncate",
    project_urls={
        "Issues": "https://github.com/simonw/datasette-no-truncate/issues",
        "CI": "https://github.com/simonw/datasette-no-truncate/actions",
        "Changelog": "https://github.com/simonw/datasette-no-truncate/releases",
    },
    license="Apache License, Version 2.0",
    classifiers=[
        "Framework :: Datasette",
        "License :: OSI Approved :: Apache Software License",
    ],
    version=VERSION,
    packages=["datasette_no_truncate"],
    entry_points={"datasette": ["no_truncate = datasette_no_truncate"]},
    install_requires=["datasette"],
    extras_require={"test": ["pytest", "pytest-asyncio"]},
    python_requires=">=3.7",
)

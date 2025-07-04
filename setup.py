from setuptools import setup
from setuptools import find_packages
from os import environ
from platform import system
from subprocess import run


def get_readme() -> str:
    with open("README.md", "r") as file:
        return file.read()


def get_requirements() -> list[str]:
    return [
        "aiohttp",
        "aiofiles",
        "ujson",
        "dataclasses",
        "dataclasses-json",
        "python-dateutil",
        "dill",
        "python-magic-bin" if system().lower() == "windows" else "python-magic"
    ]


def main():
    if "PREFIX" in environ and "/com.termux" in environ["PREFIX"]:
        print("Termux detected, checking Sox package...")
        if "sox" not in run(["pkg", "list-installed", "sox"], capture_output=True).stdout.decode("utf-8"):
            print("Sox not found, installing...")
            if run(["pkg", "install", "sox", "-y"], capture_output=True).returncode == 0:
                print("Sox has been successfully installed.")
            else:
                print("Failed to install Sox. The stability of the library is not guaranteed.")
        else:
            print("Sox found, no installation required.")

    setup(
        name="cloverspace",
        version="3.0.1",
        author="LixxRarin",
        description="An asynchronous library for creating scripts and chatbots in Clover.Space;",
        url="https://github.com/LixxRarin/Clover.Space/",
        packages=find_packages(),
        author_email="lixxrarin@gmail.com",
        install_requires=get_requirements(),
        long_description=get_readme(),
        long_description_content_type="text/markdown",
        python_requires=">=3.7",
        keywords=[
            "project-z", "projectz", "projz",
            "bots", "api", "supersymlab",
            "projz-bot", "projz-bots", "projz-api",
            "cloverspace", "clover-space"
        ]
    )


if __name__ == "__main__":
    main()

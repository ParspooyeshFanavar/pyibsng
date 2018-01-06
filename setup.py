from setuptools import setup, find_packages

setup(
    name="ibsng",
    version="1.0.0",
    description="IBSng Python Driver",
    author="Parspooyesh Fanavar",
    keywords="ibsng python driver library",
    install_requires=['requests',],
    packages=find_packages(),
)

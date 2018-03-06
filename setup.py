"""Package setup."""
from setuptools import setup, find_packages

setup(
    name="pyibsng",
    version="1.2.3",
    description="IBSng python driver",
    long_description=open("README.rst").read(),
    author="Parspooyesh Fanavar",
    author_email="info@parspooyesh.com",
    url="https://github.com/ParspooyeshFanavar/pyibsng",
    license="MIT",
    keywords=["ibsng", "driver", "library", "json-rpc", "rpc"],
    install_requires=['requests'],
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Terminals",
        "Intended Audience :: Developers",
    ],
)

from setuptools import find_packages, setup

__version__ = "0.0.1"

setup(
    name="smart-sense",
    version=__version__,
    packages=find_packages(),
    install_requires=[
        "numpy",
        ],
)

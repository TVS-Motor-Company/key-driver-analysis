import pathlib
from setuptools import setup, find_packages
import os

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# Get the code version
version = {}
with open(os.path.join(HERE, "key_driver_analysis/version.py")) as fp:
    exec(fp.read(), version)
__version__ = version["__version__"]

setup(
    name="key-driver-analysis",
    version=__version__,
    description="Key Driver Analysis",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/bnriiitb/key-driver-analysis",
    author="Nagaraju Budigam",
    author_email="nagaraju.iith@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=["numpy>=1.21.3", "pandas>=1.3.4", "scikit_learn>=1.0.1", "setuptools>=58.0.4"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ]
)

from setuptools import setup, find_packages
from codecs import open
import os

here = os.path.abspath(os.path.dirname(__file__))


def read_text(fname):
    if os.path.isfile(fname):
        with open(os.path.join(here, fname)) as f:
            return f.read()
    else:
        print("warning: file {} does not exist".format(fname))
        return ""


setup(
    name="jsonkv",  # Required
    version="1.1.7",  # Required
    description="Use JSON file as KV store easily",
    long_description=read_text("README.md"),  # Optional
    long_description_content_type="text/markdown",  # Optional (see note above)
    url="https://github.com/weaming/jsonkv",  # Optional
    author="weaming",  # Optional
    author_email="garden.yuen@gmail.com",  # Optional
    packages=find_packages(),
    # install_requires=[
    #     l
    #     for l in read_text("requirements.txt").split("\n")
    #     if l.strip() and not l.strip().startswith("#")
    # ],
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 4 - Beta",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        # Pick your license as you wish
        "License :: OSI Approved :: MIT License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    keywords="json kv store",  # Optional
)

## setup.py is the build script for setuptools. It tells setuptools about your 
## package (such as the name and version) as well as which code files to include.

import setuptools

# Use the README file as the long description content
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-LukJA", # Unique PyPI Package Name
    version="0.0.2",
    author="Luke Andrews",
    author_email="l.j.andrews.uk@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LukJA/NoTeX-Concept",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'hello-world-demo=example_pkg:hello_world',
            ],
    },
    python_requires='>=3.6',
)
from setuptools import setup, find_packages


with open("README.md", "r") as f:
    description = f.read()

setup(
    name="Redframe_hello",
    version="0.0.5",
    packages=find_packages(),
    description="This is a example project to demonstrate how to create a Python package and publish it to PyPI by Redframe",
classifiers=[
"Programming Language :: Python :: 3",
"License :: OSI Approved :: MIT License",
"Operating System :: OS Independent",
],
    install_requires=[
        # Add dependencies here.
        # e.g. 'numpy>=1.11.1'
        # flask
    ],
    entry_points={
        "console_scripts": [
            "Redframe_hello = Redframe_hello:hello",
        ],
    },
    long_description=description,
    long_description_content_type="text/markdown",
)

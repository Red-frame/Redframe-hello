from setuptools import setup, find_packages


with open("README.md", "r") as f:
    description = f.read()

setup(
    name="Redframe_hello",
    version="0.0.2",
    packages=find_packages(),
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

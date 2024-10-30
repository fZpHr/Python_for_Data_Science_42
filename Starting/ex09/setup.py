from setuptools import setup, find_packages

setup(
    name="ft_package",
    version="0.0.1",
    description="A sample test package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="zeph",
    author_email="zeph@42.fr",
    url="https://github.com/fZpHr/Python_for_Data_Science_42/tree/main/Starting/ex09/ft_package",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)

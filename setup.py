import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="predictit-data",
    version="0.0.1",
    author="Jordan Baird",
    author_email="jjordanbaird@gmail.com",
    description="Predictit API Wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jjordanbaird/predictit-data",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=['requests']
)
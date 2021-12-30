from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="LiHiSTO",
    version="0.0.1",
    author="Swati Rajwal",
    author_email="rajwalswati213@gmail.com",
    description="A package with a comprehensive list of 820 Hindi Stopwords",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/semicolon123/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/semicolon123/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={"": ["*.txt"]},
    python_requires=">=3.6",
)
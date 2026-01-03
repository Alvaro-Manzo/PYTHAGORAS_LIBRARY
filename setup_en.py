from setuptools import setup, find_packages

with open("README_EN.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Pythagorean",
    version="1.0.0",
    author="Alvaro-Manzo",
    author_email="jogobonito029@gmail.com",
    description="Professional module for Pythagorean theorem calculations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Alvaro-Manzo/PYTHAGOREAN_LIBRARY",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    python_requires=">=3.8",
    keywords="pythagorean theorem calculator triangle mathematics right-triangle",
)

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as archivo:
    descripcion_larga = archivo.read()

setup(
    name="Pytagoras",
    version="1.0.0",
    author="Alvaro-Manzo",
    author_email="jogobonito029@gmail.com",
    description="Biblioteca profesional para calculos del teorema de Pitagoras",
    long_description=descripcion_larga,
    long_description_content_type="text/markdown",
    url="https://github.com/Alvaro-Manzo/PYTHAGORAS_LIBRARY",
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
    keywords="pitagoras triangulo teorema rectangulo matematicas calculo",
)

from setuptools import setup, find_packages

setup(
    name="PrintNightmare",
    version="1.0.0",
    author="KcanCurly",
    description="Toolkit for abusing GPO.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/KcanCurly/PrintNightmare",
    packages=find_packages(),
    install_requires=[
        "impacket",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
    ],
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "printnightmare.py=src.printnightmare:main",
        ],
    },
)
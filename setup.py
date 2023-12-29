from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

VERSION = "0.1.2"
setup(
    name="salla-python-sdk",
    version=VERSION,
    description="A python SDK for salla integration",
    package_dir={"": "sdk"},
    packages=find_packages(where="sdk", exclude="tests"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/9ai-in/salla-python-sdk/",
    author="9AI",
    author_email="team@9ai.in",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    keywords=[
        "salla",
        "salla-sdk",
        "salla-api",
        "salla-python",
    ],
    install_requires=[
        "pydantic~=1.10.2",
        "aiohttp==3.9.1",
        "python-dotenv==1.0.0",
    ],
    extras_require={
        "dev": ["pytest>=7.4.3", "pytest-asyncio>=0.23.2", "twine>=4.0.2"],
    },
    python_requires="~=3.10",
)

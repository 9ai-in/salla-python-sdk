from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt", encoding="utf-8") as require_file:
    dependencies = [require.strip() for require in require_file]

VERSION = "1.0.0"
setup(
    name="salla-sdk",
    version=VERSION,
    description="A SDK for salla integration",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/9ai-in/salla-sdk",
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
    install_requires=dependencies,
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.10",
)

from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

REPO_Name = "Book-recommendation-api"
AUTHOR_USER_NAME = "levy123"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ["streamlit", "numpy"]

setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small package for a Book Recommendation System",
    long_description=long_description,
    long_description_content_type="test/markdown",
    url="https://github.com/levy123/Book-recommendation-api",
    author_email="levylauren909@gmail.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires="3.10",
    install_requires=LIST_OF_REQUIREMENTS,
)
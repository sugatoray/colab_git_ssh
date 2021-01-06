import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="colab_git_ssh", 
    version="0.0.1",
    author="Sugato Ray",
    author_email="sugatoray.dev@gmail.com",
    description="A python library to help setup SSH on Colab and access Git cloud providers like: GitHub, GitLab, BitBucket.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sugatoray/colab_git_ssh",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux/Unix",
    ],
    python_requires='>=3.6',
)

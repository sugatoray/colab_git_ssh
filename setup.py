import setuptools
import re
import os

###--------------------------------------------------###

# To include __version__ see this:
#   1. https://packaging.python.org/guides/single-sourcing-package-version/
#   2. https://stackoverflow.com/questions/458550/standard-way-to-embed-version-into-python-package
#   3. example: https://github.com/tahoe-lafs/zfec/blob/42dededf9d0ddbb165cdfccbd5acdf6e0600cb4b/setup.py#L83

PKG = "colab_git_ssh"
VERSIONFILE = os.path.join(PKG, "_version.py")
verstr = "unknown"
# try:
#     verstrline = open(VERSIONFILE, "rt").read()
# except EnvironmentError:
#     pass # Okay, there is no version file.
# else:
#     VSRE = r"^verstr = ['\"]([^'\"]*)['\"]"
#     mo = re.search(VSRE, verstrline, re.M)
#     if mo:
#         verstr = mo.group(1)
#     else:
#         print "unable to find version in %s" % (VERSIONFILE,)
#         raise RuntimeError("if %s.py exists, it is required to be well-formed" % (VERSIONFILE,))

###--------------------------------------------------###
               
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name=PKG, 
    version=verstr, # "0.0.1"
    author="Sugato Ray",
    author_email="sugatoray.dev@gmail.com",
    description="A python library to help setup SSH on Colab and access both public and private repositories on Git cloud providers like: GitHub, GitLab, BitBucket.",
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

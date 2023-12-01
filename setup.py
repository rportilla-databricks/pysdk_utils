from setuptools import find_packages, setup
#from version import get_latest_git_tag

# fetch the most recent version tag to use as build version
#build_version = get_latest_git_tag()

# use the contents of the README file as the 'long description' for the package
with open("./README.md", "r") as fh:
    long_description = fh.read()

#
# build the package
#
setup(
    name="dip-connect",
    version="0.0.1",
    author="Ricardo Portilla",
    author_email="ricardo.portilla@databricks.com",
    description="one-step-connect",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(where=".", include=["dip_connect"]),
    install_requires=[],
    extras_require=dict(tests=["pytest"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
)
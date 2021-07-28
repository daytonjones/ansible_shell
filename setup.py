import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ansible_shell',
    version='0.0.1',
    description='A "shell" for ansible',
    long_description=file: README.md
    long_description_content_type="text/markdown",
    url='http://github.com/daytonjones/ansible_shell',
    author='Dayton Jones',
    author_email='dayton@gecko.org',
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)

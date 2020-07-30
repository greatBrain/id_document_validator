import setuptools

setuptools.setup(
    name = "Identification Document Validator - roy-mustang",
    version = "0.0.1",
    author = "Erick M. Fana",
    author_email = "efanaportes@gmail.com", 
    description = "A simple Identity Document Characters Validator",
    url = "github repository", 
    packages = setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    python_requires='>=3.7',
)
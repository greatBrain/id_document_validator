import setuptools

setuptools.setup(
    name = "identity-validator",
    version = "0.0.1",
    author = "Erick M. Fana (roy-mustang)",
    author_email = "efanaportes@gmail.com", 
    description = "A simple Identity Document Characters Validator (just for DNI and cedula documents)",
    url = "https://github.com/greatBrain/identity-validator", 
    packages = setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    python_requires='>=3.7',
)
from setuptools import setup , find_packages

setup(
    name="crypto",
    version="1.0.0",
    packages=find_packages(where="src"), 
    install_requires = [
        "typer[all]",
    ],
    package_dir={"":"src"},
    include_package_data=True
    # entry_points={
    #      "console_scripts": [
    #         "crypto=main:app",
    #     ],
    # }
)
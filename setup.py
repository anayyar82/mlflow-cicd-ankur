from setuptools import find_packages, setup
from mlflow_cicd_ankur import __version__

setup(
    name="mlflow_cicd_ankur",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    version=__version__,
    description="",
    author=""
)

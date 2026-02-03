from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

from sixth_gear import __version__ as version

setup(
    name="sixth_gear",
    version=version,
    description="Sixth Gear: A hybrid LifeOS and Second Brain Frappe App",
    author="Jules",
    author_email="jules@example.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
)

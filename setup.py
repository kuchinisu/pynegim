from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

AUTHOR = 'kuchinisu'
AUTHOR_EMAIL = 'rodolfoescamilla2011@hotmail.com'
PACKAGE_NAME = 'pynegim'
VERSION = '0.0.4'

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    install_requires=requirements,
    packages=find_packages(include=[PACKAGE_NAME, f'{PACKAGE_NAME}.*']),
    include_package_data=True,
)

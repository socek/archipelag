from setuptools import find_packages
from setuptools import setup

install_requires = [
]

if __name__ == '__main__':
    setup(
        name='archipelag',
        version='0.1',
        packages=find_packages(),
        install_requires=install_requires,
        license='Apache License 2.0',
    )

from setuptools import find_packages
from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

REQUIRED_PACKAGES = [
    'certifi==2020.12.5',
    'chardet==4.0.0',
    'idna==2.10',
    'requests==2.25.1',
    'urllib3==1.26.4',
]

setup(
    name='BannerPy',
    version='1.0.0',
    description='A python app that shows a banner from a GitHub gist',
    author='Sergio Segura',
    author_email='TheLastRKoch@gmail.com',
    url="https://github.com/TheLastRKoch/BannerPy",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'bannerpy = src.app:main'
        ]
    },
    install_requires=REQUIRED_PACKAGES,
)

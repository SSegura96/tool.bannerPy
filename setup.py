from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = [
    'requests'
]

setup(
    name='BannerPy',
    version='2.1.1',
    description='A python app that shows a banner from a GitHub gist',
    author='Sergio Segura',
    author_email='TheLastRKoch@gmail.com',
    url="https://github.com/TheLastRKoch/tool.BannerPy",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'bannerpy = app:main'
        ]
    },
    install_requires=REQUIRED_PACKAGES,
)

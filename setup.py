from setuptools import setup, find_packages

setup(
    name='subdomainizer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'termcolor==1.1.0',
        'argparse==1.4.0',
        'beautifulsoup4==4.6.3',
        'requests==2.21.0',
        'htmlmin==0.1.12',
        'tldextract==2.2.0',
        'colorama==0.4.4',
        'cffi'
    ],
    entry_points={
        'console_scripts': [
            'subdomainizer = subdomainizer.subdomainizer:main',
        ],
    },
)

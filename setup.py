from setuptools import setup, find_packages

setup(
    name='quote-btc',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests>=2.32.0,<3.0.0',
        'certifi~=2025.1.31',
        'charset-normalizer~=3.4.1',
        'idna~=3.10',
        'urllib3~=2.4.0',
    ],
    entry_points={
        'console_scripts': [
            'quote-btc=app.main:main',
        ],
    },
)
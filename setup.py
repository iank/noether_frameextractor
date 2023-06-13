from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='frameextractor',
    version='0.4.2',
    packages=find_packages(),
    install_requires=required,

    # For torch+cpu
    dependency_links=[
        'https://download.pytorch.org/whl/torch_stable.html'
    ],
)

from setuptools import setup, find_packages

setup(
    name='pythonalgos',
    version='0.0.1',
    package_dir={'': 'pythonalgos'},
    packages=find_packages(where='pythonalgos'),
    description='python algos',
    tests_require=['pytest']
)

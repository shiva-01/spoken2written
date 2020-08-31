from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='spoken_to_written',
    long_description=long_description,
    packages=['spoken_to_written'],
    install_requires=['word2number'],
    include_package_data=True,
    package_dir={'spoken_to_written': 'spoken_to_written'},
    package_data={'spoken_to_written': ['conversion_rules.json']}
)
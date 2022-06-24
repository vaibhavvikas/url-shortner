#!/usr/bin/env python

"""The setup script."""
from pathlib import Path
from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

test_requirements = ['pytest>=3', ]

project_dir = Path(__file__).parent

setup(
    author="Vaibhav Vikas",
    author_email='vbhvvikas@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A python flask application to shorten the URL provided by users whether rigestered or not.",
    install_requires=project_dir.joinpath('requirements.txt').read_text().split("\n"),
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='url_shortner',
    name='url_shortner',
    packages=find_packages(include=['url_shortner', 'url_shortner.*']),
    project_dir={"":"url_shortner"},
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/vaibhavvikas/url-shortner',
    version='0.1.0',
    zip_safe=False,
)

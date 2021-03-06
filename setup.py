#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import os
from collections import defaultdict
from setuptools import setup, find_packages


with open('README.md') as readme_file:
    readme = readme_file.read()


with open('HISTORY.md') as history_file:
    history = history_file.read()


install_requires = [
    'Keras>=2.1.6',
    'featuretools>=0.1.17',
    'lightfm>=1.15',
    'networkx>=2.0',
    'numpy>=1.14.0',
    'opencv-python>=3.4.0.12',
    'python-louvain>=0.10',
    'scikit-image>=0.13.1',
    'scikit-learn>=0.19.1',
    'scipy>=1.1.0',
]


tests_require = [
    'pytest>=3.4.2',
]


setup_requires = [
    'pytest-runner>=2.11.1',
]


development_requires = [
    'Sphinx>=1.7.1',
    'autoflake>=1.1',
    'autopep8>=1.3.5',
    'bumpversion>=0.5.3',
    'coverage>=4.5.1',
    'flake8>=3.5.0',
    'isort>=4.3.4',
    'pip>=10.0.1',
    'pycodestyle==2.3.1',
    'pyflakes==1.6.0',
    'recommonmark>=0.4.0',
    'sphinx_rtd_theme>=0.2.4',
    'tox>=2.9.1',
    'twine>=1.10.0',
    'wheel>=0.30.0',
]


extras_require = {
    'test': tests_require,
    'dev': tests_require + development_requires,
}


json_primitives = glob.glob('jsons/**/*.json', recursive=True)
data_files = defaultdict(list)
for primitive_path in json_primitives:
    parts = primitive_path.split('/')
    dir_path = parts[1:-1]
    install_path = os.path.join('mlprimitives', *dir_path)
    data_files[install_path].append(primitive_path)


setup(
    author="MIT Data To AI Lab",
    author_email='dailabmit@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    data_files = list(data_files.items()),
    description="MLBlocks Primitives",
    extras_require=extras_require,
    install_requires=install_requires,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='mlblocks mlprimitives',
    name='mlprimitives',
    packages=find_packages(include=['mlprimitives', 'mlprimitives.*']),
    python_requires='>=3.5',
    setup_requires=setup_requires,
    test_suite='tests',
    tests_require=tests_require,
    url='https://github.com/HDI-Project/MLPrimitives',
    version='0.0.1',
    zip_safe=False,
)

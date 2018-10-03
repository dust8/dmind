from os import path

from setuptools import find_packages, setup

from dmind import __version__

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='dmind',
    version=__version__,
    packages=find_packages(),
    description='A sample Python project',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/dust8/dmind',
    author='dust8',
    include_package_data=True,
    classifiers=[
        '5 - Production/Stable', 'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3', 'Framework :: IPython'
    ],
    keywords='dmind mind mindmap',
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/dust8/dmind',
        'Funding': '',
        'Say Thanks!': '',
        'Source': 'https://github.com/dust8/dmind',
    },
)

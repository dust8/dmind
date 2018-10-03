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
    description='a mindmap tool for jupyter notebook',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/dust8/dmind',
    author='dust8',
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7', 'Framework :: IPython'
    ],
    keywords='dmind mind mindmap')

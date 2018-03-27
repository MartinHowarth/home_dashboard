# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='home_dashboard',

    version='0.0.1',

    description='Home Dashboard',

    url='https://github.com/pypa/sampleproject',

    author='Martin Howarth',
    author_email='howarth.martin@gmail.com',

    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='tfl dashboard bus train home wifi',

    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    install_requires=[
        'dash',
        'dash-renderer',
        'dash-html-components',
        'dash-core-components',
        'gunicorn',
        'munch',
        'nre-darwin-py',
        'plotly',
        'requests',
        'schematics',
        'wifi-qrcode-generator',
    ],
)

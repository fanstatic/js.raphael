import os

from setuptools import find_packages
from setuptools import setup

version = '2.1.0'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    read('js', 'raphael', 'test_raphael.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(
    name='js.raphael',
    version=version,
    description="Fanstatic packaging of Raphael",
    long_description=long_description,
    classifiers=[],
    keywords='',
    author='Fanstatic Developers',
    author_email='fanstatic@googlegroups.com',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    setup_requires=['hgtools'],
    install_requires=[
        'fanstatic',
        'setuptools',
        ],
    entry_points={
        'fanstatic.libraries': [
            'raphael = js.raphael:library',
            ],
        },
    )

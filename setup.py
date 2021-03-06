from setuptools import setup, find_packages

requires = [
    'six',
    'python-arango',
    'marshmallow~=2.10.0'
]

setup(
    name='arango-orm',
    version='0.4',
    description='A SQLAlchemy like ORM implementation for arangodb',
    long_description="A SQLAlchemy like ORM implementation using python-arango as the backend library",
    classifiers=[
        "Programming Language :: Python"
    ],
    author='Kashif Iftikhar',
    author_email='kashif@compulife.com.pk',
    url="https://github.com/threatify/arango-orm",
    download_url="https://github.com/threatify/arango-orm/archive/0.3.tar.gz",
    license="GNU General Public License v3 (GPLv3)",
    keywords='arangodb orm python',
    packages=find_packages(),
    install_requires=requires
)

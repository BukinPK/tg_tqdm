"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tg_tqdm',
    version='0.0.3',
    description='Extension for tqdm progressbar in Telegram',
    license='MPLv2.0, MIT Licences',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/BukinPK/tg_tqdm',
    author='Roman Troyan',
    author_email='bukinpk@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='progressbar progressmeter progress bar meter'
             ' rate eta console terminal time telegram',
    packages=['tg_tqdm'] + ['tg_tqdm.' + i for i in find_packages('tg_tqdm')],
    install_requires=['tqdm', 'python-telegram-bot'],
    project_urls={
        'Source': 'https://github.com/BukinPK/tg_tqdm',
    },
)
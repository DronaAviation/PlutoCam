import setuptools

import plutocam

with open('README.md') as fp:
    long_description = fp.read()

setuptools.setup(
    name='plutocam',
    version=plutocam.__version__,
    author='meekworth',
    author_email='meekworth@gmail.com',
    description='communicate with a lewei camera module',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/DronaAviation/plutocam',
    packages=setuptools.find_packages(),
    license='Apache License, Version 2.0',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [ 'plutocam=plutocam.__main__:main' ]
    }
)

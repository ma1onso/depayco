import setuptools

with open('README.md', 'r') as readme:
    long_description = readme.read()

setuptools.setup(
    name='depayco',
    version='1.0.2',
    license='GPL',
    author='Alonso',
    author_email='alons45@gmail.com',
    description='Django integration with ePayco (epayco.co)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ma1onso/depayco',
    packages=setuptools.find_packages(),
    install_requires=[
        'pyepayco==1.0.0',
        # TODO: don't repeat dependencies from pyepayco
        'requests >= 2.4.3',
        'pycrypto >= 2.3'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

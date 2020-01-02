import setuptools

with open('README.md', 'r') as readme:
    long_description = readme.read()

setuptools.setup(
    name='depayco',
    version='1.0',
    license='GPL',
    author='Alonso',
    author_email='alons45@gmail.com',
    description='Django integration with epayco.co',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ma1onso/depayco',
    packages=setuptools.find_packages(),
    install_requires=['pyepayco==1.0.0'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

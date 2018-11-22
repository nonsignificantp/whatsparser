import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='WhatsParser',
    version='0.6.0',
    author='Agustin Rodriguez',
    author_email='agustin.dev@protonmail.com',
    description='A parser for whatsapp .txt files',
    long_description=long_description[56:],
    long_description_content_type='text/markdown',
    url='https://github.com/nonsignificantp/whatsparser',
    license='MIT',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=['whatsapp', 'parser', 'text', 'dataframe']
)

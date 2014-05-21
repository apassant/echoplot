from distutils.core import setup

setup(
    name='echoplot',
    version='0.1.1',
    author='Alexandre Passant',
    author_email='alex@passant.org',
    packages=['echoplot'],
    scripts=['bin/echoplot'],
    url='http://pypi.python.org/pypi/echoplot',
    license='LICENSE.txt',
    description='Plot song data using the EchoNest API.',
    long_description=open('README.txt').read(),
    install_requires=[
        "matplotlib >= 1.3.1",
        "numpy >= 1.8.1",
        "pyechonest >= 8.0.1"
    ],
)

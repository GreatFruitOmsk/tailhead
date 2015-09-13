import os
from setuptools import setup


with open(os.path.join(os.path.dirname(__file__), 'tailhead', 'version.py')) as f:
    VERSION = None
    code = compile(f.read(), 'version.py', 'exec')
    exec(code)
    assert VERSION


setup(
    name='tailhead',
    packages=['tailhead'],
    version=VERSION,
    author='Mike Thornton',
    author_email='six8@devdetails.com',
    maintainer='Ilya Kulakov',
    maintainer_email='kulakov.ilya@gmail.com',
    url='https://github.com/GreatFruitOmsk/tailhead',
    download_url='https://github.com/GreatFruitOmsk/tailhead/releases',
    license='MIT',
    keywords=['tail', 'head'],
    description='tailhead is a simple implementation of GNU tail and head.',
    classifiers=[
        "Programming Language :: Python",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: POSIX",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        'Topic :: System :: Logging',
        'Topic :: Text Processing',
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: System Shells",
        "Topic :: System :: Systems Administration",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    long_description=open('README.rst').read(),
    entry_points="""
    [console_scripts]
    pytail=tailhead.__main__:main
    """
)

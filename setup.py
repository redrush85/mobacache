#coding=utf-8
from setuptools import setup


setup(
    name="moba-cache",
    version="1.1",
    author="Alexander Kuts",
    author_email="redrush85@gmail.com",
    description="mobacache is a pythonic interface for creating a cache over redis. "
                "It provides simple decorators that can be added to any function to cache its return values. ",
    license="MIT",
    keywords=["redis", "cache", "decorator"],
    url="https://github.com/redrush85/mobacache",
    download_url='https://github.com/redrush85/mobacache',
    packages=['mobacache'],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.5',
    ],
)
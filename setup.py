#-*- encoding: UTF-8 -*-
from setuptools import setup, find_packages


with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='charimg',
    version='0.0.1',
    author='insorker',
    author_email='insorker@qq.com',
    description="a tiny tool to print image in cmdline",
    long_description=long_description,
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    keywords='python image char',
    license='MIT',
    python_requires=">=3.6",

    packages = find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts':[
            'danmu.fm = danmufm.danmu:main'
        ]
    },
)

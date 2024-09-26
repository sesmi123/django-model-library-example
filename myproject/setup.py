from setuptools import setup, find_packages

setup(
    name='mymodels',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=4.2.16',
    ],
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
    ],
)

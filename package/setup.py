from setuptools import setup, find_namespace_packages

setup(
    packages=find_namespace_packages(include=('astronomer', 'astronomer.*')),
    setup_requires=[
        'pytest-runner~=5.3',
    ],
    tests_require=[
        'astronomer-certified-extensions[test]',
    ],
    extras_require={
        'test': [
            'pytest',
            'pytest-flask',
            'pytest-mock',
            'pytest-flake8',
        ],
    },
)

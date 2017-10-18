from setuptools import setup

setup(
    name='treedraw',
    description='specify and render tree diagrams',
    url='https://github.com/lyneca/treedraw',
    author='lyneca',
    license='MIT',
    version='1.1.0',
    packages=['treedraw'],
    install_requires=[
        'pycairo'
    ],
    entry_points={
        'console_scripts': [
            'treedraw = treedraw.__main__:main',
        ],
    },
    zip_safe=False
)

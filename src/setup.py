from setuptools import setup, find_packages
setup(
    name='brick-interface',
    version='0.0.6',
    packages=find_packages(),
    install_requires=[
        'pygame'
    ],
    entry_points={
        'console_scripts': [
            'brick-interface=brick_interface.main:run'
        ]
    }
)
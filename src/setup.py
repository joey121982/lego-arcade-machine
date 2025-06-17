from setuptools import setup
setup(
    name='brick-interface',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'brick-interface=main:run'
        ]
    }
)
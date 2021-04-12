from setuptools import setup

setup(
    name='stochastis',
    version='1.0.2',
    license="MIT",
    description=(
        'Encrypt data by storing it within a Python script that pretends to '
        'just be "obfuscated"'
    ),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='http://github.com/Pebaz',
    url='http://github.com/Pebaz/obfuscatron',
    py_modules=['main'],
    install_requires=['astor', 'brotli'],
    entry_points={
        'console_scripts' : [
            'obfuscatron=main:main'
        ]
    }
)

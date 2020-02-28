from setuptools import setup

setup(
    name='Package parser',
    version='1.0',
    description='Ubuntu/Debian status file parser',
    author='Joni Koskinen',
    author_email='joni.m.koskinen@gmail.com',
    packages=['src'],
    ext_package=['http.server', 'json'],
    package_data={
        '': ['.css', '.js', '.html', '.real']
    }
)
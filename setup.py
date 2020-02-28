from setuptools import setup

setup(
    name='Package parser',
    version='1.0',
    description='Ubuntu/Debian status file parser',
    author='Joni Koskinen',
    author_email='joni.m.koskinen@gmail.com',
    packages=['src'],
    requires=['http.server', 'json'],
    package_data={
        'src': ['*.css', '*.js', '*.html', '*.real']
    }
)
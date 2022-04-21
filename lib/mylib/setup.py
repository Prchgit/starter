from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='multip',
    url='https://github.com/Prchgit/mylib/',
    author='Prashant',
    author_email='jladan@uwaterloo.ca',
    # Needed to actually package something
    packages=['multip'],
    # Needed for dependencies
    install_requires=[],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='An example of a python package from pre-existing code',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)

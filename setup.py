from setuptools import setup

__version__ = (0, 0, 1)

setup(
    name='Algo_ADTs',
    description='Algorithms and Data Structures',
    version='.'.join(str(d) for d in __version__),
    author='Sangwon Lim',
    author_email='sangwonl@uvic.ca',
    packages=['ADT', 'algorithms'],

)
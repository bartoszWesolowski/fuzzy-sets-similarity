from setuptools import setup

#not tested yet
setup(name='fssimilarity',
      version='0.1',
      description='Tool for calculating fuzzy set similarity',
      url='https://github.com/bartoszWesolowski/fuzzy-sets-similarity/tree/master/python',
      author='Bartek W',
      author_email='fssimilarity@test.com',
      license='MIT',
      install_requires=[
          'markdown', 'flask_cors', 'flask', 'numpy', 'openpyxl', 'sklearn'
      ],
      zip_safe=False)
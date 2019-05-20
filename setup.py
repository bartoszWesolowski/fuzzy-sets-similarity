from setuptools import setup

# not tested yet
setup(name='fssimilarity',
      version='0.1',
      description='Tool for calculating fuzzy set similarity',
      url='https://github.com/bartoszWesolowski/fuzzy-sets-similarity/tree/master/python',
      author='Bartek Wesolowski',
      author_email='fssimilarity@test.com',
      license='MIT',
      install_requires=[
          'markdown==3.0.1', 'flask_cors==3.0.7', 'flask==1.0.2', 'numpy==1.16.2',
          'openpyxl==2.6.1', 'scikit-learn==0.20.3'
      ],
      zip_safe=False)

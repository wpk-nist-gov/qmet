from setuptools import setup

setup(name='qmet',
      version='0.0.1',
      description='qmet program', 
      long_description='',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.6',
      ],
      keywords='data analysis',
      url='https://github.com/wpk-nist-gov/qmet',
      author='William Krekelberg',
      author_email='wpk@nist.gov',
      license='NIST license https://www.nist.gov/director/licensing',
      packages=['qmet'],
      install_requires=[
#          'numpy>=1.13.3',
#          'pandas>=0.21.0',
#          'matplotlib>=2.1.0',
#          'seaborn>=0.8.0',
      ],
      # testing
      # setup_requires=['pytest-runner'],
      # tests_require=['pytest'],
      include_package_data=True,
      zip_safe=False)

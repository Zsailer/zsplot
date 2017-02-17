# Try using setuptools first, if it's installed
try:
    from setuptools import setup
except:
    from distutils.core import setup

# define all packages for distribution
packages = [
    'zsplot',
]

setup(name='zsplot',
      version='0.1.1',
      description='Complex plots that I find myself constantly remaking.',
      author='Zach Sailer',
      author_email='zachsailer@gmail.com',
      url='https://github.com/zsailer/zsplot',
      packages=packages,
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
      ],
      zip_safe=False)

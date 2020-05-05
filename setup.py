from setuptools import setup, find_packages

setup(name='pymdx-dd001',
      version='0.1',
      description='Collection of python-markdown extensions.',
      url='http://github.com/darkdragon-001/pymdx-dd001',
      author='Dark Dragon',
      author_email='darkdragon-001@web.de',
      license='MIT',
      packages=find_packages(),
      install_requires=['Markdown'],
      tests_require = ['pytest'],
      zip_safe=False)

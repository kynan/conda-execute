from setuptools import setup
import os.path

import versioneer


setup(name='conda-execute',
      version=versioneer.get_version(),
      description='A tool for executing scripts in a consistent environment.',
      author='Phil Elson',
      author_email='pelson.pub@gmail.com',
      url='https://github.com/pelson/conda-execute',
      packages=['conda_execute'],
      entry_points={
          'console_scripts': [
              'conda-execute = conda_execute.execute:main',
              'conda-tmpenv = conda_execute.tmpenv:main',
          ]
      },
      cmdclass=versioneer.get_cmdclass(),
     )


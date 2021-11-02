import sys
if len(sys.argv) == 1:
    sys.argv.append('install')

try:
    from setuptools import setup
except:
    from distutils.core import setup


setup(
    name='pypyodbc',
    version='1.3.6',
    description='PyPyODBC - A Pure Python ODBC module by ctypes',
    author='jiangwen365',
    author_email='jiangwen365 at gmail com',
    url='https://github.com/jiangwen365/pypyodbc',
    py_modules=['pypyodbc'],
      long_description="""

GitHub `Home Page <https://github.com/jiangwen365/pypyodbc/>`_


Also check out the `Wiki <https://github.com/jiangwen365/pypyodbc/wiki>`_ and 
`Version History <https://github.com/jiangwen365/pypyodbc/wiki/Version-History>`_

**Features**


 - One pure Python script, runs on CPython / IronPython / PyPy , Version 2.4 / 2.5 / 2.6 / 2.7 / 3.2 / 3.3, Win / Linux , 32 / 64 bit.

 - Almost totally same usage as pyodbc ( can be seen as a re-implementation of pyodbc in pure Python ).

 - Simple - the whole module is implemented in a single python script with less than 3000 lines.


    `A Hello World script of pypyodbc database programing <http://code.google.com/p/pypyodbc/wiki/A_HelloWorld_sample_to_access_mssql_with_python>`_

    `Built-in Access MDB file creation and compression functions on Windows <https://github.com/jiangwen365/pypyodbc/wiki/Access-MDB-support>`_


    `A DBI 2.0 SQLAlchemy enabler driver for IronPython <http://code.google.com/p/pypyodbc/wiki/Enable_SQLAlchemy_on_IronPython>`_

    `A DBI 2.0 SQLAlchemy enabler driver for *PyPy* <https://code.google.com/p/pypyodbc/wiki/Enable_SQLAlchemy_on_PyPy>`_



**Install**
- pip install pypyodbc""",
      classifiers=[
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python",
          "Development Status :: 4 - Beta",
      ],
      keywords='Python, Database, Interface, ODBC, PyPy',
      license='MIT',
      install_requires=[
        'setuptools',
      ],
      )

alfresco
********

Development
===========

Install
-------

Virtual Environment
-------------------

::

  virtualenv --python=python3.4 venv-alfresco
  source venv-alfresco/bin/activate
  pip install --upgrade pip

  pip install -r requirements.txt

Testing
-------

::

  find . -name '*.pyc' -delete
  py.test -x

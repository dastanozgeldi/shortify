Usage
=====

.. _installation:

Installation
------------

To use Shortify, first install it using pip:

.. code-block:: bash

   (env) $ pip install shortify

Or, you can clone directly from GitHub:

.. code-block:: bash

   (env) $ git clone https://github.com/Dositan/shortify

Running
-------
.. code-block:: bash

   (env) $ shortify --help

   usage: shortify <service> <url to shorten>

   Shortify Command-Line Interface.
   ...

Or, if you've done the installation through `git`, consider putting `python -m`
before `shortify`, to run Shortify as a package. Notice, you get the same output.

Examples
--------
In **shortify**, there are numerous URL-shortening services supported.
Let's use `TinyURL <https://tinyurl.com>`_ this time.
As you could notice before, the syntax is like the following:
`shortify <service> <url>`

.. code-block:: bash

   (env) $ shortify tinyurl https://sphinx-tutorial.readthedocs.io/step-1/?highlight=hyperlink#hyperlink-syntax

   https://tinyurl.com/yh6xukpw
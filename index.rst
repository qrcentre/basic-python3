.. Basic Programs with Python3 documentation master file, created by
   sphinx-quickstart on Sun Jul  8 14:56:46 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Basic Programs with Python3
===========================

This is a work in progress.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Part 1
======
.. literalinclude:: workshop/part1.py
    :language: python
    :linenos:

Part 2
======
.. literalinclude:: workshop/part2.py
    :language: python
    :linenos:

Part 3
======
.. literalinclude:: workshop/part3.py
    :language: python
    :linenos:

Docs
====
.. automodule:: basic_python3

NEA Weather API
---------------
.. autofunction:: basic_python3.weather_get_now
.. autofunction:: basic_python3.weather_get_rand

Telegram Bot API
----------------
.. autofunction:: basic_python3.telegram_whoami
.. autofunction:: basic_python3.telegram_send
.. autofunction:: basic_python3.telegram_get_updates

Miscellaneous Functions
-----------------------
.. autofunction:: basic_python3.mean

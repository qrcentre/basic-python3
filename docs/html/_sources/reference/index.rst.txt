Workshop Reference
==================

These are reference notes for the workshop.

Part 1
------

Numbers
^^^^^^^

Numbers in python work in the same way as in any calculator. The order of
operations apply.

.. code-block:: python

    >>> (1/4) * (27.3 + 25.9 + 28 + 26.5)
    26.925
    >>> (27.3-26.925)**2
    0.140625
    >>> (25.9-26.925)**2
    1.0506250000000044
    >>> (28 - 26.925)**2
    1.1556249999999986
    >>> (26.5-26.925)**2
    0.1806250000000006
    >>> (1/3) * (0.141 + 1.051 + 1.156 + 0.181)
    0.843

Strings
^^^^^^^

Strings are a sequence of characters. You can add them together end-to-end.
Strings are *not* compatible with numbers!

.. code-block:: python

   >>> 'Hello ' + 'world!'
   'Hello world!'
   >>> "Hello " + "world!"
   'Hello world!'
   >>> 'Hello ' + 80416
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: Can't convert 'int' object to str implicitly

Variables
^^^^^^^^^

Variables are a way to store *values*, for example numbers and strings. We
*assign* a value to a variable with the symbol ``=``, where the name of our new
variable is on the left, and the value it will hold is on the right.

.. code-block:: python

   >>> jelly = 52
   >>> beans = '48'
   >>> jelly
   52
   >>> beans
   '48'

You must assign a value to a variable before you use it! Otherwise, you will get
an error.

.. code-block:: python

   >>> jellybeans
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   NameError: name 'jellybeans' is not defined

Once *defined*, we can use these variables in place of our values.

   >>> temp1 = 30.7
   >>> temp2 = 29.7
   >>> average_temp = (temp1 + temp2) / 2
   >>> average_temp
   30.2
   >>> word1 = 'Hi, '
   >>> word1 + 'there!'
   'Hi, there!'

Syntax
^^^^^^

How does python know whether you are typing in a number, a string, or a
variable? Python, and other programming languages in general, infer this from
the way that you type them out---it assumes that you follow some rules, which
are the *syntax* of the langauge.


Numbers
  Starts with a digit (excluding zero, ``0``) or a period (``.``).
Strings
  Starts and end with single or triple quotation marks (``'``, ``"``, ``'''``,
  ``"""``). The starting and ending type of quotation mark must be the same.
Variable
  Starts with an alphabet, or an underscore. Thereafter, can include
  alphanumeric characters and underscores.

Here are some examples,

=========== ================ ================
Number      String           Variable
=========== ================ ================
``2345``    ``'juice'``      ``x``
``10``      ``"jam"``        ``Yellow``
``0.92810`` ``'''jerky'''``  ``fried_banana``
``3.45``    ``"""jekyll"""`` ``OwO``
=========== ================ ================

Editor
^^^^^^

The editor is a place that allows you to save the programs you have written.
Hereafter, programs in an editor are shown with line numbers, like so,

.. code-block:: python
    :linenos:

    print("This represents a program in the editor")

While the REPL is represented with no line numbers, and with the default prompt
``>>>``.

.. code-block:: python

    >>> print('This is in the REPL')
    This is in the REPL

Checkpoint
^^^^^^^^^^

By now, your program should look something like this:

.. literalinclude:: part1.py
    :language: python
    :linenos:

Part 2
------

You can download the helper library :download:`here <../../lib/basic_python3.py>`.

.. literalinclude:: part2.py
    :language: python
    :linenos:

Part 3
------
.. literalinclude:: part3.py
    :language: python
    :linenos:

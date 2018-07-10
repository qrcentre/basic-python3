Workshop Reference
==================

These are reference notes for the workshop.

Part 1
------
.. literalinclude:: part1.py
    :language: python
    :linenos:

Part 2
------

You can download the helper library :download:`here <../../lib/basic_python3.py>`.

Lists
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    >>> lst = [1,2,3]
    >>> lst2 = ["a","b","c"]
    >>> lst + lst2
    [1, 2, 3, 'a', 'b', 'c']
    >>> newlst = lst + lst2
    >>> newlst
    [1, 2, 3, 'a', 'b', 'c']
    >>> newlst[0]
    1
    >>> newlst[1:3]
    [2, 3]

For loops
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    >>> lst = [1,2,3,4]
    >>> x = 0
    >>> for i in lst:
    	x += i
    >>> x
    10

Conditionals (if, elif, else)
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    >>> x = 10
    >>> if x > 5:
    	print("haha")
    elif x < 5:
    	print("hehe")
    else:
    	print("hoho")

    haha
    >>> lst = [1,2,3,4,5]
    >>> for i in lst:
    	if i < 3:
    		print(i)

    1
    2

.. literalinclude:: part2.py
    :language: python
    :linenos:

Part 3
------
.. literalinclude:: part3.py
    :language: python
    :linenos:

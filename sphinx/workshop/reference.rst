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

Lists are structures that contain multiple values, and can contain numbers, strings and even other lists. 
Like strings, you can add lists together, and assign them to variables. 
You can also access an element of a list by using the *index* of the element. The first element has index 0. 

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

For loops
^^^^^^^^^^^^^^^^^^^^^

For loops enable us to loop over the elements in a list or string. 

.. code-block:: python

    >>> lst = [1,2,3,4]
    >>> x = 0
    >>> for i in lst:
    	x += i
    >>> x
    10
    >>> string = "hello"
    >>> newstring = ""
    >>> for char in string:
        newstring = char + newstring
    >>> newstring
    'olleh'

Conditionals (if, elif, else)
^^^^^^^^^^^^^^^^^^^^^

Using if, elif and else, we can impose conditions to control what our code does. "Elif" is short for "else if".
In the following example, the if statement checks if x > 5. If x is not > 5, then it will go into the elif statement to check if x < 5.
Finally, if none of the above conditions were satisfied, the code will execute what is specified by "else". 

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

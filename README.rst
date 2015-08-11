.. image:: https://travis-ci.org/GreatFruitOmsk/tailhead.svg?branch=master

======
tailhead
======

Python tail is a simple implementation of GNU tail and head. 

It provides 3 main functions that can be performed on any file-like object that supports ``seek()`` and ``tell()``.

* ``tail`` - read lines from the end of a file
* ``head`` - read lines from the top of a file
* ``follow`` - read lines as a file grows

It also comes with ``pytail``, a command line version offering the same functionality as GNU tail. This can be particularly useful on Windows systems that have no tail equivalent.

- `tailhead on GitHub <tailhead>`_
- `tailhead on Pypi <http://pypi.python.org/pypi/tailhead>`_

Installation
============

Install with ``pip`` or ``easy_install``.

::

    pip install tailhead

Examples
========

::

  import tailhead
  f = open('test.txt', 'w')
  for i in range(11):
      f.write('Line %d\\n' % (i + 1))
  f.close()
    
Tail
----
::

    # Get the last 3 lines of the file
    tailhead.tail(open('test.txt'), 3)
    # ['Line 9', 'Line 10', 'Line 11']

Head
----
::

    # Get the first 3 lines of the file
    tailhead.head(open('test.txt'), 3)
    # ['Line 1', 'Line 2', 'Line 3']

Follow
------
::

    # Follow the file as it grows
    for line in tailhead.follow_path('test.txt'):
        if line is not None:
            print(line)
        else:
            # sleep

Running Tests
=============

Tailer currently only has doctests.

Run tests with nose::

    nosetests --with-doctest tailhead

Run tests with doctest::

    python -m doctest -v tailhead/__init__.py

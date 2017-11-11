.. include:: abbreviation.txt

.. _user-guide-page:

============
 User Guide
============

Interval Construction
=====================

An interval can be constructed using a couple (inf, sup) or an object that support the *__getitem__*
interface

.. code-block:: py3

  Interval(inf, sup)
  Interval((inf, sup))
  Interval(iterable)
  Interval(interval)

To clone an interval use

.. code-block:: py3

  interval.copy()

Properties
==========

To get the interval boundaries use

.. code-block:: py3

  interval.inf
  interval.sup

An empty interval is defined with *inf* and *sup* set to :code:`None`.

Operations
==========

To compute the union of two intervals use

.. code-block:: py3

  i3 = i1 | i2
  i1 |= i2

To compute the intersection of two intervals use

.. code-block:: py3

  i3 = i1 & i2
  i1 &= i2

It returns an empty interval if the intersection is null.

To document

.. code-block:: py3

  interval[0]
  interval[1]

  interval1 < interval2
  interval1 > interval2

  interval += 1
  interval + 1

  interval -= 1
  interval - 1

  interval.enlarge(1)

  interval *= 2

  x in interval

  interval1.is_included_in(interval2)
  interval1.is_outside_of(interval2)
  interval1.map_in(interval2)
  interval1.map_x_in(x)
  interval1.unmap_x_in(x)

  interval.is_left_open
  interval.is_right_open

  interval.length
  interval.length_float
  interval.centre
  interval.slice

  interval.iter()

  ...

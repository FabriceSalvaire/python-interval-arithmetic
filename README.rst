This Python module implements interval arithmetic.

Interval Construction
=====================

An interval can be constructed using a couple (inf, sup) or an object that support the
:meth:`__getitem__` interface::

  Interval(inf, sup)
  Interval((inf, sup))
  Interval(iterable)
  Interval(interval)

To clone an interval use::

  interval.copy()

Properties
==========

To get the interval boundaries, use the :attr:`inf` and :attr:`sup` attribute::

  interval.inf
  interval.sup

An empty interval is defined with *inf* and *sup* set to :obj:`None`.

  interval.is_left_open
  interval.is_right_open
  interval.length
  interval.centre

Operations
==========

To compute the union of two intervals use::

  i3 = i1 | i2
  i1 |= i2

To compute the intersection of two intervals use::

  i3 = i1 & i2
  i1 &= i2

It returns an empty interval if the intersection is null.

.. End

###############################################################################
# Continuation lines

# Yes:
# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)


# More indentation included to distinguish this from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)
# Hanging indents should add a level.
foo = long_function_name(
	var_one, var_two,
    var_three, var_four)
# No:
# Arguments on first line forbidden when not using vertical alignment.
foo = long_function_name(var_one, var_two,
    var_three, var_four)


# Further indentation required as indentation is not distinguishable.
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)
# Acceptable:
# No extra indentation.
if (this_is_one_thing and
    that_is_another_thing):
    do_something()
# Add a comment, which will provide some distinction
# in editors supporting syntax highlighting.
if (this_is_one_thing and
    that_is_another_thing):
    # Since both conditions are true, we can do something.
    do_something()
# Add some extra indentation on the conditional continuation line.
if (this_is_one_thing
        and that_is_another_thing):
    do_something()

# Closing brackets (all acceptable)
my_list = [
    1, 2, 3,
    4, 5, 6,
    ]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
    )
my_list = [
    1, 2, 3,
    4, 5, 6,
]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)

###############################################################################
# Line split

with open('/path/to/some/file/you/want/to/read') as file_1, \
    open('/path/to/some/file/being/written', 'w') as file_2:
        file_2.write(file_1.read())


class Rectangle(Blob):
    def __init__(self, width, height,
                 color='black', emphasis=None, highlight=0):
        if (width == 0 and height == 0 and
                color == 'red' and emphasis == 'strong' or
                highlight > 100):
            raise ValueError("sorry, you lose")
        if width == 0 and height == 0 and (color == 'red' or
                                           emphasis is None):
            raise ValueError("I don't think so -- values are %s, %s" %
                             (width, height))
        Blob.__init__(self, width, height,
                      color, emphasis, highlight)

object.do_something().do_something_else()\
      .what_am_i_doing()

###############################################################################
# Imports

# Yes:
import os
import sys
from subprocess import Popen, PIPE
# No:
import sys, os
# Avoid:
from module import *

# imports order
import os

from rest_framework import serializers

from .models import Category, Tag, Article

###############################################################################
# Whitespace

# Yes:
spam(ham[1], {eggs: 2})
# No:
spam( ham[ 1 ], { eggs: 2 } )

# Yes:
if x == 4:
    print(x, y)
    x, y = y, x
# No:
if x == 4 :
    print(x , y)
    x , y = y , x

# Yes:
ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
ham[lower:upper], ham[lower:upper:], ham[lower::step]
ham[lower+offset:upper+offset]
ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
ham[lower + offset:upper + offset]
# No:
ham[lower + offset:upper + offset]
ham[1: 9], ham[1 :9], ham[1:9 :3]
ham[lower : : upper]
ham[ : upper]

# Yes:
spam(1)
dct['key'] = lst[index]
# No:
spam (1)
dct ['key'] = lst [index]

# Yes:
x = 1
y = 2
long_variable = 3
# No:
x             = 1
y             = 2
long_variable = 3

# Yes:
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)
# No:
i=i+1
submitted +=1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)


# No spaces around = in keyword arguments or default values
def complex(real, imag=0.0):
    return magic(r=real, i=imag)

# Yes:
if foo == 'blah':
    do_blah_thing()
do_one()
do_two()
do_three()
# Rather not:
if foo == 'blah': do_blah_thing()
do_one(); do_two(); do_three()

###############################################################################
# Comments

# No:
x = x + 1 #  Increment x
# Maybe:
x = x + 1  # Compensate for border

###############################################################################
# Recommendations

# Yes:
if foo is not None:
    pass
# No:
if not foo is None:
    pass


# Yes:
def f(x): return 2*x
# No:
f = lambda x: 2*x

# Yes:
try:
    value = collection[key]
except KeyError:
    return key_not_found(key)
else:
    return handle_value(value)
# No:
try:
    # Too broad!
    return handle_value(collection[key])
except KeyError:
    # Will also catch KeyError raised by handle_value()
    return key_not_found(key)

# Yes:
if foo.startswith('bar'):
    pass
# No:
if foo[:3] == 'bar':
    pass

# Yes:
if not seq:
    pass
if seq:
    pass
# No:
if len(seq):
    pass
if not len(seq):
    pass

# Yes:
if greeting:
    pass
# No:
if greeting == True:
    pass
# Worse:
if greeting is True:
    pass


###############################################################################
# Django

# use “action words” in docstrings
def foo():
    """
    Calculates something and returns the result.
    """
    pass


# Yes:
class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = 'people'


# No:
class Person(models.Model):
    class Meta:
        verbose_name_plural = 'people'
    FirstName = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=40)

# Yes:
# {{ foo }}
# No:
# {{foo}}


# Choices
class MyModel(models.Model):
    DIRECTION_UP = 'U'
    DIRECTION_DOWN = 'D'
    DIRECTION_CHOICES = (
        (DIRECTION_UP, 'Up'),
        (DIRECTION_DOWN, 'Down'),
    )

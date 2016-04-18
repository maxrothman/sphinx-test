"""This is a test module"""

def func(foo, bar):
  """Does a thing

  :param foo: A foo
  :type foo: str
  :param bar: a bar
  :type bar: int
  :returns: bool -- whether it worked
  :raises: AttributeError
  """
  return False

class ObjectThing(object):
  """This is a class thing.

  .. note::
    Things do stuff
  """

  def thing_doer(foo):
    """Does some stuff

    :param foo: a foo
    """
    pass

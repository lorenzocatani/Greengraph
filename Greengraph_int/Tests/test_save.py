from ..method2 import functionB
from nose.tools import assert_equal
from mock import Mock

def test_functionA():
  """ Test something"""
  # Test something
  #f = Mock(name="myroutine", return_value=2) 
  actual=functionB(2)
  expected=4
  assert_equal(expected,actual)
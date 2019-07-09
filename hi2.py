#!/usr/bin/env python

class MutableClass(object):
  def __init__(self, initial_a, initial_b):
    self.a = initial_a
    self.b = initial_b

  def stateful_add(self, x, y):
    result = self.a + self.b
    self.a = self.a * 2
    self.b = self.b * 2
    return result

def pure_add(a,b):
  return a + b

def main():
    print "pure_add(1,2): "
    print pure_add(1,2)
    print "pure_add(2,3): "
    print pure_add(2,3)
    print
    print

    instance_1 = MutableClass(1, 1)
    instance_2 = MutableClass(3, 3)
    instance_3 = MutableClass(10, 10)

    for i in xrange(3):
      print "instance_1.stateful_add(1,2): "
      print instance_1.stateful_add(1,2)

      print "intance_2.stateful_add(1,2): "
      print instance_2.stateful_add(1,2)

      print "intance_3.stateful_add(1,2): "
      print instance_3.stateful_add(1,2)

      print


if __name__ == '__main__':
    main()

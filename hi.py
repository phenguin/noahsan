
class MyClass(object):
    def __init__(self, x):
      self.state = x + 4

    def impure_add(self, a, b):
        return a + b + self.state

def pure_add(a, b):
    return a+b;

def main():
    print "pure_add(1,2): "
    print pure_add(1,2)
    print "pure_add(2,3): "
    print pure_add(2,3)
    print
    print

    instance_1 = MyClass(5)
    instance_2 = MyClass(2)
    instance_3 = MyClass(100)
    print "instance_1.impure_add(1,2): "
    print instance_1.impure_add(1,2)

    print "intance_2.impure_add(1,2): "
    print instance_2.impure_add(1,2)

    print "intance_3.impure_add(1,2): "
    print instance_3.impure_add(1,2)

if __name__ == '__main__':
    main()

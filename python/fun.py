x = 12
x=x+1
def g(x):
      x = x + 1
      def h(y):
          return x + y
      return h(6)
print g(x)
print x
# Python Numpy tutorial
# Python

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) / 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle +quicksort(right)

print quicksort([3,6,8,10,1,2,1])

# Basic data types
x = 3
print(type(x))
print x
print x + 1
print x - 1
print x * 2
print x ** 2
x += 1
print x
x *= 2
print x
y = 2.5
print type(y)
print y, y + 1, y * 2, y ** 2

t = True
f = False
print type(t)
print t and f 
print t or f 
print not t 
print t != f 

hello = 'hello'     # String literals can use single quotes
world = "world"     # or double quotes; it does not matter
print hello
print len(hello)
hw = hello + ' ' + world
print hw
hw12 = '%s %s %d' % (hello, world, 12)
print hw12

s = "hello"
print s.capitalize()
print s.upper()
print s.rjust(7)
print s.center(7)
print s.replace('l', '(ell)')
print '   world   '.strip()

# Containers 
xs = [3, 1, 2]          # A list is the Python equivalent of an array
print xs, xs[2]
print xs[-1]
xs[2] ='foo'
print xs
xs.append('bar')
print xs
x = xs.pop()
print x, xs

nums = range(5)
print nums
print nums[2:4]
print nums[2:]
print nums[:2]
print nums[:]
print nums[:-1]
nums[2:4] =[8,9]
print nums

animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print animal
for idx, animal in enumerate(animals):
    print '#%d: %s' % (idx + 1, animal)

nums = [0,1,2,3,4]
squares = []
for x in nums:
    squares.append(x ** 2)
print squares
squares = [x ** 2 for x in nums]
print squares
even_squares = [x ** 2 for x in nums if x % 2 == 0]
print even_squares

d = {'cat': 'cute', 'dog': 'furry'}
print d['cat']
print 'cat' in d
d['fish'] = 'wet'
print d['fish']
print d.get('monkey', 'N/A')
print d.get('fish', 'N/A')
del d['fish']
print d.get('fish', 'N/A')

d = {'spider': 2, 'cat': 8, 'person': 4}
for animal in d:
    legs = d[animal]
    print 'A %s has %d legs' % (animal, legs)
for animal, legs in d.iteritems():
    print 'A %s has %d legs' % (animal, legs)

nums = [0,1,2,3,4]
even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
print even_num_to_square

animals = {'cat', 'dog'}
print 'cat' in animals
print 'fish' in animals
animals.add('fish')
print 'fish' in animals
print len(animals)
animals.add('cat')
print len(animals)
animals.remove('cat')
print len(animals)

animals = {'cat', 'dog', 'fish'}
for idx, animal in enumerate(animals):
    print '#%d: %s' % (idx + 1, animal)
    
from math import sqrt
nums = {int(sqrt(x)) for x in range(30)}
print nums

d = {(x, x + 1): x for x in range(10)}
t = (5, 6)
print type(t)
print d[t]
print d[(1, 2)]
print d[(0, 1)]

# functions
def sign(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'
for x in [-1, 0, 1]:
    print sign(x)
    
def hello(name, loud = False):
    if loud:
        print 'HELLO, %s!' % name.upper()
    else:
        print 'Hello, %s' % name 
hello('Bob')
hello('Fred', loud=True)

#Classes
class Greeter(object):
    def __init__(self, name):
        self.name = name
    def greet(self, loud=False):
        if loud:
            print 'HELLO, %s!' % self.name.upper()
        else:
            print 'Hello, %s' % self.name
g = Greeter('Fred')
g.greet()
g.greet(loud=True)

# Numpy
# Arrays 
import numpy as np

a = np.array([1,2,3])
print type(a)
print a.shape
print a[0], a[1], a[2]
a[0] = 5
print a

b = np.array([[1,2,3],[4,5,6]])
print b.shape
print b[0,0], b[0,1], b[1,0]

a = np.zeros((2,2))
print a

b = np.ones((1,2))
print b 

c = np.full((2,2),7)
print c 

d = np.eye(2)
print d 

e = np.random.random((2,2))
print e

# Array indexing
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print a
b = a[:2,1:3]
print b
print a[0,1]
b[0,0] = 77
print a[0,1]

row_r1 = a[1,:]
row_r2 = a[1:2, :]
print row_r1, row_r1.shape
print row_r2, row_r2.shape

col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print col_r1, col_r1.shape
print col_r2, col_r2.shape

a = np.array([[1,2],[3,4],[5,6]])
print a[[0,1,2],[0,1,0]]
print np.array([a[0,0],a[1,1],a[2,0]])
print a[[0,0],[1,1]]
print np.array([a[0,1],a[0,1]])

a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print a 
b = np.array([0,2,0,1])
print a[np.arange(4),b]
a[np.arange(4),b] += 10
print a 

a = np.array([[1,2],[3,4],[5,6]])
bool_idx = (a > 2)
print bool_idx
print a[bool_idx]
print a[a>2]

# Data types
x = np.array([1,2])
print x.dtype
x = np.array([1.0,2.0])
print x.dtype
x = np.array([1,2], dtype = np.int64)
print x.dtype

# Array math
x = np.array([[1,2],[3,4]], dtype = np.float64)
y = np.array([[5,6],[7,8]], dtype = np.float64)
print x + y
print np.add(x,y)
print x - y
print np.subtract(x, y)
print x * y 
print np.multiply(x,y)
print x / y 
print np.divide(x,y)
print np.sqrt(x)

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
v = np.array([9,10])
w = np.array([11,12])
print v.dot(w)
print np.dot(v,w)
print x.dot(v)
print np.dot(x,v)
print x.dot(y)
print np.dot(x,y)

x = np.array([[1,2],[3,4]])
print np.sum(x)
print np.sum(x, axis = 0)
print np.sum(x, axis = 1)

x = np.array([[1,2],[3,4]])
print x 
print x.T
v = np.array([1,2,3])
print v 
print v.T

# Broadcasting
x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
v = np.array([1,0,1])
y = np.empty_like(x)

for i in range(4):
    y[i, :] = x[i, :] + v 
print y 

x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
v = np.array([1,0,1])
vv = np.tile(v, (4,1))
print vv
y = x + vv 
print y 

x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
v = np.array([1,0,1])
y = x + v 
print y

# some applications of broadcasting
v = np.array([1,2,3])
print v 
w = np.array([4,5])
print w 
print np.reshape(v, (3,1)) * w 
x = np.array([[1,2,3],[4,5,6]])
print x + v 
print ((x.T + w).T).T
print x + np.reshape(w, (2,1))
print x * 2

# SciPy
# Image operations
# from scipy.misc import imread, imsave, imresize
# img = imread('/Users/hjp/Downloads/hjp.jpg')
# img_tinted = img * [1, 0.95, 0.9]
# img_tinted = imresize(img_tinted, (300, 300))
# imsave('/Users/hjp/Downloads/hjp1.jpg', img_tinted)

# MATLAB files

# Distance between points
from scipy.spatial.distance import pdist, squareform
x = np.array([[0,1],[1,0],[2,0]])
print x
d = squareform(pdist(x, 'euclidean'))
print d 

# Matplotlib
# Plotting
import matplotlib.pyplot as plt
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)
plt.plot(x,y)
plt.show()

x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
y_tan = np.tan(x)
plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.plot(x, y_tan)
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('Sine and Cosine and Tan')
plt.legend(['Sine', 'Cosine', 'Tan'])
plt.show()

# Subplots
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.subplot(2,1,1)
plt.plot(x, y_sin)
plt.title('Sine')
plt.subplot(2,1,2)
plt.plot(x, y_cos)
plt.title('Cosine')
plt.show()

# Images
# from scipy.misc import imread, imresize
# img = imread('/Users/hjp/Downloads/hjp.jpg')
# img_tinted = img * [1, 0.95, 0.9]
# plt.subplot(1,2,1)
# plt.imshow(img)
# plt.subplot(1,2,2)
# plt.imshow(np.unit8(img_tinted))
# plt.show()







from fractions import Fraction
import math
import random
# List operations/methods
L = [123, 'spam', 1.23]
#print(L[0:-1])
#L.append('NI')
#print(L)
#L.pop(2)
#print(L)
#L.sort()
#print(L)
s= '1 2 3'
s.split()

print(L.index(123)) #Gives error if not found, use in try, catch
# Matrix/List comprehensions
M = [[1, 2, 3], [4, 5, 6], [7,8,9]] 
print([row[1] for row in M if row[1] % 2 == 0])
# Diagonal
print([M[i][i] for i in range( len(M) ) ])

# Generator
G = (sum(row) for row in M)
print(next(G))
print(next(G))

# Records
rec = {'name': {'first': 'Raj', 'last': 'Sekhon'}, 'job': 'student'}
print(rec['name']['first'])

# Set operations
X = set('gallahan')
Y = {'f','l','e','s','h','wound'}

print(X & Y) # Set intersection
print(X | Y) # Set union
print(X - Y) # Set difference
print(X > Y) # Superset
print(X < Y) # Subset
print(X ^ Y) # Symmetric Difference/XOR

print({n ** 2 for n in [1,2,3,4]}) # ** = exponentiation
print('f' in X, 'f' in Y)
print( 1.0 / 3.0)



#reduce(lambda parameter_list: expression)
#Fractions
f = Fraction(2,3)
print(f + 1)

#Types
print(type(L) == list) 
if isinstance(L, list): 
    print('yes')
# Type checking is not usually advised
# Limits polymorphism

# Classes
class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insertToFront(self, value):
        if self.head == None:
            self.head = Node(value) 
        else:
            newNode = Node(value)
            newNode.next = self.head
            self.head = newNode
    def list_print(self):
        node = self.head
        while node:
            print node.value
            node = node.next

LList = LinkedList()
for i in range(1,6):
    LList.insertToFront(i)
LList.list_print()

# Display 64 in octal, hex, binary
print('{0:o}, {1:x}, {2:b}'.format(64, 64, 64))
# Display 64 in octal/hex,
# Display 255 in hex, hex capitalized
print('%o, %x, %x, %X' % (64, 64, 255, 255))
#Compute sin, cos of 2pi
print(round(math.sin(2*math.pi)), round(math.cos(2*math.pi)))
#Random int 0 - 10
print(random.randint(0,10))
print(random.choice(['spam', 'eggs']))

#random.shuffle([]) => useful for swapping values randomly

#Fractions and using limit denominator
test_fr = Fraction(1,5)
test_fr += Fraction(*(2.0/5).as_integer_ratio())
print(test_fr)
print(test_fr.limit_denominator(5))

#To create a set
Set1 = set()
Set1.add('Hello')
# NOTE: SETS CAN ONLY CONTAIN IMMUTABLE OBJECTS
#       NO EMBEDDED LISTS/DICTS

# Set Comprehension
print({x ** 2 for x in [1,2,2]})
# ^ Outputs: set([1, 4])

# For list equality check, use set instead of sorting

# Python uses reference count garbage collection, has 
# built-in system to solve issue of cyclical references. (gc module)

# a and b reference the SAME object
a = 3
b = a
# a now references a DIFFERENT object
a = 'spam'

# Reset a
a = b
# Same as above, b /= 5
a += 2

# L1 L2 reference same object
L1 = [1, 2, 3]
L2 = L1

# NOTE: This changes BOTH L1 and L2, affect applies on mutable objects
L1[0] = 24

# To avoid, make a copy, only works for lists
L2 = L1[:]
# For other data structures use:
#    import copy 
#    L2 = copy.copy(L!)


# To avoid escapes use, r
#myfile = open(r'C:\new\text.dat', 'w')
#or 
#file = open('C:\\new\\text.dat', 'w')

S = 'spammy'
#Cut out m's to make the word spay
S = S[:3] + S[-1]
print(S) 

#To replace only one & first instance use
S = 'spammy'
firstM = S.find('m')
#Then modify from there
S = S[:firstM] + S[firstM + 1:]
print(S)

template = 'Hello {name}!'
stringF = template.format(name='World')
print(stringF)

# NOTE: List append/sort modify object in-place
# DO NOT assing list to ret value of these operations
# ex: L.sort() sorts L in-place returns None

L = [1, 2, 3]
#in-place reversal
L.reverse()
#returns reversed list w/out modifying L
L2 = list( reversed(L) )

# Push onto back
L.append(0)
L.append(-1)
# Pop off and return back
neg1 = L.pop()

print(L)
print(neg1)

# Insertion
L = [1,4,5]
L[1:1] = [2,3]
print(L)

# Replacement
L = [1,4,5]
L[1:3] = [2,3]
print(L)

# Deletion
L = [1,4,5]
L[1:3] = []
print(L)

# Dicts often used to implement sparse data structures
 
# Dict with tuple keys
Matrix = {}
Matrix[(0,0,0)] = 0
Matrix[0,0,4] = 1
# ...

# Error checking
#  Using if statement
if (0,0,0) in Matrix:
    print(Matrix[(0,0,0)])

#  Try catch block
try: 
    print(Matrix[(0,0,0)])
except KeyError:
    print(0)

#  Gets val or returns 0
Matrix.get((0,0,0), 0)

a = 1
b = 2
# Swap Values
a, b = b, a

# Changes only L
L = [1, 2]
M = L
L = L + [3,4]

# Changes both, bc += auto chooses in-place
L = [1, 2]
M = L
L += [3,4]

test = True
i = 0
while test:
    if i > 0: 
        break
    i += 1
else: 
    # This else only executes if the loop executes normally (no break)
    print('Hello')

# Files are their own iterators

# f = open('sample.py')
# iter(f) is f
#  True

# Lists/other built-ins are not, support multiple iterations

# Comprehensions


#  List Comprehensions make a new list, rather than in-place changes
#  Run at C language speed, so often faster than for loop

[x + y for x in 'spam' for y in 'eggs']


# Easy for loop question
# Write a for loop that prints the ascii code of each char in a string
s = "aaaa"
for char in s:
    print(ord(char))

# Print dict items in sorted order using a for loop
D = {4: 's', 3: 'p', 2: 'a', 1: 'm'}
for key in sorted(D):
    print(key)

# LEGB scoping lookup 
#   Local, Enclosures (ex: def), Global, Built-ins

# Closure example
def catString(s):
    def action(s2):
        return s2 + s
    return action

addSpam = catString('spam')

needLots = addSpam("I need lots of ")
print(needLots)


# Lambda version
def lamCatString(s):
    action = (lambda s2: s2 + s)
    return action

addSpam = lamCatString('spam!')

needLots = addSpam("I need lots of ")

print(needLots)


# Using function attributes
def attrCatString(s):
    def action(s2):
        return s2 + action.s1
    # Atributes not needed here, but illustrates concept
    action.s1 = s               
    return action

addSpam = attrCatString('spam!!!')

needLots = addSpam("I need lots of ")

print(needLots)


# Collects uncaught args
def printAsMany( *args):
    print(args)

printAsMany(1,2,3,4,5,6,7)

# Collects uncaught keyword args into dict
# NOTE: ** must go last
def printAsManyDict(**args):
    print(args)

printAsManyDict(a=1,b=2,c=3)


# Alternative use of * in call

def func(a,b,c,d):
    print( a + b + c + d)

args = (1,1,1,1)
func(*args)

# Example of using * in arg
def min1(first, *rest):
    for arg in rest:
        if arg < first:
            first = arg
        return first
def max1(first, *rest):
    for arg in rest:
        if arg > first:
            first = arg
        return first

def min2(*args):
    tmp = list(args)
    tmp.sort
    return tmp[0]

def max2(*args):
    tmp = list(args)
    tmp.sort(reverse=True)
    return tmp[0]

def min3(*args):
    res = args[0]
    for arg in args[1:]:
        if res > arg:
            res = arg
    return res
def max3(*args):
    res = args[0]
    for arg in args[1:]:
        if res < arg:
            res = arg
    return res

# Higher order programming example
def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res

def lessthanrel(x,y): return x < y

# Pass in test = lt operator
print(minmax(lessthanrel, 1,2,3,4))
# Pass in gt operator with lambda expr.
print(minmax(lambda x,y: x > y, 1,2,3,4)  )

# Sum recursively over nested list
def sumtree(L):
    tot = 0
    for x in L:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)
    return tot

L = [1, [2, [3, 4], 5], 6, [7, 8]]

print(sumtree(L))

# NOTE: The below implementations for DFS/BFS work on nested lists, 
#       They are not intended for objects which can be cyclic graphs
#
# Bredth-first 
def BFS(L, item):
    items = list(L) 
    while items:
        front = items.pop(0)
        if not isinstance(front, list): 
            if front == item:
                return True
        else: 
            items.extend(front) # Enque
    return False
print(BFS(L, 3))
print(BFS(L, 9))
# Depth-first

def DFS(L, item):
    items = list(L) 
    while items:
        front = items.pop(0)
        if not isinstance(front, list): 
            if front == item:
                return True
        else: 
            items[:0] = front   # Push onto front
    return False
print(DFS(L, 3))
print(DFS(L, 9))


# Uses closure concept to remember x
def action(x):
    return (lambda y: x + y)

act = action(100)
print(act(5))


# Lambda functions often used in callbacks, defer execution of handler
# until certain event occurs/not creatuin

# Python supports first class functions/objects

# Map function example
notSquared = [1, 2, 3]
Squared = map(lambda x: x ** 2, notSquared)
print(Squared)

# Filter using filter function example
notFiltered = [1,2,3,4,5]
oddFiltered = filter(lambda x: x % 2 == 0, notFiltered)
print(oddFiltered)

# Filter with list comp
print([x for x in notFiltered if x % 2 == 0])
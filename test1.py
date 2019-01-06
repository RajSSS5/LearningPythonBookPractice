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

# Matrix/List comprehensions
M = [[1, 2, 3], [4, 5, 6], [7,8,9]] 
print([row[1] for row in M if row[1] % 2 == 0])
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
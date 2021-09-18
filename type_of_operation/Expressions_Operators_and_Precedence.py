# test case
number1 = 123
number2 = -123
number3 = 12.3
number4 = -12.3
number5 = "abc"
number6 = '7f'
x = True
'''
Logical Operators
not unary negation
and conditional and
or conditional or
'''
if(number1 is not number2):
    print("{} is not same {}".format(number1, number2))
if(number1 == 123 and number2 == -123):
    print("{} is not same {}".format(number1, number2))
if(number1 == 123 or number2 == -123):
    print("{} is not same {}".format(number1, number2))

'''
Equality Operators:
is same identity
is not different identity
== equivalent
!= not equivalent
'''
'''
Comparison Operators
Data types may define a natural order via the following operators:
< less than
<= less than or equal to
> greater than
>= greater than or equal to
'''
'''
Arithmetic Operators
Python supports the following arithmetic operators:
+ addition
− subtraction
multiplication
/ true division
// integer division
% the modulo operator
'''
'''
Bitwise Operators
Python provides the following bitwise operators for integers:
∼ bitwise complement (prefix unary operator)
& bitwise and
| bitwise or
ˆ bitwise exclusive-or
<< shift bits left, filling in with zeros
>> shift bits right, filling in with sign bit
'''
'''
Sequence Operators:(str, tuple, and list)
s[j] element at index j
s[start:stop] slice including indices [start,stop)
s[start:stop:step] slice including indices start, start + step,
start + 2 * step, . . . , up to but not equalling or stop
s+t concatenation of sequences
k s shorthand for s + s + s + ... (k times)
val in s containment check
val not in s non-containment check
'''
'''
s == t equivalent (element by element)
s != t not equivalent
s < t lexicographically less than
s <= t lexicographically less than or equal to
s > t lexicographically greater than
s >= t lexicographically greater than or equal to
'''
'''
Operators for Sets and Dictionaries
Sets and frozensets support the following operators:
key in s containment check
key not in s non-containment check
s1 == s2 s1 is equivalent to s2
s1 != s2 s1 is not equivalent to s2
s1 <= s2 s1 is subset of s2
s1 < s2 s1 is proper subset of s2
s1 >= s2 s1 is superset of s2
s1 > s2 s1 is proper superset of s2
s1 | s2 the union of s1 and s2
s1 & s2 the intersection of s1 and s2
s1 − s2 the set of elements in s1 but not s2
s1 ˆ s2 the set of elements in precisely one of s1 or s2
'''
'''
For Dictionary:
d[key] value associated with given key
d[key] = value set (or reset) the value associated with given key
del d[key] remove key and its associated value from dictionary
key in d containment check
key not in d non-containment check
d1 == d2 d1 is equivalent to d2
d1 != d2 d1 is not equivalent to d2
'''
'''
alpha = [1, 2, 3]
beta = alpha # an alias for alpha
beta += [4, 5] # extends the original list with two more elements
beta = beta + [6, 7] # reassigns beta to a new list [1, 2, 3, 4, 5, 6, 7]
print(alpha) # will be [1, 2, 3, 4, 5]
'''
from itertools import permutations
a = [1,2,3,4]
p = permutations(a)
print(p)
print( p.__next__() )
print( p.__next__() )

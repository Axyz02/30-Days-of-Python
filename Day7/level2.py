# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

st1 = A.union(B)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
st2 = A.union(B)
st3 = B.union(A)
print(A.symmetric_difference(B))
del it_companies
del A
del B
del age
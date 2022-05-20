import pandas as pd

l1 = [1, 2, 3, 4, 5]
l2 = [9, 8, 7, 6, 5]

s1 = pd.Series(l1, index = ['0', '1', '2', '3', '4']).to_frame()
s1.columns = ['a']
s2 = pd.Series(l2, index = ['0', '1', '2', '3', '4']) 

print(s1)
print(s2)

s = pd.concat([s1, s2], axis = 1)

print(s)

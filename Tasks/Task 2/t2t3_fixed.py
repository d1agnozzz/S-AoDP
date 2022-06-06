import numpy as np 

m = np.random.randint(0, 1000, size=(5, 15))

def sort_diagonals_secondary(m):
    for j in range(1, len(m)):
        for i in range(0, len(m[0])):
            ti = i
            tj = j
            while tj > 0 and ti < len(m[0])-1 and m[tj][ti] < m[tj-1][ti+1]:
                m[tj][ti], m[tj-1][ti+1] = m[tj-1][ti+1], m[tj][ti]
                tj -= 1
                ti += 1

def sort_diagonals_main(m):
    for j in range(1, len(m)):
        for i in range(0, len(m[0])):
            ti = i
            tj = j
            while tj > 0 and ti > 0 and m[tj][ti] < m[tj-1][ti-1]:
                m[tj][ti], m[tj-1][ti-1] = m[tj-1][ti-1], m[tj][ti]
                tj -= 1
                ti -= 1

print(m)
print(len(m[0]))
sort_diagonals_secondary(m)
print(m)
sort_diagonals_main(m)
print()
print(m)

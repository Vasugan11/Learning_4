data_structure = [[1,2,3], {'a':4, 'b':5}, (6, {'cube':7, 'drum':8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

dstr = data_structure


dstr[0] = sum(dstr[0][0:])


dict_ = dstr[1]
k = []
v = []
for i in dict_:
    k.append(i)
    v.append(dict_[i])
dstr[1] = k + v
dstr[1][0] = len(dstr[1][0])
dstr[1][1] = len(dstr[1][1])
dstr[1] = sum(dstr[1][0:])


dstr[2] = list(dstr[2])
dict_1 = dstr[2][1]
s = []
t = []
for i in dict_1:
    s.append(i)
    t.append(dict_1[i])
dstr[2][1] = s + t
dstr[2][1][0] = len(dstr[2][1][0])
dstr[2][1][1] = len(dstr[2][1][1])
dstr[2][1] = sum(dstr[2][1][0:])
dstr[2] = sum(dstr[2][0:])


dstr[3] = len(dstr[3])


dstr[4] = list(dstr[4])
dstr[4] = dstr[4][1]
dstr[4] = dstr[4][0]
dstr[4] = list(dstr[4])
dstr[4] = dstr[4][0]
dstr[4] = list(dstr[4])
dstr[4][2] = list(dstr[4][2])
dstr[4][2][0] = len(dstr[4][2][0])
dstr[4][2] = sum(dstr[4][2][0:])
dstr[4][1] = len(dstr[4][1])
dstr[4] = sum(dstr[4][0:])


dstr = sum(dstr[0:])
print(dstr)
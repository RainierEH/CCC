j = str(input())
d = str(input())
m = int(input())

jl = []
js = []
dl = []

for char in j:
    if char != ' ':
        jl.append(int(char) - m)
        js.append(0)

for char in d:
    if char != ' ':
        dl.append(int(char))

for i in jl:
    if jl[i] < dl[i]:
        js[i] += 1

jtotal = 0
dtotal = 0

for i in js:
    if js[i] == 1:
        jtotal += jl[i]
    else:
        dtotal += 1

if jtotal > dtotal:
    print('YES')
else:
    print('NO')

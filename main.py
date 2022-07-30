import json
try:
    f = open("f.json","a+")
    b = json.load(f.read())
except:
    f = open("f.json","w")
    b = {}
while True:
    a = input(">>>")
    if not a:
        break
    for key, value in b.items():
        f = 0
        for d in key:
            for e in a:
                if a == d:
                    f += 1
        if f >= 0.8*len(key):
            print(b[a])
            break
    if f ==0:
        c = input("你输入的问题不存在，请输入你要的答案\a")
        if c:
            b[a] = c
        else:
            break
f.write(json.dumps(b))
f.close()

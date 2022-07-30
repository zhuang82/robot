import json
f = open("f.json","r+")
b = json.load(f.read())
while True:
    a = input(">>>")
    if a == "":
        break
    try:
        b[a]
    except:
        c = input("你输入的问题不存在，请输入你要的答案")
        b[a] = c
    else:
        print(b[a])
f.write(json.dump(b))
f.close()

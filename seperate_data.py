a = dict()
with open('./data1.csv','r',encoding='utf-8') as f:
    while r := f.readline():
        key = r.split(',')[0]
        if(a.get(key) != None):
            a[key].append(r)
        else:
            a[key] = [r]
    for key in a:
        with open("./tndata/data_"+key.split(' ')[0]+".csv",'w',encoding='utf-8') as document:
            document.writelines(a[key])
    
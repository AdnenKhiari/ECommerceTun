#mx = -1
import re
def clean_comma(d):
    return re.sub(r'/([0-9]),([0-9])(.*,.*TND)$/mug','\1\.\2\3',d)

    
with open('./data1.csv','r',encoding='utf-8') as f,open('./data1_all.csv','w',encoding='utf-8') as r:
    while(data := f.readline()):
        all = clean_comma(data).split(',')
        #mx = max(mx,len(all))
       # if(len(all) >= 8):
        #    new_data = ','.join(all)
        #    r.write(new_data)
        while(len(all) != 9):
            all.insert(len(all) - 2,'')
        r.write(','.join(all))
        
#print(mx)
import pandas as pd

path = r''
df = pd.read_excel(path)
lst = list(df.numbers)

def fill_box (lst):
    count = 0
    packs = []
    final =[]
    
    for i in range (len(lst)):
        if lst[i] == 0:
            continue

        if count + lst[i] <= 12:
            packs.append(lst[i])
            count += lst[i]
            lst[i] = 0
            #print (lst)
            #print (packs)
            if count + lst[i] == 12:
                count = 0
                #print (packs)
                final.append(packs)
                packs =[]
        elif count + lst[i] > 12:
            for j in range (i , len(lst)):
                if count + lst[j] == 12:
                    packs.append(lst[j])
                    count = 0
                    #print (packs)
                    final.append(packs)
                    packs =[]
                    lst[j] = 0
                    #print (lst)
                    packs.append(lst[i])
                    count = lst[i]
                    lst[i] = 0
    return final

def codding_list(packing):
    count = 0
    box =[]
    for i in range (len(packing)):
        count += 1
        if count % 2 == 1:
            code = [1 for j in range(len(packing[i]))]
            box.append(code)
        else:
            code = [0 for j in range(len(packing[i]))]
            box.append(code)
    return box

packing = fill_box(lst)
binary = codding_list(packing)

def flatten(l):
    return [item for sublist in l for item in sublist]

num = flatten(packing)
coded = flatten(binary)
col1 = 'Numbers'
col2 = 'Coded_List'
data = pd.DataFrame({col1:num,col2:coded})
data.to_excel('final.xlsx', sheet_name='sheet1', index=False)

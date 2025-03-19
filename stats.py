def num_of_words(str):
    lst = str.split()
    return len(lst)
    

def num_of_characters(str):
    dct = {}
    for char in str:
        if char.lower() in dct:
            dct[char.lower()] += 1
        else:
            dct[char.lower()] = 1
    
    return dct

def order_dct(dct):
    lst = []

    for key, value in dct.items():
        d = {}
        d[key] = value
        lst.append(d)
    
    lst.sort(key=lambda x: list(x.values())[0], reverse=True)  
    
    return lst
    

    



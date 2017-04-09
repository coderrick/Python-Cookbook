'''

'''

def unique_str(str):
    unq_map = {}
    for i in range(len(str)):
        unq_map[str[i]] = i
    
    print(unq_map)
    print(len(unq_map))
    print(len(str))

    if len(unq_map) != len(str):
        print('False')
        return 

    print('True')
    

unique_str('dog')

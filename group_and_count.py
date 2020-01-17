def group_and_count(collection):
    dictionary = {}
    for element in collection:
        date = element[0]
        number = element[1]  
        key = (date.year, date.month)
        if key in dictionary:        
            key_value = dictionary[key] + number
        else:
            key_value = number
        dictionary[key] = key_value
    return dictionary
            
        





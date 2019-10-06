def data(collection,name):
    new_data=[]
    for person in collection:
        if person['name'] == name:
           new_data.append(person)
    return new_data


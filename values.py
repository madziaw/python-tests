def values(collection,key):
  new_collection=[]
  for element in collection:
    if key in element:
      new_collection.append(element[key])
  return new_collection

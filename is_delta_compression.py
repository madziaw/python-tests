def is_delta_compression(collection):
   new_collection =[collection[0]]
   previous_element = collection[0]
   for element in collection[1:]:
      new_element = element - previous_element
      previous_element = element
      new_collection.append(new_element)
   return new_collection

def count_words(string):
   dictionary = {}
   new_string = string.replace(',','').replace('.','').lower()
   for element in new_string.split():
      if element in dictionary:
        dictionary[element] = dictionary[element] + 1  
      else:
        dictionary[element] = 1
   return dictionary

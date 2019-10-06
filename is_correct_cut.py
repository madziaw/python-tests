def is_correct_cut(string,number):
   collection = []
   part = ''
   for element in string:
      part = part + element
      if len(part) == number:
        collection.append(part)
        part = ''
   if len(part)!=0:
     collection.append(part)
   return collection

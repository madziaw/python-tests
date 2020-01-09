def group_up (collection, string):
   groups ={}
   for element in collection:
       name_group = element[string]
       if name_group not in groups:
           groups[name_group] = []
           groups[name_group].append(element)
       else:
           groups[name_group].append(element)
   return groups




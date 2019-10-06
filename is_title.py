def is_title(string):
   words = string.split(' ')
   new_words = []
   for word in words:
      new_word = word[0].upper() + word[1:].lower()
      new_words.append(new_word)
   return ' '.join(new_words)

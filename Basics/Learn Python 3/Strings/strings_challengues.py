#CHALLENGUE 1
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):
  uniques = 0
  for letter in letters:
    if letter in word:
      uniques += 1
  return uniques

#print(unique_english_letters("mississippi"))
#print(unique_english_letters("Apple"))

#CHALLENGUE 2 y 3
def count_char_x(word,x):
  if x in word:
    return word.count(x)

#print(count_char_x("mississippi", "s"))
#print(count_char_x("mississippi", "m"))
#print(count_multi_char_x("mississippi", "iss"))
#print(count_multi_char_x("apple", "pp"))

#CHALLENGUE 4
def substring_between_letters(word, start, end):
  start_ind = word.find(start)
  end_ind = word.find(end)
  if start_ind > -1 and end_ind > -1:
    return word[start_ind + 1:end_ind]
  return word

#rint(substring_between_letters("apple", "p", "e"))
#rint(substring_between_letters("apple", "p", "c"))

#CHALLENGUE 5
# Write your x_length_words function here:
def x_length_words(sentence, x):
  words = sentence.split(" ")
  for word in words:
      if len(word) < x:
          return False
      else: return True
  return
#print(x_length_words("i like apples", 2))
#print(x_length_words("he likes apples", 2))

#CHALLENGUE ADVANCED 1
def check_for_name(sentence,name):
  return name.lower() in sentence.lower()

#print(check_for_name("My name is Jamie", "Jamie"))
#print(check_for_name("My name is jamie", "Jamie"))
#print(check_for_name("My name is Samantha", "Jamie"))

#CHALLENGUE ADVANCED 2
def every_other_letter(word):
  every_other = ""
  for i in range(0, len(word), 2):
    every_other += word[i]
  return every_other

#print(every_other_letter("Codecademy"))
#print(every_other_letter("Hello world!"))
#print(every_other_letter(""))

#CHALLENGUE ADVANCED 3
def reverse_string(word):
  reversed_string = ""
  for i in range(len(word)-1, -1, -1):
    reversed_string += word[i]
  return reversed_string 

#print(reverse_string("Codecademy"))
#print(reverse_string("Hello world!"))
#print(reverse_string(""))

#CHALLENGUE ADVANCED 4
def make_spoonerism(word1,word2):
  return  word2[0]+word1[1:] + " " + word1[0]+word2[1:]

#print(make_spoonerism("Codecademy", "Learn"))
#print(make_spoonerism("Hello", "world!"))
#print(make_spoonerism("a", "b"))

#CHALLENGUE ADVANCED 5
def add_exclamation(word):
  while(len(word) < 20):
    word += "!"
  return word

#print(add_exclamation("Codecademy"))
#print(add_exclamation("Codecademy is the best place to learn"))


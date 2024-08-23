#CHALLENGUE 1
my_dictionary = {
    1:2,2:5,3:9,4:3
}
def sum_values(dict):
    sum = 0
    for values in dict.values():
        sum += values
    return sum

#print(sum_values(my_dictionary))

#CHALLENGUE 2
def sum_even_keys(my_dictionary):
  total = 0
  for key in my_dictionary.keys():
    if key%2 == 0:
      total += my_dictionary[key]
  return total

#print(sum_even_keys({1:5, 2:2, 3:3}))
#print(sum_even_keys({10:1, 100:2, 1000:3}))

#CHALLENGUE 3
def add_ten(my_dictionary):
  for key in my_dictionary.keys():
    my_dictionary[key] += 10
  return my_dictionary

#print(add_ten(my_dictionary))

#CHALLENGUE 4
def add_ten(my_dictionary):
  for key in my_dictionary.keys():
    my_dictionary[key] += 10
  return my_dictionary

#print(add_ten({1:5, 2:2, 3:3}))
#print(add_ten({10:1, 100:2, 1000:3}))

#CHALLENGUE 5
def values_that_are_keys(my_dictionary):
  value_keys = []
  for value in my_dictionary.values():
    if value in my_dictionary:
      value_keys.append(value)
  return value_keys


#CHALLENGUE 6
def max_key(my_dictionary):
    largest_key = float("-inf")
    largest_value = float("-inf")
    for key, value in my_dictionary:
        if value > largest_value:
            largest_value = value
            largest_key = key
    return largest_key
    

print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"

#CHALLENGUE 7
# Write your word_length_dictionary function here:
def word_length_dictionary(words):
  word_lengths = {}
  for word in words:
    word_lengths[word] = len(word)
  return word_lengths
# Uncomment these function calls to test your  function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}

#CHALLENGUE 8
# Write your frequency_dictionary function here:
def frequency_dictionary(words):
  freqs = {}
  for word in words:
    if word not in freqs:
      freqs[word] = 0
    freqs[word] += 1
  return freqs
# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}

#CHALLENGUE 9
# Write your unique_values function here:
def unique_values(my_dictionary):
  seen_values = []
  for value in my_dictionary.values():
    if value not in seen_values:
      seen_values.append(value)
  return len(seen_values)
# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1

#CHALLENGUE 10
# Write your count_first_letter function here:
def count_first_letter(names):
  letters = {}
  for key in names:
    first_letter = key[0]
    if first_letter not in letters:
      letters[first_letter] = 0
    letters[first_letter] += len(names[key])
  return letters
# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}

def letter_check(word,letter):
    for character in word:
        if character == letter:
            return True
        elif (character == word[-1]) and character != letter:
            return False
        
#print(letter_check("fresa","a"))
        
def common_letters(string_one,string_two):
    new_list = []
    for i in string_one:
        for j in string_two:
            if i == j:
                if i in new_list:
                    continue
                else:
                    new_list.append(i)
    return(new_list)
                      
#print(common_letters('manhattan', 'san francisco'))
        
        
        
def username_generator(first_name,last_name):
  first_part = ""
  second_part = ""
  user_name = ""
  if len(first_name) <= 3:
    first_part = first_name
  else: first_part = first_name[:3]

  if len(last_name) <= 3:
    second_part = last_name
  else: second_part = last_name[:4]
  user_name = first_part + second_part
  
  return user_name

#print(username_generator("Abe","Simpson"))

#Coge una palabra y le pone la última letra delante
def password_generator(user_name):
    password = ""
    password = user_name[-1] + user_name[:len(user_name) - 1]
    return password
    

#print(password_generator("Jorge"))


authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"


author_names = authors.split(",")
#print(author_names)

author_last_names = []
for name in author_names:
  author_last_names.append(name.split()[-1])

#print(author_last_names)
 
#---------------------Strings Review--------------------------------#
#---------------------Strings Review--------------------------------#
#---------------------Strings Review--------------------------------#

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

#print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(',')
#print(highlighted_poems_list)

highlighted_poems_stripped = []
for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip())

#print(highlighted_poems_stripped)

highlighted_poems_details = []
for poem in highlighted_poems_stripped:
  highlighted_poems_details.append(poem.split(":"))

print(highlighted_poems_details)

titles = []
poets = []
dates = []


for poem in highlighted_poems_details:
  i = 0
  while i <= 2:
    if i == 0:
      titles.append(poem[i])
    elif i == 1:
      poets.append(poem[i])
    elif i == 2:
      dates.append(poem[i])
    i += 1


print(titles)
print()
print(poets)
print()
print(dates)
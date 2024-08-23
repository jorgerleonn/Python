#CHALLENGUE 1
def tenth_power(num):
    return num**10

#CHALLENGUE 2
def square_root(num):
    return num**(1/2)

#CHALLENGUE 3
def win_percentage(wins,losses):
    total_games = wins + losses
    ratio_won = wins / total_games
    return ratio_won * 100

#CHALLENGUE 4
def average(num1,num2):
    return (num1 + num2)/2

#CHALLENGUE 5 (% devuelve el resto)
def remainder(num1,num2):
    return (num1 * 2) % (num2 / 2)

#functiones CHALLENGUES ADVANCED
#CHALLENGUE 1
def first_three_multiples(num):
    print(num)
    print(num*2)
    print(num*3)
    return num*3

#CHALLENGUE 2
def tip(total,percentage):
    return (total*percentage)/100

#CHALLENGUE 3
def introduction(first_name,last_name):
    return (str(last_name) + ", " + str(first_name) + " " + str(last_name))

#CHALLENGUE 4
def dog_years(name,age):
    return name + ", you are " + str(age * 7) + " years old in dog years"

#CHALLENGUE 5
def lost_of_math(a, b, c, d):
    first = a + b
    second = c - d
    third = first * second
    fourth = third % a
    print(first)
    print(second)
    print(third)
    return fourth



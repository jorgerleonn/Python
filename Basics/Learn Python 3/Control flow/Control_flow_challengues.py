#CHALLENGUE 1
def large_power(base,exponent):
    if base**exponent > 5000:
        return True
    else: return False
    
#CHALLENGUE 2
def over_budget(budget,food_bill,electricity_bill,internet_bill,rent):
    if budget < (food_bill + electricity_bill + internet_bill + rent):
        return True
    else: return False

over_budget(10,5,6,7,7)

#CHALLENGUE 3
def twice_as_large(num1,num2):
    if num1 > num2*2:
        return True
    else: return False

#CHALLENGUE 4
def divisible_by_ten(num):
    if num %10 == 0:
        return True
    else: return False

#CHALLENGUE 5
def not_sum_to_ten(num1,num2):
    if num1 + num2 != 10:
        return True
    else: return False
    
#CONTROL FLOW CHALLENGUES ADVANCED
#CHALLENGUE 1
def in_range(num,lower,upper):
    if (num >= lower) and (num <= upper):
        return True
    else: return False
    
#CHALLENGUE 2
def same_name(your_name,my_name):
    if your_name == my_name:
        return True
    else: return False

#CHALLENGUE 3
def always_false(num):
    if num == 0:
        return False
    else: return False

#CHALLENGUE 4
def movie_review(rating):
    if rating <= 5:
        return ("Avoid at all costs!")
    elif (rating > 5) and (rating < 9):
        return("This one was fun.")
    elif (rating >= 9):
        return("Outstanding!")
    else: return False
    
#CHALLENGUE 5
def max_num(num1,num2,num3):
    if (num1 == num2) or (num1 == num3) or (num2 == num3):
        return("It's a tie!")
    else: return max(num1,num2,num3)
    
    









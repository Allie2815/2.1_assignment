# DSC 510
# Week 2
# Programming Assignment Week 2
# Author Allie Dunkel
# 12/9/2022

# Change#: 1
# Change(s) Made: Added lines 15-28 following assignment 2.1
# Date of Change: 12/9/2022

# This will get the users name
name = input('What is your name? ')
# This will display a welcome message using the users name
print('Welcome ' + name)
# This will get the users companies name
company_name = input('What is your companies name? ')
# This will get the amount of optic cable the company, and I changed the data type to an integer, so I can multiply
# it on line 16
cable_amount = int(input('How much fiber optic cable will you need (in feet)? '))
# This will calculate the total cost
total_cost = cable_amount * 0.87
# This will print the recipe using all the info from above, I need to change the previous numbers to strings because
# you cannot concatenate a string and an integer
print('The company, ' + company_name + ', will need ' + str(cable_amount) + ' feet of fiber optic cable. The total cost will be ' + str(total_cost) + ' dollars.')

# DSC 510
# Week 3
# Programming Assignment Week 3
# Author Allie Dunkel
# 12/17/2022

# Change#: 2 Change(s) Made: Added lines 26-62 following assignment 3.1 - changed the format to match the assignment
# and make more readable and added the if and elif statements
# Date of Change: 12/17/2022

# This will get the users name
name = input('What is your name? ')
# This will display a welcome message using the users name
print('Welcome ' + name)
# This will get the users companies name
company_name = input('What is your companies name? ')
# This will get the amount of optic cable the company, and I changed the data type to an integer, so I can multiply
# it on line 16
cable_amount = int(input('How much fiber optic cable will you need (in feet)? '))
# This will figure out how much to charge them based on the amount of cable they need. I needed to start with the highest number because the program goes in order
if cable_amount > 500:
    discount_cost3 = cable_amount * 0.50
    print('The company, ' + company_name + ', will need ' + str(
        cable_amount) + ' feet of fiber optic cable. The total cost will be ' + str(discount_cost3) + ' dollars.')
elif cable_amount > 250:
    discount_cost2 = cable_amount * 0.70
    print('The company, ' + company_name + ', will need ' + str(
        cable_amount) + ' feet of fiber optic cable. The total cost will be ' + str(discount_cost2) + ' dollars.')
elif cable_amount > 100:
    discount_cost1 = cable_amount * 0.80
    print('The company, ' + company_name + ', will need ' + str(
        cable_amount) + ' feet of fiber optic cable. The total cost will be ' + str(discount_cost1) + ' dollars.')
elif cable_amount <= 100:
    regular_cost = cable_amount * 0.87
    print('The company, ' + company_name + ', will need ' + str(
        cable_amount) + ' feet of fiber optic cable. The total cost will be ' + str(regular_cost) + ' dollars.')
# I think there is an easier and condensed way to do this, but I am not sure how


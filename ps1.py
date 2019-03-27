#MIT6_00SCS11_ps1.pdf

# Paying Off Credit Card Debt

# get the balance from the user
print("Please enter the balance (as a float!): ")
balance = input()
print("")
print("the balance is " + balance)

# Minimum monthly payment = Minimum monthly payment rate x Balance
# to be split into interest paid and principal paid
# variable = mmp, a float which needs to be converted to a str to print out. 

mmpr = 0.02	# 1.5%
mmp = mmpr*float(balance)

print("the minimum monthly payment rate is ")
print(mmpr)
print("the minimum monthly payment is ")
print(mmp)

# annual interest rate. to be used for interest paid
a_i_r = 0.18	# to be a percentage, so 0.18. 

# interest paid = Annual interest rate / 12 months x Balance
#i_p = (a_i_r)/(12.0)*(balance) # error with this equation: TypeError: can't multiply sequence by non-int of type 'float'
i_p = ((a_i_r)/(12.0))*(float(balance))
#i_p = (float(a_i_r)) # don't need to float() this guy as its already a float!

print("The interest paid is: ")
print(i_p)

# if we use a balance of 5000.0, then the interest paid is 75.0 just like the
# example. Principal paid is mmp - i_p
p_p = float(mmp) - i_p
print("The Principal paid is: ")
print(p_p)

# remaining balance = balance - principal paid
r_b = float(balance) - p_p
print("the remaining balance is ")
print(r_b)


# so here we need to start implementing the logic for the actual problem.
# we need to find the balance after a year. we need to follow the following outline
# retrieve user input
# initialize some state variables. remember monthly i_r from annual i_r as input
# for each month:
    # compute the new balance.
print("The balance for each month is as below: ")
for i in range(1, 12):
    print("Month " + str(i) + ":" + str(r_b))
    r_b = float(r_b)
    r_b = r_b-p_p   #ok so, this isnt correct, BUT it shows how we can iterate over the range, and decrease the balance by SOME value each "month"!

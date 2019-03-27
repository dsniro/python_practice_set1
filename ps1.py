#MIT6_00SCS11_ps1.pdf
import time
start = time.time()
"the code you want to test stays here"

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
    print("Month " + str(i) + ":     " + str(round(r_b, 2)))
    r_b = float(r_b)
    r_b = r_b-p_p   #ok so, this isnt correct, BUT it shows how we can iterate over the range, and decrease the balance by SOME value each "month"!

    mmp = mmpr*float(r_b)
    print("the new minimum monthly payment is ")
    print(round(mmp, 2)) #ok so I think this part is correct. 
    
    i_p = ((a_i_r)/(12.0))*(float(r_b))
    print("The new interest paid is: ")
    print(round(i_p, 2))

    p_p = float(mmp) - i_p
    print("The new Principal paid is: ")
    print(round(p_p, 2))

    #r_b = float(balance) - p_p
    print("the remaining balance is ")
    print(round(r_b, 2))

    #print("")
    print("")
print("Pretty depressing!")
print("")
print("note to self: Still need to output total amount paid")
print("")
print("")
print("")
# I think the idea here is that I can basically take all those equations,
# pass in the current value, calculate it, and update it
# constants will be minimum monthly payment rate, mmpr = 0.02

# the key will be to have balance be updated into a new_balance.
# using new_balance, we can calculate the rates again, and then move down the list
# of other operations to do.
# lets start with the first month. we know the new balance will be 4975
# btw, we already have this stored as r_b (remaining balance)

### several minutes later ( this whole problem only took me about an hour total (minus breaks and other interruptions)

# so at this point, I went back into the for loop, updated it to include each
# value being recalculated and now it appears to be working??
# might need to go in, manually, and see that each one is being calculated correctly.
# also, need to round out the numbers.
# but hey....look at that!
end = time.time()
print("Executed in: ")
print(end - start)
print( "seconds")
print("Brought to you by Derek Niro")

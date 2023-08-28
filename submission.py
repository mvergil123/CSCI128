# Gold mine program
import os


gold_mine_name = input("Hello, please type the name of the gold mine: ")

# development costs
total_development_cost = 145230000 + 36200000 + 209500000 + 80700000 + 48100000 + 28200000

# Operating Costs
excavation_cost = 9 * 1000000

processing_cost = 10 * 1000000

employee_cost = 100000 * 150

extra_cost = 100000000

total_operating_costs = excavation_cost + processing_cost + employee_cost + extra_cost

# calculating the exact amount of pure gold retrieved in grams 

gold_retrieved = 11000000

total_gold = gold_retrieved * .95

gold_in_ounces = total_gold / 28.35

expected_gold_price = int(input("Please input the expected gold price per ounce (oz): "))

# rehabilitation cost 
rehabilitation_cost = 150000000

# total revenue
total_revenue = gold_in_ounces * expected_gold_price

# yearly profit
yearly_profit = total_revenue - total_operating_costs


os.system('clear')

# total profit
total_profit = (yearly_profit * 20) - total_development_cost - rehabilitation_cost

# in the future
future_gold_price = expected_gold_price * .65

future_revenue  = gold_in_ounces * future_gold_price

future_yearly_profit = future_revenue - total_operating_costs

future_total_profit = (future_yearly_profit * 20) - total_development_cost - rehabilitation_cost

#potential profit
potential_profit = total_profit + future_total_profit

# output

print("OUTPUT Investment Planning Report of " +gold_mine_name+  " Mine in Colorado Springs")

print(" ")

print("OUTPUT The yearly profit is: " +str(yearly_profit))

print(" ")

print("OUTPUT The total profit is: " +str(total_profit))

print(" ")

print("OUTPUT The potential profit after 40 years is: " +str(potential_profit))

print(" ")

print("Have a good day!")

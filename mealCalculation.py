# Write a function to calculate total w/ 3 parameters:
# A meal cost, tax rate, tip rate. Calculate tip and tax then give total.

# Write a function to calculate total w/ 3 parameters:
# A meal cost, tax rate, tip rate. Calculate tip and tax then give total.

def calculate_total(meal_cost, tax_rate, tip_rate):
    tax = meal_cost * tax_rate
    tip = meal_cost * tip_rate
    total = meal_cost + tax + tip
    return total  # Returning total cost

def main():
    meal_cost = 53.48
    tax_rate = 0.07
    tip_rate = 0.18

    total_cost = calculate_total(meal_cost, tax_rate, tip_rate)
    print("Total cost including tax and tip:", round(total_cost, 2))

# Call main function
main()

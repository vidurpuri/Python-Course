num_of_people = int(input('Enter number people sharing rent: '))
total_rent = int(input('Enter total rent: '))
food_Ordered = int(input('Enter total food ordered for snacking in month: '))
electricity_units = int(input('Total no. of electricity units spend: '))
charge_per_unit = int(input('Enter charge per electricity unit: '))

total_charge_per_units_spend = electricity_units * charge_per_unit

total_expenditure = (total_rent + food_Ordered + total_charge_per_units_spend) / num_of_people

print(f'Each has to pay: {total_expenditure}')
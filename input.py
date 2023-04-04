from functions import convert_to_cad

# Prompt the user to enter the amount to convert
amount = float(input("Enter the amount to convert to CAD: "))

# Call the convert_to_cad function with the user input amount
results = convert_to_cad(amount)

# Display the results
for currency, value in results.items():
    print(f"{amount:.2f} {currency} is equal to {value:.2f} CAD")

from forex_python.converter import CurrencyRates

def convert_to_cad(amount):
    # Create an instance of the CurrencyRates class
    c = CurrencyRates()

    # Convert from USD to CAD
    usd_to_cad = c.convert('USD', 'CAD', amount)

    # Convert from EURO to CAD
    euro_to_cad = c.convert('EUR', 'CAD', amount)

    # Convert from GBP to CAD
    gbp_to_cad = c.convert('GBP', 'CAD', amount)

    # Convert from RUPEE to CAD
    rupee_to_cad = c.convert('INR', 'CAD', amount)

    # Return the results as a dictionary
    return {
        'USD': usd_to_cad,
        'EURO': euro_to_cad,
        'GBP': gbp_to_cad,
        'RUPEE': rupee_to_cad
    }

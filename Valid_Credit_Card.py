
import re

def validate_credit_card(card_number):
    """
    Validate a credit card number and return the card company.

    Args:
        card_number (str): The credit card number to validate.

    Returns:
        str: The card company if the number is valid, otherwise None.
    """

    # Define regular expression patterns for each card company
    patterns = {
        'MasterCard': r'^5[1-5][0-9]{14}$',
        'Visa': r'^4[0-9]{12}(?:[0-9]{3})?$',
        'American Express': r'^3[47][0-9]{13}$',
        'Diners Club': r'^3(?:0[0-5]|[68][0-9])[0-9]{11}$',
        'Discover': r'^6(?:011|5[0-9][0-9])[0-9]{12}$',
        'EnRoute': r"^2014\d{11}$|^2149\d{11}$",
        'JCB': r'^(?:2131|1800|35\d{3})\d{11}$',
        'Voyager': r'^8699[0-9]{11}$',
        'HiperCard': r"^38\d{11,16}$|^60\d{11,16}$",
        'Aura': r"^50\d{14}$"
    }

    # Iterate over the patterns and check if the card number matches
    for company, pattern in patterns.items():
        if re.match(pattern, card_number):
            check = company
            break
        else:
        # If no match is found, return None
            check = "Cartão invalido ou não aceito."
    print(check)
    pass

if __name__ == "__main__":
    card_number = input("Digite o número do cartão de crédito: ")
    validate_credit_card(card_number.replace(" ", ""))

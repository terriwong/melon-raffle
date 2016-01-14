from random import choice
from customer_info import organize_customer_data


def pick_winner(customers):
    """Choose a random winner from list of customers."""

    chosen_customer = choice(customers.keys())

    print "Contact {} at {} to notify them they've won".format(
        chosen_customer,
        customers[chosen_customer]["email"]
        )


customers = organize_customer_data("customers.txt")

pick_winner(customers)

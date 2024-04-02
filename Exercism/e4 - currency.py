def exchange_money(budget: float, exchange_rate: float):
    return budget / exchange_rate



print(exchange_money(127.5,1.2))

def get_change(budget: float, exchanging_value: float):
    return budget - exchanging_value
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

print(get_change(127.5,120))


def get_value_of_bills(denomination, number_of_bills):
    return denomination * number_of_bills
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """
print(get_value_of_bills(5,128))


def get_number_of_bills(amount: float, denomination: int):
    float = amount / denomination
    return int(float)
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """

print(get_number_of_bills(127.5 , 5))


def get_leftover_of_bills(amount: float, denomination: int):
    return amount % denomination
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """
print(get_leftover_of_bills(127.5, 20))


def exchangeable_value(budget: float, exchange_rate: float, spread: int, denomination:int):
    planning_to_exchange =  budget / exchange_rate 
    exchange_spread = exchange_rate * spread
    spread_value =  exchange_spread / 100
    return exchange_spread + exchange_rate

    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
print(exchangeable_value(127.25, 1.20, 10, 20))
"""
The change-making problem involves finding the minimum number of coins
from a set of denominations that add up to a given amount of money.

The change-making problem involves finding the minimum number of coins
from a set of denominations that add up to a given amount of money.
"""


def make_change(target_amount):
    change_list = []
    coin_count = 0
    denomination = [200, 100, 50, 20, 10, 5, 2, 1]  # order is important
    for d in denomination:
        # use the current coin until its value is too large
        while target_amount >= d:
            target_amount -= d  # decrease the remaining amount
            change_list.append(d)  # MAke a note of which coin was used
            coin_count += 1  # increase the coin count
    return coin_count, change_list


print(make_change(24))  # 20p + 2p + 2p
print(make_change(163))  # 1 + 50p + 10p + 2p + 1p

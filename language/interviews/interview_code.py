# 5 Kadane's algorithms
# def find_max_streak(votes):
#     """
#     INPUT:
#         votes: A python list of negative and positive numbers
#     OUTPUT:
#         sum: The total sum of the maximum subarray (highest vote count streak)
#     """
#     # Track the current subarray,
#     # starting with just the first value
#     cur_sub = votes[0]
#     # Track the current maximum sum
#     # Starting with the first value
#     max_sum = votes[0]
#
#     # Loop through elements in votes array
#     # Starting at index 1, since variables above already at index 0
#     for vote_value in votes[1:]:
#         # Choose either your current subarray with the added vote value,
#         # or just the added vote value, whichever is greater
#         cur_sub = max(vote_value, cur_sub + vote_value)
#
#         # The maximum
#         max_sum = max(max_sum, cur_sub)
#
#     return max_sum
#
#
# # greedy algorithm approach
# def find_profit(food_prices):
#     """
#     INPUT:
#         food_prices : Python List of integer food prices per day
#     OUTPUT:
#         max_profit: An integer which shows the max profit possible.
#                     This should be a zero if
#     """
#
#     # Check length
#     if len(food_prices) < 2:
#         return 0 # need at least two prices!
#
#     # Start minimum price marker at first price
#     min_food_price = food_prices[0]
#
#     # Start off with an initial max profit
#     max_profit = 0
#
#     # Skip the first index of 0
#     for price in food_prices[1:]:
#         # NOTE THE REORDERING HERE DUE TO THE NEGATIVE-PROFIT TRACKING
#
#         # Check the current price against our minimum for a profit
#         # comparison against the max_profit
#         comparison_profit = price - min_food_price
#
#         # Compare against our max_profit so far
#         max_profit = max(max_profit, comparison_profit)
#
#         # Check to set the lowest stock price so far
#         min_food_price = min(min_food_price, price)
#
#     return max_profit
#

# def find_profit(prices):
#     """
#     INPUT:
#         food_prices: Python List of historical prices
#     OUTPUT:
#         max_profit: Max profit possible
#     """
#     # Start with a zero-max profit
#     max_profit = 0
#     # Use i to track position in price array
#     # We start at index 1 (in order to calculate a profit Day 1 - Day 0)
#     i = 1
#     # Iterate through an entire array
#     while i < len(prices):
#         # Check to see if there is a profit to be made
#         # Between Day i and Day i-1
#         if prices[i] > prices[i - 1]:
#             # If there is a profit to be made
#             # Log the profit
#             max_profit += prices[i] - prices[i - 1]
#         i += 1
#     return max_profit
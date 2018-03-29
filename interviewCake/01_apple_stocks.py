# get the stock price of apple stocks from an array
# find the highest buy/sell price


stockPricesFromYesterday = [10, 7, 5, 8, 11, 9]


def max_profit_bruteforce(stockPricesFromYesterday):
    max_profit = 0
    earlier_price = 0
    for outer_time in stockPricesFromYesterday:
            for inner_time in stockPricesFromYesterday:

                earlier_time = min(outer_time, inner_time)
                later_time = max(outer_time, inner_time)

                earlier_price = earlier_time
                later_price = later_time

                # print("earlier time : " + str(earlier_time))
                # print("later time : " + str(later_time))
                # print("earlier price : " + str(earlier_price))
                # print("later price : " + str(earlier_price))


                potential_profit = later_price - earlier_price
                max_profit = max(max_profit, potential_profit)

    return max_profit

print (max_profit_bruteforce(stockPricesFromYesterday))

#guided solution: either evaluate it with the inner loop, but runtime is still o(n)^2
#greedy approach....check the most profit running through it O(n) or O(1) space...need to throw errors for invalid


def max_profit(stockPricesFromYesterday):
    profit = 0
    if len(stockPricesFromYesterday) < 2:
        return "not enough prices"
    if len(stockPricesFromYesterday) == 2 and stockPricesFromYesterday[1] < stockPricesFromYesterday[0]:
        return "no result"
    if len(stockPricesFromYesterday) == 2 and stockPricesFromYesterday[1] > stockPricesFromYesterday[0]:
        return stockPricesFromYesterday[1] - stockPricesFromYesterday[0]
    # if len(stockPricesFromYesterday) > 2:
    #     for price in stockPricesFromYesterday(range)

assert max_profit([1]) == "not enough prices"
assert max_profit([2,1]) == "no result"
assert max_profit([1,2]) == 1

# assert max_profit([1,2,3]) == 2



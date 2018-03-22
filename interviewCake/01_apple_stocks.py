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

                print("earlier time : " + str(earlier_time))
                print("later time : " + str(later_time))
                print("earlier price : " + str(earlier_price))
                print("later price : " + str(earlier_price))


                potential_profit = later_price - earlier_price
                max_profit = max(max_profit, potential_profit)

    return max_profit

print (max_profit_bruteforce(stockPricesFromYesterday))




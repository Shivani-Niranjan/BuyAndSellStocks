'''
Buy and Sell Stocks
Say you have an array, A, for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Return the maximum possible profit.

Input 1:
A = [1, 2]

Input 2:
A = [1, 4, 5, 2, 4]

Output 1:
1

Output 2:
4
'''
array = list(map(int, input().split()))
profit = 0
buy = array[0]
for sell in array[1:]:
    if sell > buy:
        profit = max(profit, sell - buy)
    else:
        buy = sell

print (profit)
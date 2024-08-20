## What we’re looking for:
# Working code. You should be able to run this from the command line or repl and have it work.
# We don’t really care which language you use, but we recommend something high level.
# We’re interested in the general style of code, how you use your editor, naming conventions etc.
# There are many ways to solve this, but we suggest using a simple approach, as it is not primarily an algorithmic exercise (though bonus points for knowing and being able to implement the best approaches).
# Also, just so you know we’re serious — the code _must_ work. Pseudo code or code with syntactic errors is an automatic 0.

## The problem
# Given a number `x` and a sorted array of coins `coinset`, write a function
# that finds a combination of these coins that add up to X
# There are an infinite number of each coin.
# This is hopefully familiar to making change for a given amount of money in a currency, but it gets more interesting if we remove the 1 coin and have “wrong” coins in the coinset.

# Return a map (or dictionary or whatever it is called in your preferred programming language such that each key is the coin, and each value is the number of times you need that coin.
# You need to only return a single solution, but for bonus points, return the one with the fewest number of coins.
# Don’t worry about performance or scalability for this problem.


# # A Specific example
# If x=7 and the coinset= [1,5,10,25], then the following are both solutions:
# `{1: 7}` since  7*1 = 7
# `{1: 2, 5: 1}` since 1*2 + 5*1=7

# Some test cases for you to verify your approach works
# A. x = 6 coinset = [1,5,10,25]
# B. x = 6, coinset = [3,4]
# C. x = 6, coinset = [1,3,4]
# D. x = 6, coinset = [5,7]
# E. x = 16, coinset = [5,7,9]


def make_change_1(x, coinset):
    reminder = x
    result = dict()
    for i in range(len(coinset)-1,-1,-1):
        coin = coinset[i]
        if coin <= reminder:
            times = reminder // coin
            reminder = reminder % coin
            result[coin] = times

    if reminder != 0:
        return None
    return result


def make_change(x, coinset):
    reminder = x
    result = dict()
    for i in range(len(coinset)-1,-1,-1):
        coin = coinset[i]
        if coin <= reminder:
            r = make_change(reminder - coin,coinset)
            if r is not None:
                r[coin] = r.get(coin,0) + 1
                return r

    if reminder != 0: return None
    return result

print(make_change(10, [3,4]))
print(make_change(9, [1,5,10,25]))
print(make_change(6, [1,5,10,25]))
print(make_change(7, [1,5,10,25]))
print(make_change(0, [1,5,10,25]))
print(make_change(6, [3,4]))
print(make_change(9, [3,4]))

print(make_change(5, [1,3,4]))
print(make_change(6, [1,3,4]))
print(make_change(6, [5,7]))
print(make_change(16, [5,7,9]))
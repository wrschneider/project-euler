cache = {}

def ways_to_make(n, coins, level):
    print(" " * level * 2, n, coins)
    if n == 0: return 1 # leaf node
    if len(coins) == 1:
        if n % coins[0] == 0: 
            return 1 # leaf node - fill with last coin.  Usually true if last coin is a one
        else: 
            return 0 # dead end - cannot be filled with last coin - only would happen if there is no 1p coin

    return sum(ways_to_make(n - coins[0] * i, coins[1:], level + 1) for i in range(0, n // coins[0] + 1))

coins = [1, 2, 5, 10, 20, 50, 100, 200][::-1]
print(ways_to_make(200, coins, 0))
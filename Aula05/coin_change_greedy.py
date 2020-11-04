def coin_change_greedy(n):
  coins = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.01]
  i = 0

  while(n>0):
    if(coins[i] > n):
      i = i+1
    else:
      print(coins[i])
      n = n-coins[i]

if __name__ == '__main__':
    given = 2.35
    coin_change_greedy(given)
import random
def primary():


  f = open("/Users/caroline/python-random-quote/quotes.txt")
  quotes = f.readlines()
  f.close()
  last = 13
  rnd = random.randint(0, last)
  print(quotes[rnd])

if __name__== "__main__":
  primary()

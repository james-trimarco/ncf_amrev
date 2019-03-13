def combinator(x):
  prods = list(itertools.combinations(x,2))
  strength = (1,)
  flips = []
  new_prods = []
  
  for item in prods:
    reversal = item[::-1]
    flips.append(reversal)
    
  prods = prods + flips

  for tup in prods:
    new_prods.append(tup + strength)
    
  return new_prods
import math
import django
my_list = [0,1,2,3,4,5,6,7,8,9]
win_countries = ["India", "USA", "Japan", "USA", "UK", "Japan"]
profile = {"name" : "John Doe", "username" : "johndoe", "languages" : ["Python", "Java", "JavaScript"], "followers" : 100}

class happy:
  # numeric operations
  def is_prime(num):
    for i in range(2, math.floor(math.sqrt(num))+1):
      if num % i == 0:
        return False
    return True
  def multiples_of(num, end = 64):
    multiples = []
    for i in range(num, end+1, num):
      multiples.append(i)
    return multiples
  # list operations
  def copy(target):
    return target[:] # copies list
  def rev(target):
    return target[::-1] # reverses list
  def skip(target, multiple=2):
    return target[::multiple]
  def purify(target, order = True):
    if order:
      return sorted(list(set(target))) # returns alphabetically ordered list
    else:
      return list(set(target)) # returns randomly placed list
  # dictionary operations
  def split(dictionary):
    output = []
    keys = []
    values = []
    for key, value in dictionary.items():
      keys.append(key)
      values.append(value)
    output.append(keys)
    output.append(values)
    return output # returns nested list
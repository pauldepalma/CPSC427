#Permute a list
def make_teams(num):
  lst = [i for i in range(1,num+1)]

  lst = Permutations(lst).random_element()

  print lst



from operator import itemgetter

def calcDistances(unknown,movie_data):
    dist_lst = []
    for point in movie_data:
      xdist = (point[0] - unknown[0])**2
      ydist = (point[1] - unknown[1])**2
      dist = (xdist + ydist) ** .05
      item = (dist,point[2])
      dist_lst.append(item)
    return sorted(dist_lst,key=itemgetter(0))

def count_votes(distances,k):
    vote_count = {}
    vote_count['r'] = 0
    vote_count['a'] = 0
    for i in range(k):
        label = distances[i][1]
        if vote_count[label] > 0:
            vote_count[label] = vote_count[label] + 1
        else:
            vote_count[label] = 1

    if (vote_count['r'] > vote_count['a']):
        return 'r'
    else:
        return 'a'
    
def main():
    unknown = (18,90)
    title = "Blade Runner"
    k = 3
    movie_data = [(3,104,'r'),(2,100,'r'),(1,81,'r'),(101,10,'a'),(99,5,'a'),
                  (98,2,'a')]
    

    distances = calcDistances(unknown, movie_data)
    winner = count_votes(distances,k)
    if winner == 'r':
        type = 'romance'
    else:
        type = 'adventure'

    print (title + ':' + type)
    
main()

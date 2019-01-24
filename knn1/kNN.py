
import operator

def calcDistances(unknown,movie_data):
    dist_lst = []
    for point in movie_data:
      xdist = (point[0] - unknown[0])**2
      ydist = (point[1] - unknown[1])**2
      dist = (xdist + ydist) ** .05
      item = (dist,point[2])
      #dist_lst is a list of tuples  of the form (distance, label)
      dist_lst.append(item)
    return dist_lst

#count_votes is a collection of label:vote pairs, where 'vote' is the number
#of votes gotten by the label.  sorted_vote_count is list of label,vote tuples,
#sorted by votes in reverse numerical order.  So, the 0th item in the list is 
#the tuple containing the label with the most votes, the 1st item is the tuple
#containing the second highest vote count and so forth
def count_votes(dist_lst,k):
    vote_count = {}
    for i in range(k):
        label = dist_lst[i][1]
        if label in vote_count:
            vote_count[label] = vote_count[label] + 1
        else:
            vote_count[label] = 1

    sorted_vote_count = sorted(vote_count.iteritems(), 
            key=operator.itemgetter(1),
            reverse = True)

    #0th item in 0th tuple, i.e, the label with the most votes
    return sorted_vote_count[0][0] 

    
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

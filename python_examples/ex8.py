'''
Demonstrates:
    split
    join
    set
'''

def split_join():
    str1 = 'These are the days when birds come back'
    lst = str1.split()  #create a list with words of str1 as elements
    for item in lst:
        print (item)

    str2 = ''.join(lst) #construct a string from the elements of lst
    #notice that spaces are removed relative to the original string
    print (str2)

def do_set():
    people1 = set(['Zack', 'John', 'Mary', 'Katie']) #create set
    people2 = set(['Katie', 'Michael'])  #create set

    print ('Jeremy' in people1) #check for set membership
    print ('Katie' in people2)  #check for set membership

    people3 = people1 & people2 #set intersection
    print(people3)

    people4 = people1 | people2 #set union
    print (people4)

    print(people2 <= people1) #is people2 a subset of people1
    print(people2 >= people1) #is people2 a superset of people1
    

def main():
    split_join()
    do_set()
    
                   
main()
    

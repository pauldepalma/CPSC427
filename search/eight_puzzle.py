'''
CPSC 427 
Paul De Palma
GU Username: depalma
ex4.py
Generates first-level child states from an initial state of the 8-puzzle 
Usage: python proj4.py
References
1. An Eight-Puzzle Solver in Python, downloaded: 2/18/18 from 
   https://gist.github.com/flatline/8382021
'''

from copy import deepcopy

#nested list representation of 8 puzzle. 0 is the blank
_init_state = [[2,8,3],
               [1,6,4],
               [7,0,5]]

class EightPuzzle:
    def __init__(self):
        #child states will be kept in a list
        #the constructor adds the initial (i.e., parent state) to the list
        self.state_lst = [[row for row in _init_state]]

    #displays all states in the list
    def display(self):
        for state in self.state_lst:
            for row in state:
                print row
            print ""
        

    #returns (row,col) of value in state indexed by state_idx  
    def find_coord(self, value, state_idx):
        for row in range(3):
            for col in range(3):
                if self.state_lst[state_idx][row][col] == value:
                    return (row,col)
                
    #returns list of (row, col) tuples which can be swapped for blank
    #these form the legal moves of state state_idx within the state list 
    def get_new_moves(self, state_idx):
        row, col = self.find_coord(0,state_idx) #get row, col of blank
        moves = []
        if row > 0:
            moves.append((row - 1, col))  #move from directly above
        if col > 0:
            moves.append((row, col - 1))  #move from the left
        if row < 2:
            moves.append((row + 1, col)) # move from the bottom
        if col < 2:
            moves.append((row, col + 1)) # move from the right
        return moves


    #Generates all child states for the state indexed by state_idx
    #in the state list.  Appends child states to the list
    def generate_states(self,state_idx):
        #get legal moves
        move_lst = self.get_new_moves(state_idx)
        
        #find coordinates of the blank position
        blank = self.find_coord(0,state_idx)

        #shift the blank and tile to be moved for each move 
        #append resulting state to the state list
        for tile in move_lst:
            #create a new state using deep copy 
            #ensures that matrices are completely independent
            clone = deepcopy(self.state_lst[state_idx])

            #move tile to position of the blank
            clone[blank[0]][blank[1]] = clone[tile[0]][tile[1]]

            #set tile position to 0                          
            clone[tile[0]][tile[1]] = 0
            
            #append child state to the list of states.
            self.state_lst.append(clone)

def main():
    p = EightPuzzle()
    p.generate_states(0)
    p.display()


if __name__ == "__main__":
    main()

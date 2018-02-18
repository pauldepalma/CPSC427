'''
CPSC 427 
Paul De Palma
GU Username: depalma
ex4.py
Generates first-level child states from an initial state of the 8-puzzle 
a defined initial state
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
        self.matrix_lst = [[row for row in _init_state]]

    #displays all states in the list
    def display(self):
        for matrix in self.matrix_lst:
            for row in matrix:
                print row
            print ""
        

    #returns (row,col) of value in state indexed by matrix_idx  
    def find_coord(self, value, matrix_idx):
        if value < 0 or value > 8:
            raise Exception("value out of range")

        for row in range(3):
            for col in range(3):
                if self.matrix_lst[matrix_idx][row][col] == value:
                    return (row,col)
                
    #returns list of (row, col) tuples which can be swapped for blank
    #these form the legal moves of state matrix_idx within the state list 
    def get_new_moves(self, matrix_idx):
        row, col = self.find_coord(0,matrix_idx) #get row, col of blank
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


    
    def generate_states(self,matrix_idx):
        #get legal moves
        move_lst = self.get_new_moves(matrix_idx)
        
        #find coordinates of the blank position
        blank = self.find_coord(0,matrix_idx)

        #shift the blank and tile to be moved for each move 
        #append resulting state to the matrix list
        for tile in move_lst:
            #create a new matrix using deep copy 
            #ensures that matrices are completely independent
            clone = deepcopy(self.matrix_lst[matrix_idx])

            #move tile to position of the blank
            clone[blank[0]][blank[1]] = clone[tile[0]][tile[1]]

            #set tile position to 0                          
            clone[tile[0]][tile[1]] = 0
            
            #append new game configuration to the list of game configurations
            self.matrix_lst.append(clone)

def main():

    p = EightPuzzle()
    p.generate_states(0)
    p.display()


if __name__ == "__main__":
    main()

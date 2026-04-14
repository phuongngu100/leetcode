class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        # notice a pattern east (to the right), south (down), west (left), then north (up). so this is clockwise, and we do this pattern everytime by incresing the distance.

        # first store the directions
        dir = [[0,1],[1,0],[0,-1],[-1,0]] # order matters, move like the pattern east south west north

        visited = [] # keep those have visited so dont see again

        step = 1 # initial step is 1

        direction = 0 #start moving east first

        while len(visited) < rows * cols: #total cell, only stop when all is found
            for _ in range(2): #each step size is used twice!! after that increase the step
                for _ in range(step): #if step =3 step 3 in 2 directions then increase the outer loop until reach 2 said directions
                    if(rStart >= 0 and rStart < rows and cStart >=0 and cStart < cols): #check if current position is inside the grid
                        visited.append([rStart,cStart])
                    # make changes to the current position
                    rStart += dir[direction][0] #first append the position THEN move
                    cStart += dir[direction][1]
                direction = (direction + 1) % 4 # turn 90 degrees
            step +=1

            '''
            core idea
            for _ in range(step):
                move one step

            direction = (direction + 1) % 4 --> move one step, then turn right
            '''
        return visited

        
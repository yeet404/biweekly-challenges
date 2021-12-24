FILL = 0

class SeatLayout:
    layout = []

    # init using length by width format
    def __init__(self, col, row):
        self.col = col
        self.row = row
        for i in range(row):
            self.layout.append([FILL for j in range(col)])

    def add(self, row, col, name):
        # TODO: refactor this repetitive check
        row -= 1
        col -= 1
        if row < 0 or col < 0:
            print("Invalid seat.")
            return

        try:
            if not self.layout[row][col]:
                self.layout[row][col] = str(name)
            else:
                print("Seat occupied.")
        except IndexError:
            print("Invalid seat.")

    def remove(self, row, col):
        row -= 1
        col -= 1
        if row < 0 or col < 0:
            print("Invalid seat.")
            return
        
        try:
            if self.layout[row][col]:
                self.layout[row][col] = 0
            else:
                print("Seat empty.")
        except IndexError:
            print("Invalid seat.")
    
    # inconsistent return types (void, list) since printing to console anyways
    # this probably isn't a good idea but idk lol
    def find_exposed(self, row, col):
        RADIUS = 1
        row -= 1
        col -= 1
        
        if row < 0 or col < 0:
            print("Invalid seat.")
            return

        try:
            if not self.layout[row][col]:
                print("Seat empty.")
                return
        except IndexError:
            print("Invalid seat.")

        # this is so bad lol
        # finds people exposed 
        exposed = []
        seats = [(RADIUS, 0), (0, RADIUS)]
        for i in seats:
            try:
                top_left = self.layout[row-i[0]][col-i[1]]
                if top_left:
                    exposed.append(top_left)
            except IndexError:
                pass
            try:
                bottom_right = self.layout[row+i[0]][col+i[1]]
                if bottom_right:
                    exposed.append(bottom_right)
            except IndexError:
                pass
        
        print(exposed)
    
    def print(self):
        for i in range(self.row):
            print(*self.layout[i])
    
    # DEBUG
    def debug(self, type):
        if type == "remove":
           for i in range(1, self.row+1):
                for j in range(1, self.col+1):
                    self.remove(i, j) 
        if type == "add":
            for i in range(1, self.row+1):
                for j in range(1, self.col+1):
                    self.add(i, j, "Bob")

def main():
    test = SeatLayout(3, 4)
    # test.add(4, 3, "Bob") # add
    # test.add(3, 3, "yeet") # add+remove
    # test.remove(3, 3)
    # test.add(4, 3, "Rob") # add occupied
    # test.remove(1, 1) # remove empty
    # test.add(100, 100, "asdf") # add invalid
    # test.remove(1000, 34) # remove invalid
    
    # test.add(-1, -1, "Negative") # add invalid (neg)
    # test.remove(-2, -3) # remove invalid (neg)

    # test.debug("add")

    test.find_exposed(2, 2)

    test.print()

if __name__ == "__main__":
    main()

DEBUG = True
FILL = 0

# src: https://stackoverflow.com/a/30650004
class strictlist(list):
    def __getitem__(self, n):
        if n < 0:
            raise IndexError("...")
        return list.__getitem__(self, n)

class SeatLayout:
    layout = strictlist()

    # init using length by width format
    def __init__(self, col, row):
        self.col = col
        self.row = row
        for i in range(row):
            self.layout.append(strictlist(FILL for j in range(col)))

    # expects 0-indexed
    def add(self, row, col, name):
        try:
            if not self.layout[row][col]:
                self.layout[row][col] = str(name)
            else:
                print("Seat occupied.")
        except IndexError:
            print("Invalid seat.")

    def remove(self, row, col):
        try:
            if self.layout[row][col]:
                self.layout[row][col] = 0
            else:
                print("Seat empty.")
        except IndexError:
            print("Invalid seat.")

    def find_exposed(self, row, col):
        RADIUS = 1

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
           for i in range(self.row):
                for j in range(self.col):
                    self.remove(i, j) 
        if type == "add":
            for i in range(self.row):
                for j in range(self.col):
                    self.add(i, j, "Bob")

def debug():
    test = SeatLayout(3, 4)
    # print(test.layout)
    # test.add(3, 2, "Bob") # add
    # test.add(2, 2, "yeet") # add+remove
    # test.remove(2, 2)
    # test.add(3, 2, "Rob") # add occupied
    # test.remove(0, 0) # remove empty
    # test.add(100, 100, "asdf") # add invalid
    # test.remove(1000, 34) # remove invalid
    
    # test.add(-1, -1, "Negative") # add invalid (neg)
    # test.remove(-2, -3) # remove invalid (neg)

    test.debug("add")

    test.find_exposed(1, 0)

    test.print()

def main():
    pass

if __name__ == "__main__":
    if DEBUG:
        debug()
    else:
        main()

class SeatLayout:
    layout = []

    # length x width format
    def __init__(self, col, row):
        self.col = col
        self.row = row
        for i in range(row):
            self.layout.append([0 for j in range(col)])

    def add(self, row, col, name):
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
            return

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
    """
    def get_exposed(self, row, col):
        RADIUS = 1
        row -= 1
        col -= 1
        exposed = []

        try:
            if not self.layout[row][col]:
                print("Seat empty.")
                return exposed.append(-1)
        except IndexError:
            print("Invalid seat.")

        # this is so bad lol
        seats = [(RADIUS, 0), (0, RADIUS)]
        for i in seats:
            try:
                exposed.append(self.layout[row-i[0]][col-i[1]])
            except IndexError:
                pass
            try:
                exposed.append(self.layout[row+i[0]][col+i[1]])
            except IndexError:
                pass
        
        return exposed
    """
    def print(self):
        for i in range(self.row):
            print(*self.layout[i])

def main():
    test = SeatLayout(3, 4)
    test.add(4, 3, "Bob") # add
    test.add(3, 3, "yeet") # add+remove
    test.remove(3, 3)
    test.add(4, 3, "Rob") # add occupied
    test.remove(1, 1) # remove empty
    test.add(100, 100, "asdf") # add invalid
    test.remove(1000, 34) # remove invalid
    
    test.add(-1, -1, "Negative") # add invalid (neg)
    test.remove(-2, -3) # remove invalid (neg)
    
    test.print()

if __name__ == "__main__":
    main()

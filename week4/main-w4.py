class SeatLayout:
    layout = []
    def __init__(self, l, w):
        self.l = l
        self.w = w
        for i in range(self.w):
            self.layout.append([0 for j in range(self.l)])

    def add(self, row, col):
        row -= 1
        col -= 1
        try:
            if not self.layout[row][col]:
                self.layout[row][col] = 1
            else:
                print("Seat occupied.")
        except IndexError:
            print("Invalid seat.")

    def remove(self, row, col):
        row -= 1
        col -= 1
        try:
            if self.layout[row][col]:
                self.layout[row][col] = 0
            else:
                print("Seat empty.")
        except IndexError:
            print("Invalid seat.")

    def print(self):
        for i in range(self.w):
            print(*self.layout[i])

def main():
    test = SeatLayout(3, 4)
    test.add(4, 3) # add
    test.add(3, 3) # add+remove
    test.remove(3, 3)
    test.add(4, 3) # add occupied
    test.remove(1, 1) # remove empty
    test.add(100, 100) # add invalid
    test.remove(1000, 34) # remove invalid
    
    test.print()

if __name__ == "__main__":
    main()
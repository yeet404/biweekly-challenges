"""
There is so much bad code in this lol.
"""

import sys

FILL = 0

# src: https://stackoverflow.com/a/30650004
class strictlist(list):
    def __getitem__(self, n):
        if n < 0:
            raise IndexError("...")
        return list.__getitem__(self, n)

class SeatLayout:
    # init using length by width format
    def __init__(self, col, row):
        self.layout = strictlist()
        self.col = col
        self.row = row
        for i in range(row):
            self.layout.append(strictlist(FILL for j in range(col)))

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

        # ew
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
        
        print("Person(s) exposed: \n - ", end="")
        print(*exposed, sep="\n - ")
    
    # really bad but hopefully understandable
    def print(self):
        # find longest string in self.layout
        longest = 1
        for i in range(self.row):
            for j in self.layout[i]:
                name_len = len(str(j))
                if name_len > longest:
                    longest = name_len
        # ensure all seats/pipes (|) line up
        MOST_SPACE = longest * " "
        space = ""
        for i in range(self.row):
            for j in self.layout[i]:
                space = MOST_SPACE[0:longest-len(str(j))]
                print(f"{j}{space}", end="|")
            print()
            # print(*self.layout[i])
    
    # DEBUG - fill/empty all seats
    def debug(self, type):
        if type == "remove":
           for i in range(self.row):
                for j in range(self.col):
                    self.remove(i, j) 
        if type == "add":
            for i in range(self.row):
                for j in range(self.col):
                    self.add(i, j, "Bob")

def inputf():
    return sys.stdin.readline().split()

# yum spaghetti
# input is 1-indexed
# should refactor some more
def main():
    print("-----\nSeating Organizer - yeet404\n-----")
    s = None
    saved = {}
    while True:
        try:
            i = inputf()
        except KeyboardInterrupt:
            print("Type \"end\" to exit.\n")
            continue
        try:
            match i[0]:
                case "create":
                    try:
                        s = SeatLayout(int(i[1]), int(i[2]))
                    except (IndexError, ValueError):
                        print("Invalid syntax.")
                case "add":
                    try:
                        s.add(int(i[1])-1, int(i[2])-1, i[3])
                    except (IndexError, ValueError, AttributeError):
                        print("Invalid syntax.")
                case "rm":
                    try:
                        s.remove(int(i[1])-1, int(i[2])-1)
                    except (IndexError, ValueError, AttributeError):
                        print("Invalid syntax.")
                case "print":
                    try:
                        s.print()
                    except (UnboundLocalError, AttributeError):
                        print("Invalid syntax.")
                case "exposed":
                    try:
                        s.find_exposed(int(i[1])-1, int(i[2])-1)
                    except (IndexError, ValueError, AttributeError):
                        print("Invalid syntax.")
                case "save":
                    if s:
                        try:
                            saved[str(i[1])] = s
                        except (KeyError, IndexError):
                            print("Invalid syntax.")
                    else:
                        print("No layout to save.")
                case "access":
                    try:
                        s = saved[str(i[1])]
                    except (IndexError, KeyError):
                        print("Invalid syntax.")
                # bad implementation
                case "del":
                    if not s:
                        print("No layout to delete.\n")
                        continue
                    try:
                        if i[1] == "this":
                            del s
                        else:
                            del saved[str(i[1])]
                    except (IndexError, KeyError):
                        print("Invalid syntax.") 
                case "end":
                    return
                case _:
                    print("Invalid command.")
        except IndexError:
            print("Type \"end\" to exit.")
        print()

if __name__ == "__main__":
    main()

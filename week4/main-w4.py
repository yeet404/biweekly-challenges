class SeatLayout:
    layout = []
    def __init__(self, l, w):
        self.l = l
        self.w = w
        for i in range(self.w):
            self.layout.append([0 for j in range(self.l)])

    def print(self):
        for i in range(self.w):
            print(*self.layout[i])

def main():
    sl = SeatLayout(3, 4)
    sl.print()

if __name__ == "__main__":
    main()
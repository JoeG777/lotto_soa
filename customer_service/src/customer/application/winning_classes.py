from collections import defaultdict

class WinningClasses:
    winning_class = defaultdict(lambda: 0)

    def __init__(self):
        s = [
            ((6,1), 1),
            ((6,0) ,2),
            ((5,1), 3),
            ((5,0),4),
            ((4,1),5),
            ((4,0),6),
            ((3,1),7),
            ((3,0),8),
            ((2,1),9)
        ]
        for k, v in s:
            self.winning_class[k]=v

    def get(self, key:tuple[int, int]):
        return self.winning_class[key]

winning_classes = WinningClasses()
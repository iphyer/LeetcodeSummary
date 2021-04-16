class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x,y = ord(coordinates[0]) - ord('a'), int(coordinates[1])-1
        if x % 2 == 0 and y % 2 == 0:
            return False
        elif x % 2 == 0 and y % 2 != 0:
            return True
        elif x % 2 != 0 and y % 2 == 0:
            return True
        else:
            return False

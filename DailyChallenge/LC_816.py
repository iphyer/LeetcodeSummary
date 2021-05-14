class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        s = s[1:-1]
        N = len(s)
        res = []
        
        def DecimalPointsLists(x: str) -> List[str]:
            output = []
            # without Decimal Points
            if x[0] != "0" or x == "0":
                output.append(x)
            # with Decimal Points
            for i in range(1, len(x)):
                if (x[:i] == "0" or x[0] != "0") and x[-1] != "0":
                    # 0.001 True
                    # 00.01 False
                    # 0.000 False
                    tmp = x[:i] + "." + x[i:]
                    output.append(tmp)
            return output
        
        for i in range(1, N):
            x = s[:i]
            y = s[i:]
            
            for x_c in DecimalPointsLists(x):
                for y_c in DecimalPointsLists(y):
                    res.append("({}, {})".format(x_c, y_c))
        return res

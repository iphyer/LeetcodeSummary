class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        res = 0
        if startTime < finishTime:
            # not overnight
            s = startTime.split(":")
            f = finishTime.split(":")
            res = 4 * ( int(f[0]) - int(s[0]) - 1)
            t1 = s[1]
            if t1 == "00": res += 1
            if t1 <= "15": res += 1
            if t1 <= "30": res += 1
            if t1 <= "45": res += 1
            
            t2 = f[1]
            if t2 >= "15": res += 1
            if t2 >= "30": res += 1
            if t2 >= "45": res += 1
            
        else:
            # overnight
            # Day 1
            s = startTime.split(":")
            f = finishTime.split(":")
            res = 4 * ( 23 - int(s[0]))
            t1 = s[1]
            if t1 == "00": res += 1
            if t1 <= "15": res += 1
            if t1 <= "30": res += 1
            if t1 <= "45": res += 1

            # Day 2
            res += 4 * (int(f[0]) )
            t2 = f[1]
            if t2 >= "15": res += 1
            if t2 >= "30": res += 1
            if t2 >= "45": res += 1
        return res

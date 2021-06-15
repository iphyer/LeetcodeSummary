class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # greedy
        sortedBoxTypes = sorted(boxTypes, key = lambda x: x[1], reverse = True)
        res = 0
        while truckSize > 0 and sortedBoxTypes:
            truck_num, truck_unit = sortedBoxTypes.pop(0)
            if truck_num > truckSize:
                res += truck_unit * truckSize
                truckSize = 0
            else:
                res += truck_unit * truck_num
                truckSize -= truck_num
        return res

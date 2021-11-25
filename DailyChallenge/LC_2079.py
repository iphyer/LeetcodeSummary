class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        # simulation
        res = 0
        curr_can_ind = -1
        curr_capacity = capacity
        plant_ind = 0
        while plant_ind < len(plants):
            while plant_ind < len(plants) and curr_capacity >= plants[plant_ind]:
                #print(res)
                res += (plant_ind - curr_can_ind)
                curr_capacity -= plants[plant_ind]
                curr_can_ind = plant_ind
                plant_ind += 1
            #print(res)
            if curr_can_ind != len(plants) - 1:
                curr_capacity = capacity
                res += (curr_can_ind * 2 + 2)
        return res
            

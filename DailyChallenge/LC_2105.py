class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        # simulation
        ans = 0
        amountA = capacityA
        amountB = capacityB
        
        Flag_odd = False
        N = len(plants)
        
        if N % 2 == 0:
            # even plants
            indexA = N // 2
            indexB = N // 2 - 1
        else:
            indexA = N // 2
            indexB = N // 2
            Flag_odd = True
        
        # calcuate A
        for i in range(0, indexA):
            if plants[i] > amountA:
                # water not enough, need refill
                while plants[i] > amountA:
                    if amountA < capacityA:
                        amountA = capacityA
                    ans += 1
                    if plants[i] > amountA:
                        plants[i] -= amountA
                    else:
                        amountA -= plants[i]
                        plants[i] = 0
                # no need to refill
                if plants[i]: # still left some not filled but less than capacityA
                    amountA = capacityA - plants[i]
            else:
                # water enough no need to refill
                amountA = amountA - plants[i]
        #print(ans)
        # calcuate B
        for i in range(N-1, indexB, -1):
            #print(i, amountB)
            if plants[i] > amountB:
                # water not enough, need refill
                while plants[i] > amountB:
                    if amountB < capacityB:
                        amountB = capacityB
                    ans += 1
                    if plants[i] > amountB:
                        plants[i] -= amountB
                    else:
                        amountB -= plants[i]
                        plants[i] = 0
                # no need to refill
                if plants[i]: # still left some not filled but less than capacityA
                    amountB = capacityB - plants[i]
            else:
                # water enough no need to refill
                amountB = amountB - plants[i]
        #print("B finished")
        #print(ans)
        #print(amountA)
        #print(amountB)
        # calcuate the middle one in odd number of plants
        if Flag_odd:
            #print("Flag_odd")
            #print(ans)
            #print(amountA)
            #print(amountB)
            i = N // 2
            #the one with more water currently in his/her watering can should water this plant. If they have the same amount of water, then Alice should water this plant.
            if amountA < amountB:
                # B takes it
                if plants[i] > amountB:
                    # water not enough, need refill
                    while plants[i] > amountB:
                        if amountB < capacityB:
                            amountB = capacityB
                        ans += 1
                        if plants[i] > amountB:
                            plants[i] -= amountB
                        else:
                            amountB -= plants[i]
                            plants[i] = 0
                    # no need to refill
                    if plants[i]: # still left some not filled but less than capacityA
                        amountB = capacityB - plants[i]
                else:
                    # water enough no need to refill
                    amountB = amountB - plants[i]
                
            else:
                # A takes it
                if plants[i] > amountA:
                    # water not enough, need refill
                    while plants[i] > amountA:
                        if amountA < capacityA:
                            amountA = capacityA
                        ans += 1
                        if plants[i] > amountA:
                            plants[i] -= amountA
                        else:
                            amountA -= plants[i]
                            plants[i] = 0
                    # no need to refill
                    if plants[i]: # still left some not filled but less than capacityA
                        amountA = capacityA - plants[i]
                else:
                    # water enough no need to refill
                    amountA = amountA - plants[i]
        #print(ans)       
        return ans

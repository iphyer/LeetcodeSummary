class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # find combined rect
        max_x = -float('inf')
        min_x = float('inf')
        max_y = -float('inf')
        min_y = float('inf')
        area_each_sum = 0
        
        # Using two methods to judge
        # (1) Total Area
        # (2) No over lapping: two loops is too slow 
        #       using four conner points of rectangles to solve it
        #       the conner points in the final results should only be max_x,max_y,min_x,min_y
        points = set()
        for rect in rectangles:
            # check area summary
            area_each_sum += abs(rect[0] - rect[2]) * abs(rect[1] -rect[3])
            if max_x < max(rect[0], rect[2]): max_x = max(rect[0], rect[2])
            if min_x > min(rect[0], rect[2]): min_x = min(rect[0], rect[2])
            if max_y < max(rect[1], rect[3]): max_y = max(rect[1], rect[3])
            if min_y > min(rect[1], rect[3]): min_y = min(rect[1], rect[3])
            # check four conner points
            rect_p = [(rect[0], rect[1]), (rect[2], rect[1]), (rect[0], rect[3]), (rect[2], rect[3])]
            for p in rect_p:
                if p in points: points.remove(p)
                else: points.add(p)
        # check total area           
        area_all = (max_y - min_y) * (max_x - min_x)
        if area_each_sum != area_all: return False
        # check remaining four conners
        if len(points) != 4: return False
        # check the left 4 points, should be max_x,max_y,min_x,min_y
        if (max_x, min_y) not in points: return False
        if (max_x, max_y) not in points: return False
        if (min_x, min_y) not in points: return False
        if (min_x, max_y) not in points: return False
        # pass all checkings
        return True
        """ Two Loops == > Too Slow
        else:
            # should be no IoU in rectangles
            for i in range(len(rectangles)):
                for j in range(i+1,len(rectangles)):
                    Pi_x1, Pi_y1, Pi_x2, Pi_y2 = rectangles[i][0], rectangles[i][1], rectangles[i][2], rectangles[i][3]
                    Pj_x1, Pj_y1, Pj_x2, Pj_y2 = rectangles[j][0], rectangles[j][1], rectangles[j][2], rectangles[j][3]
                    # get IoU rect
                    left_max = max(Pi_x1, Pj_x1)
                    top_max = max(Pi_y1, Pj_y1)
                    right_min =  min(Pi_x2, Pj_x2)
                    bottom_min = min(Pi_y2, Pj_y2)
                    # IoU inter area
                    inter = max(0,(right_min-left_max)) * max(0, (bottom_min-top_max))
                    if inter > 0:
                        return False
            # no overlapping
            return True
        """

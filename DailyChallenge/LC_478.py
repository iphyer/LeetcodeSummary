class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        # x = r * cos(theta) + x0
        # y = r * sin(theta) + y0
        # r:     0 ~ raduis
        # theta: 0 ~ 360
        # r should be sqrt(random())
        # the probabilty of finding points in larger r should be larger than points in smaller r
        # https://stackoverflow.com/questions/5837572/generate-a-random-point-within-a-circle-uniformly

        r = math.sqrt(random.random()) * self.radius 
        theta = random.uniform(0, 360) / (2 * math.pi)
        
        return [r * math.cos(theta) + self.x, r * math.sin(theta) + self.y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()

"""

Rejection Sampling Methods

https://maxming0.github.io/2021/03/17/Generate-Random-Point-in-a-Circle/


    def randPoint(self) -> List[float]:
        while True:
            u = 2 * random.random() - 1
            v = 2 * random.random() - 1
            if u * u + v * v <= 1:
                return [self.x + u * self.r, self.y + v * self.r]

"""


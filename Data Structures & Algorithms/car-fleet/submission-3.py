"""
facts:
    n items, position -> starting position , speed -> how many grid to move per hour
        all with len n
    target -> the ending position
        the car can only move speed[i] per iteration
        All the values of position are unique.
    a car cannot pass another car ahead of it
        it can only drive at the same speed if catch up witgh another car -> they will become a v
            single car is also consider a car carFleet
            the car with same speed will be different carfleet
    return the number of different car fleet at the ending position

"""


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        for i in range(len(position)):
            arr.append((position[i], speed[i]))
        arr.sort(key=lambda car: car[0], reverse=True)
        res = 1
        currMin = None
        for pos, speed in arr:
            n = (target - pos) / speed
            if currMin == None:
                currMin = n
            else:
                if n > currMin:
                    currMin = n
                    res += 1
        return res

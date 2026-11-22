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
        arr = sorted(zip(position, speed), key=lambda car: car[0], reverse=True)
        res = 1
        currMin = (target - arr[0][0]) / arr[0][1]
        for i in range(1, len(arr)):
            pos, spe = arr[i]
            n = (target - pos) / spe
            if n > currMin:
                currMin = n
                res += 1
        return res

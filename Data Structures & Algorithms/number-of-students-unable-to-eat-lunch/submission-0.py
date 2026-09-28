class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        obj = {
            1: students.count( 1),
            0: students.count( 0)
        }
        for i in sandwiches:
            obj[i] -= 1
            if(obj[i] == -1):
                return obj[1 if i == 0 else 0]
        return 0
        


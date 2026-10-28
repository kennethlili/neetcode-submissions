# {
#     row:{
#         1: []
#     }
#     col:{
#         colNumer
#     }
#     box:{

#     }
# }

# 1,1 1,2 1,3 1,4
# 2,1


# 4,1

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {} 
        col = {}
        box = {}
        for i in range(9):
                row[i] = defaultdict(list)
                col[i] = defaultdict(list)
                box[i] = defaultdict(list)
            
        for r in range(len(board)):
            for c in range(len(board[0])):
                print(r,c)
                val = board[r][c]
                if val == '.':
                    continue
                if not row[r][val]:
                    row[r][val] = 1
                else:
                    return False
                if not col[c][val]:
                    col[c][val] = 1
                else:
                    return False
                boxid = 0
                if r< 3 and c < 3:
                    boxid = 0
                elif r< 3 and c < 6:
                    boxid = 1
                elif r< 3 and c < 9:
                    boxid = 2
                elif r< 6 and c < 3:
                    boxid = 3
                elif r< 6 and c < 6:
                    boxid = 4
                elif r< 6 and c < 9:
                    boxid = 5
                elif r< 9 and c < 3:
                    boxid = 6
                elif r< 9 and c < 6:
                    boxid = 7
                elif r< 9 and c < 9:
                    boxid = 8

                if not box[boxid][val]:
                    box[boxid][val] = 1
                else:
                    return False
            
            
        return True



                

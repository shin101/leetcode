class Solution:
    def judgeCircle(self, moves: str) -> bool:
        curr = [0,0]
        for move in moves:
            if move == "U" : 
                curr[1] += 1
            elif move == "D":
                curr[1] -= 1
            elif move == "L":
                curr[0] -=1
            else: # move is R
                curr[0] += 1
        return [0,0] == curr
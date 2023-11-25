class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        D, R = deque([]), deque([])
        for idx, char in enumerate(senate):
            if char == "D":
                D.append(idx)
            else:
                R.append(idx)
        
        while D and R:
            d_pop = D.popleft()
            r_pop = R.popleft()

            if d_pop < r_pop:
                D.append(d_pop + len(senate))
            else:
                R.append(len(senate) + r_pop)

        return "Dire" if D else "Radiant"

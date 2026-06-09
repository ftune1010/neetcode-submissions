class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                if num in rows[r]:
                    return False
                if num in cols[c]:
                    return False
                pos = (r // 3) * 3 + (c // 3)
                if num in boxes[pos]:
                    return False
                rows[r].add(num)
                cols[c].add(num)
                boxes[pos].add(num)
        return True
        
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowsNums = [[]] * 9
        colsNums = [[]] * 9
        groupsNums = {}

        for rowIdx, row in enumerate(board):
            for colIdx, cell in enumerate(row):
                if (cell == "."):
                    continue
                rowNums = rowsNums[rowIdx]
                colNums = colsNums[colIdx]
                group = (rowIdx // 3, colIdx //3)
                groupNums = groupsNums.get(group)

                if (cell in rowNums or cell in colNums or (groupNums is not None and cell in groupNums)):
                    return False
                else:
                    rowsNums[rowIdx] = rowNums + [cell]
                    colsNums[colIdx] = colNums + [cell]
                    groupsNums[group] = groupNums + [cell] if groupNums is not None else [cell]

        return True

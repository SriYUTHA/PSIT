"""Island"""
def main(island):
    """Find the number of islands ?"""
    island_row, island_col = [int(x) for x in input().split()]
    lst_island = [input().split() for _ in range(island_row)]
    for row in range(island_row):
        for col in range(island_col):
            if lst_island[row][col] == '1':
                island += 1
                lst_island = same_island(col, row, lst_island)
    print(island)

def same_island(col, row, lst_island):
    """find same island"""
    surround1 = [(row-1, col-1), (row-1, col), (row-1, col+1), (row, col-1)]
    surround2 = [(row, col), (row, col+1), (row+1, col-1), (row+1, col), (row+1, col+1)]
    surround = surround1 + surround2
    for i, j in surround:
        if i < 0 or j < 0 or i > len(lst_island)-1 or j > len(lst_island[0])-1:
            pass
        elif lst_island[i][j] == '1':
            lst_island[i][j] = '2'
            lst_island = same_island(j, i, lst_island)
    return lst_island
main(0)

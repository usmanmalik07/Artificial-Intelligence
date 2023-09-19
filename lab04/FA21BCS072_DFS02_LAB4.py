row = [-1, -1, -1, 0, 1, 0, 1, 1]
col = [-1, 1, 0, -1, -1, 1, 0, 1]
 
def isSafe(x, y, processed):
    return (0 <= x < len(processed)) and (0 <= y < len(processed[0]))\
        and not processed[x][y]

def searchBoggle(board, words, result, processed, i, j, path=''):
    # mark the current node as processed
    processed[i][j] = True
 
    # update the path with the current character and insert it into the set
    path += board[i][j]
 
    # check whether the path is present in the input set
    if path in words:
        result.add(path)
 
    # check for all eight possible movements from the current cell
    for k in range(len(row)):
        # skip if a cell is invalid, or it is already processed
        if isSafe(i + row[k], j + col[k], processed):
            searchBoggle(board, words, result, processed, i + row[k], j + col[k], path)
 
    # backtrack: mark the current node as unprocessed
    processed[i][j] = False
 
 
def searchInBoggle(board, words):
 
    # construct a set to store valid words constructed from the boggle
    result = set()
 
    # base case
    if not board or not len(board):
        return
 
    # `M × N` board
    (M, N) = (len(board), len(board[0]))
 
    # construct a boolean matrix to store whether a cell is processed or not
    processed = [[False for x in range(N)] for y in range(M)]
 
    # generate all possible words in a boggle
    for i in range(M):
        for j in range(N):
            # consider each character as a starting point and run DFS
            searchBoggle(board, words, result, processed, i, j)
 
    return result
 
 
if __name__ == '__main__':
 
    board = [
        ['M', 'S', 'E'],
        ['R', 'A', 'T'],
        ['L', 'O', 'N']
    ]
    
    board1 = [
        ['M', 'S', 'E', 'F'],
        ['R', 'A', 'T', 'D'],
        ['L', 'O', 'N', 'E'],
        ['K', 'A', 'F', 'B']
    ]
 
    words = ['STAR', 'NOTE', 'SAND', 'STONE']
 
    validWords = searchInBoggle(board, words)
    print(validWords)

def create_board(size : int=3):
    return [["_" for i in range(size)]for i in range(size)]

def split_board(board):

    return "\n".join([" ".join(i) for i in board])

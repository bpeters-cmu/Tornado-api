
class Game:
    in_progress = 'In Progress'
    draw = 'Draw'
    win = ' Wins'

    def __init__(self,id, player1, player2, board, status, move):
        self.id = id
        self.player1 = player1
        self.player2 = player2
        self.board = board
        self.status = status
        self.move = move

    def update_game(self, board):
        self.board = board
        self.move += 1
        if(Game.check_status(self.board, 1)):
            self.status = self.player1 + Game.win
        elif(Game.check_status(self.board, 0)):
            self.status = self.player1 + Game.win
        elif(None in self.board):
            self.status = Game.draw
        else:
            self.status = Game.in_progress

    def to_json(self):
        return {
            'id': self.id,
            'player1': self.player1,
            'player2': self.player2,
            'board': self.board,
            'move': self.move,
            'status': self.status
        }

    @staticmethod
    def check_status(board, xo):
        if board[0] == xo and board[1] == xo and board[2] == xo:
            return True
        if board[3] == xo and board[4] == xo and board[5] == xo:
            return True
        if board[6] == xo and board[7] == xo and board[8] == xo:
            return True
        if board[2] == xo and board[5] == xo and board[8] == xo:
            return True
        if board[1] == xo and board[4] == xo and board[7] == xo:
            return True
        if board[0] == xo and board[4] == xo and board[8] == xo:
            return True
        if board[2] == xo and board[4] == xo and board[6] == xo:
            return True
        return False

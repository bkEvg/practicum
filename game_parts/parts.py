
class Board:
    """Class describes a gaming field """
    board_size = 3

    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
   
    def __str__(self):
        return (
            'Объект игрового поля размером ',
            f'{self.board_size}x {self.board_size}'
        )

    def make_move(self, row, col, player):
        self.board[row][col] = player

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

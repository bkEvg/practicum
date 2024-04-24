
class Board:
    """Класс описывающий концепцию игры крестики-нолики """
    board_size = 3

    def __init__(self):
        """Init метод"""
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
   
    def __str__(self):
        """Представление класса в строке"""
        return (
            'Объект игрового поля размером ',
            f'{self.board_size}x {self.board_size}'
        )

    def make_move(self, row, col, player):
        """ Функция размещает ход на доске"""
        self.board[row][col] = player

    # def display(self):
    #     """Функция отображает игровое поле, функция для консольной игры"""
    #     for row in self.board:
    #         print('|'.join(row))
    #         print('-' * 5)
    
    def is_board_full(self) -> bool:
        """ Проверка циклом, если ли у нас пустые клетки"""
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board[i][j] == ' ':
                    return False
        return True
    
    def check_win(self, player) -> bool:
        """Проверка победы """ 

        for i in range(3):
            # Проверка по горизонту и вертикали
            if (all(self.board[i][j] == player for j in range(3))) \
                or (all(self.board[j][i] == player for j in range(3))):
                return True
        # Проверка по главной и побочной вертикали
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] == player \
                or self.board[0][2] == self.board[1][1] == self.board[2][0] == player):
            return True
        return False

    def write_results(self, string: str):
        with open("results.txt", 'a') as data:
            data.write(string + '\n')

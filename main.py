from game_parts import Board
from game_parts.exceptions import FieldIndexError, CellOccupiedError


def main():
    game = Board()
    game.display()
    current_player = 'X'
    is_running = True

    # Тут пользователь вводит координаты ячейки.
    while is_running:
        print(f"Ход делают: {current_player}")
        while True:
            try:
                row = int(input('Введите номер строки: '))
                column = int(input('Введите номер столбца: '))
                if (row < 0 or row >= game.board_size) or \
                (column < 0 or column >= game.board_size):
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    raise CellOccupiedError
            except FieldIndexError:
                print(f"Введите координаты в диапозоне: Х (0-\
                    {game.board_size - 1}) Y (0-{game.board_size - 1})")
                continue
            except ValueError:
                print("Принимаются только положительные целочисленные цифры")
                print("Введите значения заново")
                continue
            except CellOccupiedError:
                print('Ячейка занята, выбери другую.')
            except Exception as e:
                print(f"Возникла ошибка: {e}")
            else:
                break
        
        # В метод make_move передаются те координаты, которые ввёл пользователь.
        game.make_move(row, column, current_player)
        print('Ход сделан!')
        game.display()
        if game.check_win(current_player):
            print(f"ИГРОК {current_player} ПОБЕДИЛ")
            is_running = False
        if game.is_board_full():
            print("НИЧЬЯ")
            is_running = False
        current_player = '0' if current_player == "X" else "X"

if __name__ == '__main__':
    main()


from game_parts import Board
import pygame


pygame.init()

# Константы
CELL_SIZE = 100
BOARD_SIZE = 3
WIDTH = HEIGHT = CELL_SIZE * BOARD_SIZE
LINE_WIDTH = 15
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
X_COLOR = (84, 84, 84)
O_COLOR = (242, 235, 211)
X_WIDTH = 15
O_WIDTH = 15
SPACE = CELL_SIZE // 4

# Настройки экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Крестики-Нолики')
screen.fill(BG_COLOR)


# Отрисовка сетки для игры 3х3
def draw_lines():

    # Горизонтальные линии
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, CELL_SIZE * i),
            (WIDTH, CELL_SIZE * i),
            LINE_WIDTH
        )

    # Вертикальные линии
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (i * CELL_SIZE, 0),
            (i * CELL_SIZE, HEIGHT),
            LINE_WIDTH
        )


# Отрисовка крестиков и ноликов 
def draw_figures(board:list) -> None:
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 'X':
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (col * CELL_SIZE + SPACE, row * CELL_SIZE + SPACE),
                    (col * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE),
                    X_WIDTH
                )
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (
                        col * CELL_SIZE + SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE
                    ),
                    (
                        col * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + SPACE
                    ),
                    X_WIDTH
                )
            elif board[row][col] == "O":
                pygame.draw.circle(
                    screen,
                    O_COLOR,
                    (
                        col * CELL_SIZE + CELL_SIZE // 2,
                        row * CELL_SIZE + CELL_SIZE // 2
                    ),
                    CELL_SIZE // 2 - SPACE,
                    O_WIDTH
                )


def main():
    game = Board()
    current_player = 'X'
    is_running = True
    draw_lines()
    
    while is_running:
        for event in pygame.event.get():

            # Обработка закрытия окна
            if event.type == pygame.QUIT:
                is_running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x = event.pos[1]
                mouse_y = event.pos[0]
                
                clicked_row = mouse_x // CELL_SIZE
                clicked_col = mouse_y // CELL_SIZE
                if game.board[clicked_row][clicked_col] == ' ':
                    game.make_move(clicked_row, clicked_col, current_player)
                    if game.check_win(current_player):
                        game.write_results(f'ПОБЕДИЛ {current_player}')
                        is_running = False
                    elif game.is_board_full():
                        game.write_results(f"МИР дружба ЖВАЧКА")
                        is_running = False
                    current_player = "O" if current_player == "X" else "X"
                    draw_figures(game.board)
        pygame.display.update()
    pygame.quit()
                


if __name__ == '__main__':
    main()

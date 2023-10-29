# Контекст
# Вероятнее всего, вы с детства знакомы с этой игрой. Пришло
# время реализовать её. Два игрока по очереди ставят крестики
# и нолики на игровое поле. Игра завершается когда кто-то
# победил, либо наступила ничья, либо игроки отказались
# играть.
# ● Задача
# Написать игру в “Крестики-нолики”. Можете использовать
# любые парадигмы, которые посчитаете наиболее
# подходящими. Можете реализовать доску как угодно - как
# одномерный массив или двумерный массив (массив массивов).
# Можете использовать как правила, так и хардкод, на своё
# усмотрение. Главное, чтобы в игру можно было поиграть через
# терминал с вашего компьютера.


class X_and_o:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"

    def display_board(self):
        for i in range(0, 9, 3):
            print(self.board[i], "|", self.board[i + 1], "|", self.board[i + 2])

    def move(self, position):

        if self.board[position] == " ":
            self.board[position] = self.current_player
            self.current_player = "X" if self.current_player == "0" else "0"

    def check_win(self):
        win_conditions = [(0, 1, 2),
                          (3, 4, 5),
                          (6, 7, 8),
                          (0, 3, 6),
                          (1, 4, 7),
                          (2, 5, 8),
                          (0, 4, 8),
                          (2, 4, 6)]
        for conditions in win_conditions:
            if self.board[conditions[0]] == self.board[conditions[1]] == self.board[conditions[2]] != " ":
                return self.board[conditions[0]]
            if " " not in self.board:
                return "Ничья"
        return None

    def game(self):
        while True:
            self.display_board()
            position = int(input("ВВедите номер клетки от 0 до 8: "))
            self.move(position)
            result = self.check_win()
            if result:
                if result == "Ничья":
                    print("Ничья")
                else:
                    print("Игрок ", result, "победил!!!")
                break


if __name__ == "__main__":
    game = X_and_o()
    game.game()

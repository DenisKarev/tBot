class TicTac:
    def board(self):
        temp = ''
        for i in self.tic_tac_toe_board:
            temp += ''.join(i) + '\n'
        return temp

    def __init__(self):
        self.player = 'X'
        self.em = 'Некорректный ввод!'
        self.fu = 'Позиция уже занята!'
        self.draw = 'Поздравляем! Боевая ничья!'
        self.tttrules = """Игра Крестики-нолики: для двух игроков последовательно ставящих \
на поле X для первого или O для второго игрока.
Выигрывает игрок первым составивший три своих знака по прямой или диагонали. Игра заканчиватеся когда \
заполнены все поля. Если все поля заполнены а выигравшего нет присуждается ничья."""

# Первый ход за игроком X """
        self.fieldd = [0, 0, 0,                       # digital(int) representation of player moves
                       0, 0, 0,
                       0, 0, 0]
        self.fd = [' ', ' ', ' ',                       # digital(int) representation of player moves
                   ' ', ' ', ' ',
                   ' ', ' ', ' ']
        self.winning_moves = [[0, 1, 2],                # [0, 1, 2]
                              [3, 4, 5],                 # [3, 4, 5]
                              [6, 7, 8],                 # [6, 7, 8]
                              [0, 3, 6],
                              [1, 4, 7],
                              [2, 5, 8],
                              [0, 4, 8], [2, 4, 6]]      # diagonals
        self.possible_moves = [1 for _ in range(9)]
        self.tic_tac_toe_board = [[' ', ' ', ' '],
                                  [' ', ' ', ' '],
                                  [' ', ' ', ' ']]
        # self.tic_tac_toe_board = [[' ¹', ' │ ', ' ²', ' │ ', ' ³'],
        #                           ['──', '─┼─', '──', '─┼─', '───'],
        #                           [' ⁴', ' │ ', ' ⁵', ' │ ', ' ⁶'],
        #                           ['──', '─┼─', '──', '─┼─', '───'],
        #                           [' ⁷', ' │ ', ' ⁸', ' │ ', ' ⁹']]
        # self.tic_tac_toe_board = [[' \u00b9', ' │ ', ' \u00b2', ' │ ', ' \u00b3'],
        #                           ['──', '─┼─', '──', '─┼─', '───'],
        #                           [' \u2074', ' │ ', ' \u2075', ' │ ', ' \u2076'],
        #                           ['──', '─┼─', '──', '─┼─', '───'],
        #                           [' \u2077', ' │ ', ' \u2078', ' │ ', ' \u2079']]
        self.pos_dict = {0: [0, 0, '¹'], 1: [0, 2, '²'], 2: [0, 4, '³'],
                         3: [2, 0, '⁴'], 4: [2, 2, '⁵'], 5: [2, 4, '⁶'],
                         6: [4, 0, '⁷'], 7: [4, 2, '⁸'], 8: [4, 4, '⁹']
                         }

    def cplayer(self):
        self.player = 'O' if self.player == 'X' else 'X'

    def finished(self):
        for lines in self.winning_moves:
            if self.fieldd[lines[0]] + self.fieldd[lines[1]] + self.fieldd[lines[2]] == 30:
                return 'X'
            elif self.fieldd[lines[0]] + self.fieldd[lines[1]] + self.fieldd[lines[2]] == 3:
                return 'O'
        return False

    def move(self, p: int):
        t = self.pos_dict[p]
        # self.tic_tac_toe_board[t[0]][t[1]] = self.tic_tac_toe_board[t[0]][t[1]].replace(t[2], self.player)
        self.fd[p] = self.player
        if self.player == 'X':
            self.fieldd[p] = 10
        else:
            self.fieldd[p] = 1

    # def rules(self):
    #     return self.tttrules

    def pmove(self):
        return f'Ход игрока  {self.player} '

    def win(self):
        return f'Поздравляем {self.player} вы победили!'


game = TicTac()
# print(game.rules())


# playing = True
# while playing:
#     print(game)
#     print(game.pmove())
#     pos = input(f'Введите номер позиции: ')
#     if pos.isdecimal():
#         if int(pos) > 0 and int(pos) < 10:
#             pos = int(pos)-1
#             if game.possible_moves[pos]:
#                 game.possible_moves[pos] = 0
#                 game.move(pos)
#                 if game.finished() or sum(game.possible_moves) == 0:
#                     playing = False
#                 else:
#                     game.cplayer()
#             else:
#                 print(game.fu)
#         else:
#             print(game.em)
#     else:
#         print(game.em)

# print(game)
# winner = game.finished()
# if winner:
#     print(game.win())
# else:
#     print(game.draw)
# print(game.board())
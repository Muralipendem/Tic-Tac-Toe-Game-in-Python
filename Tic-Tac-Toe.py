squares = [' ']*9
choose = 'XO'
chart = '''
  0   1   2
  {0} | {1} | {2}
 -----------
3 {3} | {4} | {5} 5
 -----------
  {6} | {7} | {8}
  6   7   8
'''
win_chances = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8), # horizontals
    (0, 3, 6), (1, 4, 7), (2, 5, 8), # verticals
    (0, 4, 8), (2, 4, 6)             # diagonals
]

def check_win(player):
    for a, b, c in win_chances:
        if {squares[a], squares[b], squares[c]} == {player}:
            return True

while True:
    print(chart.format(*squares))
    if check_win(choose[1]):
        print(f'{choose[1]} is the winner')
        break
    if ' ' not in squares:
        print('Draw')
        break
    move = int(input(f'{choose[0]} to move [0-8] place > '))
    if not 0 <= int(move) <= 8 or squares[move] != ' ':
        print('Invalid move!')
        continue
    squares.pop(move)
    squares.insert(move,choose[0])
    choose=choose[::-1]
'''Let's play! You have to return which player won! In case of a draw return Draw!.

Examples:

rps('scissors','paper') // Player 1 won!
rps('scissors','rock') // Player 2 won!
rps('paper','paper') // Draw!'''

def rps(p1, p2):
    tmp_dict = {'scissors': 2, 'paper': 1, 'rock': 3}

    if p1 == p2:
        return 'Draw!'

    if p1 == 'paper' and p2 == 'rock':
        return 'Player 1 won!'
    elif p1 == 'rock' and p2 == 'paper':
        return 'Player 2 won!'

    if tmp_dict[p1] > tmp_dict[p2]:
        return 'Player 1 won!'
    elif tmp_dict[p1] < tmp_dict[p2]:
        return 'Player 2 won!'


Test.describe('rock paper scissors')
Test.it('player 1 win')
Test.assert_equals(rps('rock', 'scissors'), "Player 1 won!")
Test.assert_equals(rps('scissors', 'paper'), "Player 1 won!")
Test.assert_equals(rps('paper', 'rock'), "Player 1 won!")

Test.it('player 2 win')
Test.assert_equals(rps('scissors', 'rock'), "Player 2 won!")
Test.assert_equals(rps('paper', 'scissors'), "Player 2 won!")
Test.assert_equals(rps('rock', 'paper'), "Player 2 won!")

Test.it('draw')
Test.assert_equals(rps('rock', 'rock'), 'Draw!')
Test.assert_equals(rps('scissors', 'scissors'), 'Draw!')
Test.assert_equals(rps('paper', 'paper'), 'Draw!')

'''
Other people's solutions:

1.
def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"

2.
def rps(p1, p2):
    hand = {'rock':0, 'paper':1, 'scissors':2}
    results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    return results[hand[p1] - hand[p2]]
    
3.
rps = lambda a, b: ['Draw!', 'Player 1 won!', 'Player 2 won!'][('srp'.index(a[0]) - 'srp'.index(b[0])) % 3]
'''
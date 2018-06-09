lottery_players = {
        'name': 'derek',
        'numbers': (13, 14, 15, 16, 17)
    }


class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = ( 34, 42, 12, 65, 23, 54, 23)

    def total(self):
        return sum(self.numbers)

player_one = LotteryPlayer('Derek')
player_two = LotteryPlayer('Ben')

print(player_one.name)
print(player_one.total())
print(player_two.name)
print(player_two.total())

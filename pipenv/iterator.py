class lineup:

    def __init__(self, coolPLayers):
        self.coolPLayers = coolPLayers

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < (len(self.coolPLayers) -1):
            player = self.coolPLayers[self.n]
            self.n += 1
            return player
## This is a test
astros = [
 'Springer',
 'Bregman',
 'Altuve',
 'Correa',
 'Reddick',
 'Gonzalez',
 'McCann',
 'Davis',
 'Tucker'
]

astros_lineup = lineup(astros)
process = iter(astros_lineup)

print(next(process))
print(next(process))

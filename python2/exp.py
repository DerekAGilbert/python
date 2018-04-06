class Invoice:


    def __init__(self, client, total):
        self.client = client
        self.total = total

    def formatter(self):
        f'{self.client} owes: ${self.total}'

# setters and getters

google = Invoice('Google', 100)

print(google.client)

google.client = 'Yahoo'

print(google.client)

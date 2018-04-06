class Invoice:

    def __init__(self, client, total):
        self.client = client
        self.total = total

    def __str__(self):
        return f'Invoice from {self.client} for {self.total}'

inv = Invoice('google', 550)
print(str(inv))

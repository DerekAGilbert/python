class User:
    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def greeting(self):
        return f'Hi {self.first_name} {self.last_name}'

class AdminUser(User):
    def active_users(Self):
        return '500'

derek = AdminUser('derek@gmail.com', 'derek', 'gilbert')

ashlyn = User('ashlyn@gmail.com', 'ashlyn', 'gilbert')

print(derek.active_users())
print(derek.greeting())
# does not inherit
print(ashlyn.active_users())

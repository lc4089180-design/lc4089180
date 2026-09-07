#Given this code snippet: class User: def __init__(self, name): self.name = name def greet(self): print('Hi' + self.name) user1 = User('Amit') user1.greet() — Fix the code so that it prints 'Hi Amit' (with a space) instead of 'HiAmit'.
class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hi " + self.name)


user1 = User("Amit")
user1.greet()
class Cat:
    def __init__(self, name, type, color, age, catMeow, catRun, catWalk):
        self.name = name
        self.type = type
        self.color = color
        self.age = age
        self.catMeow = catMeow
        self.catRun = catRun
        self.catWalk = catWalk

    def run(self):
        return f'I can run: {self.catRun}'
    
    def walk(self):
        return f'I can Walk: {self.catWalk}'
    


cat1 = Cat('Meshw', 'shras', 'black', '6 Months', 'Meow', '20 staps/second', '3 staps/second')

print(cat1)
print(cat1.run())
print(cat1.walk())
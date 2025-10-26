class Person:
    def __init__(self, name, age, sex, location):
        self.name = name
        self.age = age
        self.sex = sex
        self.location = location

    def greeting(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old. I am a {self.sex} and live in {self.location}. Nice to meet you!")

Jimmy = Person("Jimmy", 34, "male", "Göteborg")

Jimmy.greeting()
class programmer:
    company = "Microsoft"
    def __init__(self, name, salary, language, pin):
       self.name = name
       self.salary = salary
       self.language = language
       self.pin = pin

p = programmer("krish", "Python", 13000000, 800020)
print(p.name, p.language, p.salary, p.pin)

r = programmer("Radha", "javascript", 6400000, 801508)
print(r.name, r.language, r.salary, r.pin)
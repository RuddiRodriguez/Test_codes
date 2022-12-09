class Country:
    def __init__(self, info):
        self.info = info

    def __getitem__(self, key):
        return self.info[key]


france = Country({
    "Name": "France",
    "Population": 66_991_000 ,
    "Capital": "Paris",})

name = france["Name"]
# name is "France"
population = france["Population"]
# population is 66991000
capital = france["Capital"]

print(f'{name=}')
print(f'{population=}')
print(f'{capital=}')


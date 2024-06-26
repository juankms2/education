# OOP in python
class Cat:
  species = 'mammal'

  def __init__(self, name, age):  # Constructor
    self.name = name
    self.age = age

def findOldestCat(cats):
  oldest = None
  for cat in cats:
    if oldest is None or cat.age > oldest.age:
      oldest = cat

  return oldest.name


cat1 = Cat('Tom', 3)
cat2 = Cat('Tommy', 5)
cat3 = Cat('Tomas', 1)

# Exercise 1
# print(findOldestCat([cat1, cat2, cat3]))

###################################################################################
class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

# !!! class Simon extends Cat
class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# Exercise 2
#1 Add nother Cat
caty = Cat('Catty', 2)

#2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = [caty, Simon('Simon', 1), Sally('Sally', 2)]

#3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)

#4 Output all of the cats walking using the my_pets instance
# my_pets.walk()


# Exercise 3
class SuperList(list):
  def __len__(self):
    return 100
  
super_list = SuperList()
super_list.append(10)
super_list.append(20)

print(super_list)
print(super_list[0])
print(len(super_list))

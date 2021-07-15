#Creatin the baseclass animals
class Animal:
    def __init__(self, name, year_discovered):
        self.name = name
        self.year_discovered = year_discovered
    
    def __repr__(self):
        return f"Name: {self.name}, Year Discovered {self.year_discovered}"

    def __srt__(self):
        return f"Animal:{self.name} discovered: {self.year_discovered}" # Step 2: Create a Mamal class that inherits from your Animal base class X be sure to create the class variables move, breathe and reproduce and assign
        
# Creating subclasses for each: Mamals, Birds, and Fishes
class Mamal(Animal):
    def __init__(self, name, year_discovered):
        super().__init__(name, year_discovered)
        _move = 'walk'
        _breath = 'lungs'
        _reproduce = 'live birth'
        self.move = _move
        self.breath = _breath
        self.reproduce = _reproduce
    
    def move_type(self):
        return f"Move: {self.move}"

    def breath_type(self):
        return f"Breathe: {self.breath}"

    def repo_type(self):
        return f"Reproduces: {self.reproduce}"

class Bird(Animal):
    def __init__(self, name, year_discovered):
        super().__init__(name, year_discovered)
        _move = 'fly'
        _breath = 'lungs'
        _reproduce = 'eggs'
        self.move =  _move
        self.breath = _breath
        self.reproduce = _reproduce

    def move_type(self):
        return f"Move: {self.move}"

    def breath_type(self):
        return f"Breathe: {self.breath}"

    def repo_type(self):
        return f"Reproduces: {self.reproduce}"

class Fish(Animal):
    def __init__(self, name, year_discovered):
        super().__init__(name, year_discovered)
        _move = 'swim'
        _breath = 'gills'
        _reproduce = 'eggs'
        self.move = _move
        self.breath = _breath
        self.reproduce = _reproduce

    def move_type(self):
        return f"Move: {self.move}"

    def breath_type(self):
        return f"Breathe: {self.breath}"

    def repo_type(self):
        return f"Reproduces: {self.reproduce}"


def main():
    mamals_list = [
        {"name": "Panda", "year": 1869},
        {"name": "Zebra", "year": 1778},
        {"name": "Koala", "year": 1816},
        {"name": "Sloth", "year": 1804},
        {"name": "Armadillo", "year": 1758},
        {"name": "Raccoon", "year": 1758},
        {"name": "BigFoot", "year": 2021},
    ]


    birds_list = [
        {"name": "Pigeon", "year": 1837},
        {"name": "Peacock", "year": 1821},
        {"name": "Toucan", "year": 1758},
        {"name": "Parrot", "year": 1824},
        {"name": "Swan", "year": 1758},
    ]

    fishes_list = [
        {"name": "Salmon", "year": 1758},
        {"name": "Catfish", "year": 1817},
        {"name": "Perch", "year": 1758},
    ]

    animals = []

    # Using the [*args] we can take each of the dictionaries inside the list and append
    # each on in the animals list, and with the ".values()" the data inside the dictionary
    # previously extracted from the list is stored inside each requirement inside the Class __init__ function.
    for mamal in mamals_list:
        obj = Mamal(*mamal.values()) 
        animals.append(obj) 
    
    for bird in birds_list:
        obj = Bird(*bird.values())
        animals.append(obj)

    for fish in fishes_list:
        obj = Fish(*fish.values())
        animals.append(obj)
    

    # Sort by the desired value.
    sorted_animals = None
    year_S   = lambda animal: animal.year_discovered 
    name_S   = lambda animal: animal.name 
    move_S   = lambda animal: animal.move 
    lung_S   = lambda animal: animal.breath


    # Output:
    print("=== List all the animals in descending order by year named ===")
    sorted_animals = sorted(animals, key=year_S, reverse=True)
    for animal in sorted_animals:
        print("{ name:", animal.name + ",", "year_discovered:", animal.year_discovered, "}") 

    print("\n\n=== List all the animals alphabetically ===")
    sorted_animals = sorted(animals, key=name_S)
    for animal in sorted_animals:
        print("{ name:", animal.name, "}")
    
    print("\n\n=== List all the animals order by how they move ===")
    sorted_animals = sorted(animals, key=move_S)
    for animal in sorted_animals:
        print("{ name:", animal.name + ",", "move:", animal.move, "}")
    
    print("\n\n=== List only those animals the breath with lungs ===")
    sorted_animals = sorted(animals, key=lung_S)
    for animal in sorted_animals:
        if animal.breath == "lungs":
            print("{ name:", animal.name + ",", "breath:", animal.breath, "}")

    print(
        "\n\n=== List only those animals that breath with lungs and were named in 1758 ==="
    )

    print("\n\n=== List only those animals that lay eggs and breath with lungs ===")

    print("\n\n=== List alphabetically only those animals that were named in 1758 ===")


if __name__ == "__main__":
    main()

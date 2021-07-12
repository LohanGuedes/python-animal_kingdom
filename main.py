class Animal:
    def __init__(self, name, year_discovered):
        self.name = name
        self.year_discovered = year_discovered
    
    def __repr__(self):
        return f"Name: {self.name} - Year Discovered {self.year_discovered}"

    def __srt__(self):
        return f"Animal:{self.name} discovered: {self.year_discovered}" # Step 2: Create a Mamal class that inherits from your Animal base class X be sure to create the class variables move, breathe and reproduce and assign
        
class Mamal(Animal):
    def __init__(self, name, year_discovered, move='walk', breath='lungs', reproduce='live births'):
        super().__init__(name, year_discovered)
        self.move = move
        self.breath = breath
        self.reproduce = reproduce
    
    def move_type(self):
        return f"Move: {self.move}"

    def breath_type(self):
        return f"Breathe: {self.breath}"

    def repo_type(self):
        return f"Reproduces: {self.reproduce}"

class Bird(Animal):
    def __init__(self, name, year_discovered, move='fly', breath='lungs', reproduce='eggs'):
        super().__init__(name, year_discovered)
        self.move = move
        self.breath = breath
        self.reproduce = reproduce

    def move_type(self):
        return f"Move: {self.move}"

    def breath_type(self):
        return f"Breathe: {self.breath}"

    def repo_type(self):
        return f"Reproduces: {self.reproduce}"

class Fish(Animal):
    def __init__(self, name, year_discovered, move='swim', breath='gills', reproduce='eggs'):
        super().__init__(name, year_discovered)
        self.move = move
        self.breath = breath
        self.reproduce = reproduce

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

    # Step 5: loop through the list's above, and add each object created to the **animals** list
    animals = []
    for mamal in mamals_list:
        for 
    
    # Step 6: Solve the requirements below....
    # HINT: Be sure to create new lists when sorting 
    # and NOT altering a list in place. Assign the result to the **sorted_animals** list
    # 
    # https://stackoverflow.com/questions/403421/how-to-sort-a-list-of-objects-based-on-an-attribute-of-the-objects

    sorted_animals = None
    print("=== List all the animals in descending order by year named ===")

    print("\n\n=== List all the animals alphabetically ===")

    print("\n\n=== List all the animals order by how they move ===")

    print("\n\n=== List only those animals the breath with lungs ===")

    print(
        "\n\n=== List only those animals that breath with lungs and were named in 1758 ==="
    )

    print("\n\n=== List only those animals that lay eggs and breath with lungs ===")

    print("\n\n=== List alphabetically only those animals that were named in 1758 ===")


if __name__ == "__main__":
    # be sure to call your main method
    main()

class AnimalRegistry:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        
    def get_animal(self):
        return self.animals
        
    def list_commands(self, animal):
        return animal.get_commands()

    def teach_animal(self, animal, new_command):
        animal.add_command(new_command)

from AnimalRegistry import AnimalRegistry
from Counter import Counter
from Model.Cat import Cat
from Model.Dog import Dog
from Model.Hamster import Hamster


registry = AnimalRegistry()
counter = Counter()


while True:
    print(' Завести новое животное - 1',
    '\n Список команд - 2',
    '\n Обучить животное - 3',
    '\n Выход - 0')
    
    choice = input('>')
    
    if choice == '1':
        while True:
            species = input('Какое животное добавить:\n1 - Кошка\n2 - Собака\n3 - Хомяк\n0 - Возврат в основное меню\n>')
            if species == '1':
                name = input('Введите имя животного: ')
                try:
                    with counter:
                        if name:
                            new_cat = Cat(name) 
                            registry.add_animal(new_cat)
                            counter.add()
                            print(f"Животное {new_cat.name} успешно добавлено в реестр.\n")
                except ValueError as e:
                    print(e)
                    
            elif species == '2':
                name = input('Введите имя животного: ')
                try:
                    with counter:
                        if name:
                            new_dog = Dog(name) 
                            registry.add_animal(new_dog)
                            counter.add()
                            print(f"Животное {new_dog.name} успешно добавлено в реестр.\n")
                except ValueError as e:
                    print(e)
                    
            elif species == '3':
                name = input('Введите имя животного: ')
                try:
                    with counter:
                        if name:
                            new_hamster = Hamster(name) 
                            registry.add_animal(new_hamster)
                            counter.add()
                            print(f"Животное {new_hamster.name} успешно добавлено в реестр.\n")
                except ValueError as e:
                    print(e)
                    
            elif species == '0':
                break
            
    elif choice == '2':
            name = input("Введите имя животного: ")
            for animal in registry.animals:
                if animal.name == name:
                    commands = animal.get_commands()
                    if commands:
                        print(f"{animal.name} знает следующие команды: {', '.join(commands)}")
                    else:
                        print(f"{animal.name} не знает ни одной команды.")
                    break
            else:
                print("Животное не найдено в реестре.")
            
    elif choice == '3':
        name = input("Введите имя животного: ")
        for animal in registry.animals:
            if animal.name == name:
                command = input("Введите новую команду для животного: ")
                animal.add_command(command)
                print(f"{animal.name} успешно обучено новой команде.")
                break
            else:
                print("Животное не найдено в реестре.")
                
    else:
        break
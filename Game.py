import time
import random

def print_slowly(text, delay=0.015):
    if isinstance(text, list):
        for item in text:
            print_slowly(item, delay)
    else:
        for letter in str(text):
            print(letter, end='', flush=True)
            time.sleep(delay)
        print()

def start_game():
    print_slowly("Добро пожаловать в заброшенный город!")
    print_slowly("Вы просыпаетесь в разрушенном здании. Вокруг тишина и пустота.")
    print_slowly("Ваша задача - раскрыть секрет исчезновения жителей этого города.")
    input("Нажмите Enter, чтобы начать...")

def choose_action(actions):
    print_slowly("\nВыберите действие:")
    for i, action in enumerate(actions):
        print_slowly(f"{i + 1}. {action}")
    while True:
        try:
            choice = int(input("> "))
            if 1 <= choice <= len(actions):
                return choice - 1
            else:
                print_slowly("Введите число, соответствующее доступному действию.")
        except ValueError:
            print_slowly("Пожалуйста, введите число.")

def choose_items(items):
    print_slowly("Вы можете взять только определенные предметы. Выберите:")
    for i, item in enumerate(items):
        print(f"{i + 1}. {item}")
    chosen_items = []
    while True:
        try:
            choice = int(input("Введите номер предмета (0 для завершения выбора): "))
            if choice == 0:
                break
            elif 1 <= choice <= len(items):
                chosen_item = items[choice - 1]
                if chosen_item not in chosen_items:
                    chosen_items.append(chosen_item)
                    print_slowly(f"{chosen_item} добавлен в выбранные предметы.")
                else:
                    print_slowly("Вы уже выбрали этот предмет.")
            else:
                print_slowly("Введите число из списка.")
        except ValueError:
            print_slowly("Пожалуйста, введите номер.")
    return chosen_items

def level_1(inventory):
    print_slowly("\n=== Уровень 1: Пробуждение ===")
    print_slowly("Вы находитесь в центре города, вокруг разрушенные здания.")
    actions = ["Осмотреться", "Искать записку", "Проверить инвентарь"]
    level_complete = False

    while not level_complete:
        choice = choose_action(actions)

        if choice == 0:
            print_slowly("Вы видите несколько зданий. Некоторые из них можно исследовать.")
            time.sleep(1)
        elif choice == 1:
            print_slowly("Вы нашли записку с намеками на то, что произошло в городе.")
            print_slowly("Записка добавлена в инвентарь.")
            inventory.append("Записка")
        elif choice == 2:
            print_slowly("Инвентарь: " + ", ".join(inventory))  # Объединяем список в строку
            if "Записка" in inventory:
                print_slowly("В записке говорится: 'Ключи к разгадке скрыты в здании напротив.'")
                print_slowly("Вам нужно найти ключи, чтобы открыть ворота и перейти дальше.")
                level_complete = True

def level_2(inventory):
    print_slowly("\n=== Уровень 2: Тени прошлого ===")
    print_slowly("Вы добрались до центра города. Вокруг вас находятся важные здания.")
    items = ["Ключ", "Фонарик", "Лом"]
    puzzles_solved = set()
    level_complete = False

    while not level_complete:
        actions = ["Искать предметы", "Использовать терминалы", "Проверить инвентарь", "Пройти дальше"]
        choice = choose_action(actions)

        if choice == 0:
            print_slowly("Вы нашли несколько предметов.")
            chosen_items = choose_items(items)
            inventory.extend(chosen_items)
            print_slowly("Вы добавили выбранные предметы в инвентарь.")
        elif choice == 1:
            if "Ключ" in inventory:
                print_slowly("Вы активировали терминалы и узнали о таинственных экспериментах.")
                puzzles_solved.add("Терминалы активированы")
            else:
                print_slowly("Терминалы заблокированы. Найдите ключ.")
        elif choice == 2:
            print_slowly("Инвентарь: " + ", ".join(inventory))  # Объединяем список в строку
        elif choice == 3:
            if "Терминалы активированы" in puzzles_solved:
                print_slowly("Вы смогли открыть доступ к лабораториям.")
                level_complete = True
            else:
                print_slowly("Терминалы заблокированы. Вы не можете пройти дальше.")

def level_25(inventory):
    print_slowly("\n=== Уровень 2.5: Встреча с монстром ===")
    print_slowly("По пути в подземный бункер вы увидели монстра на дороге.")
    print_slowly("Что вы хотите сделать?")
    
    while True:
        actions = ["Прокрасться мимо", "Ударить ломом"]
        choice = choose_action(actions)

        if choice == 0:
            if random.choice([True, False]):
                print_slowly("Вам удалось прокрасться мимо монстра незамеченным!")
                break 
            else:
                print_slowly("Монстр заметил вас! Игра окончена.")
                exit()  
        elif choice == 1:
            if "Лом" in inventory:
                print_slowly("Вы ударили монстра ломом и одержали победу!")
                break  
            else:
                print_slowly("У вас нет лома. Монстр побеждает вас.")
                print_slowly("Игра окончена.")
                exit() 

def level_3(inventory):
    print_slowly("\n=== Уровень 3: Правда под завесой ===")
    print_slowly("Вы находитесь в подземном бункере, где хранится вся правда о проекте.")
    puzzles = {
        "Система охраны": "активна",
        "Главный сервер": "не взломан",
        "Энергия": "активна"
    }
    level_complete = False

    while not level_complete:
        actions = ["Взломать систему", "Проверить сервер", "Выключить энергию", "Проверить статус"]
        choice = choose_action(actions)

        if choice == 0:
            print_slowly("Вы успешно отключили систему охраны.")
            puzzles["Система охраны"] = "отключена"
        elif choice == 1:
            if puzzles["Система охраны"] == "отключена":
                print_slowly("Вы взломали главный сервер и получили доступ к закрытым данным.")
                puzzles["Главный сервер"] = "взломан"
            else:
                print_slowly("Система охраны активна. Сначала её нужно отключить, чтобы взломать сервер.")
        elif choice == 2:
            print_slowly("Энергия отключена.")
            puzzles["Энергия"] = "отключена"
        elif choice == 3:
            print_slowly("Статус систем:")
            for system, status in puzzles.items():
                print_slowly(f"{system}: {status}")
            if puzzles["Главный сервер"] == "взломан" and puzzles["Энергия"] == "отключена":
                print_slowly("Вы получили контроль над системой. Наступает момент выбора...")
                print_slowly("1. Уничтожить лаборатории и сбежать.")
                print_slowly("2. Попытаться восстановить систему и возродить технологии.")
                print_slowly("3. Ничего не делать, и дать всему самоуничтожиться.")
                final_choice = int(input("> "))

                if final_choice == 1:
                    print_slowly("Вы разрушили лаборатории и сбежали из города.")
                    print_slowly("Город останется погруженным в забвение.")
                elif final_choice == 2:
                    print_slowly("Вы пытаетесь восстановить технологии, но будущее остается неопределенным.")
                    print_slowly("Может ли прогресс исправить прошлые ошибки?")
                elif final_choice == 3:
                    print_slowly("Вы ничего не сделали, и город взорвался, уничтожив все остатки прошлого.")
                level_complete = True

def main():
    inventory = [] 
    start_game()
    level_1(inventory)
    level_2(inventory)
    level_25(inventory)
    level_3(inventory)
    print("\n=== Конец игры ===")
    print("Спасибо за игру!")

if __name__ == "__main__":
    main()
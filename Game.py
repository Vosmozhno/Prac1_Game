import time

def start_game():
    print("Добро пожаловать в заброшенный город!")
    print("Вы просыпаетесь в разрушенном здании. Вокруг тишина и пустота.")
    print("Ваша задача - раскрыть секрет исчезновения жителей этого города.")
    input("Нажмите Enter, чтобы начать...")

def choose_action(actions):
    print("\nВыберите действие:")
    for i, action in enumerate(actions):
        print(f"{i + 1}. {action}")
    choice = int(input("> "))
    return choice - 1

def level_1(inventory):
    print("\n=== Уровень 1: Пробуждение ===")
    print("Вы находитесь в центре города, вокруг разрушенные здания.")
    actions = ["Осмотреться", "Искать записку", "Проверить инвентарь"]
    level_complete = False

    while not level_complete:
        choice = choose_action(actions)

        if choice == 0:
            print("Вы видите несколько зданий. Некоторые из них можно исследовать.")
            time.sleep(1)
        elif choice == 1:
            print("Вы нашли записку с намеками на то, что произошло в городе.")
            print("Записка добавлена в инвентарь.")
            inventory.append("Записка")
        elif choice == 2:
            print("Инвентарь:", inventory)
            if "Записка" in inventory:
                print("В записке говорится: 'Ключи к разгадке скрыты в здании напротив.'")
                print("Вам нужно найти ключи, чтобы открыть ворота и перейти дальше.")
                level_complete = True

def level_2(inventory):
    print("\n=== Уровень 2: Тени прошлого ===")
    print("Вы добрались до центра города. Вокруг вас находятся важные здания.")
    items = ["Ключ", "Фонарик", "Лом"]
    puzzles_solved = set()
    level_complete = False

    while not level_complete:
        actions = ["Искать предметы", "Использовать терминалы", "Проверить инвентарь", "Пройти дальше"]
        choice = choose_action(actions)

        if choice == 0:
            print("Вы нашли предметы:", items)
            inventory.extend(items)
            print("Предметы добавлены в инвентарь.")
        elif choice == 1:
            if "Ключ" in inventory:
                print("Вы активировали терминалы и узнали о таинственных экспериментах.")
                puzzles_solved.add("Терминалы активированы")
            else:
                print("Терминалы заблокированы. Найдите ключ.")
        elif choice == 2:
            print("Инвентарь:", inventory)
        elif choice == 3:
            if "Терминалы активированы" in puzzles_solved:
                print("Вы смогли открыть доступ к лабораториям.")
                level_complete = True
            else:
                print("Терминалы заблокированы. Вы не можете пройти дальше.")

def level_3(inventory):
    print("\n=== Уровень 3: Правда под завесой ===")
    print("Вы находитесь в подземном бункере, где хранится вся правда о проекте.")
    puzzles = {
        "Система охраны": "отключена",
        "Главный сервер": "не взломан",
        "Энергия": "активна"
    }
    level_complete = False

    while not level_complete:
        actions = ["Взломать систему", "Проверить сервер", "Выключить энергию", "Проверить статус"]
        choice = choose_action(actions)

        if choice == 0:
            print("Вы успешно отключили систему охраны.")
            puzzles["Система охраны"] = "отключена"
        elif choice == 1:
            if puzzles["Система охраны"] == "отключена":
                print("Вы взломали главный сервер и получили доступ к закрытым данным.")
                puzzles["Главный сервер"] = "взломан"
            else:
                print("Система охраны мешает взлому. Отключите её сначала.")
        elif choice == 2:
            print("Энергия отключена.")
            puzzles["Энергия"] = "отключена"
        elif choice == 3:
            print("Статус систем:")
            for system, status in puzzles.items():
                print(f"{system}: {status}")
            if puzzles["Главный сервер"] == "взломан" and puzzles["Энергия"] == "отключена":
                print("Вы получили контроль над системой. Наступает момент выбора...")
                print("1. Уничтожить лаборатории и сбежать.")
                print("2. Попытаться восстановить систему и возродить технологии.")
                print("3. Ничего не делать, и дать всему самоуничтожиться.")
                final_choice = int(input("> "))

                if final_choice == 1:
                    print("Вы разрушили лаборатории и сбежали из города.")
                    print("Город останется погруженным в забвение.")
                elif final_choice == 2:
                    print("Вы пытаетесь восстановить технологии, но будущее остается неопределенным.")
                    print("Может ли прогресс исправить прошлые ошибки?")
                elif final_choice == 3:
                    print("Вы ничего не сделали, и город взорвался, уничтожив все остатки прошлого.")
                level_complete = True

def main():
    inventory = [] 
    start_game()
    level_1(inventory)
    level_2(inventory)
    level_3(inventory)
    print("\n=== Конец игры ===")
    print("Спасибо за игру!")

# Запуск игры
if __name__ == "__main__":
    main()
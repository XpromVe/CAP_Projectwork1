import random

def get_computer_choice():
    """Генерирует и возвращает случайный выбор компьютера"""
    choices = ['камень', 'ножницы', 'бумага']
    return random.choice(choices)


def determine_winner(player, computer):
    """
    Определяет победителя текущего раунда
    Возвращает: 'игрок' - победил игрок, 'компьютер' - победил компьютер, 'ничья' - равный результат
    """
    if player == computer:
        return 'ничья'
    
    # Проверяем победу игрока
    if (player == 'камень' and computer == 'ножницы') or \
       (player == 'ножницы' and computer == 'бумага') or \
       (player == 'бумага' and computer == 'камень'):
        return 'игрок'
    
    # В остальных случаях побеждает компьютер
    return 'компьютер'


def display_rules():
    """Отображает правила игры"""
    print("\n" + "="*60)
    print("        ДОБРО ПОЖАЛОВАТЬ В ИГРУ 'КАМЕНЬ-НОЖНИЦЫ-БУМАГА'")
    print("="*60)
    print("\nПРАВИЛА ИГРЫ:")
    print("  • Камень побеждает ножницы")
    print("  • Ножницы побеждают бумагу")
    print("  • Бумага побеждает камень")
    print("  • При одинаковом выборе очки не начисляются")
    print("  • Победитель - первый, кто наберёт 3 очка")
    print("\nВозможные варианты ввода: камень, ножницы, бумага")
    print("="*60 + "\n")


def main():
    """Основная логика игры"""
    display_rules()
    
    player_score = 0
    computer_score = 0
    
    while True:
        # Запрос выбора у игрока
        while True:
            player_choice = input("Ваш выбор (камень/ножницы/бумага): ").lower().strip()
            if player_choice in ['камень', 'ножницы', 'бумага']:
                break
            else:
                print("❌ Неверный ввод! Пожалуйста, введите: камень, ножницы или бумага")
        
        # Компьютер делает выбор
        computer_choice = get_computer_choice()
        
        # Определяем победителя раунда
        result = determine_winner(player_choice, computer_choice)
        
        # Выводим результаты раунда
        print("\n" + "-"*60)
        print(f"Вы выбрали: {player_choice}")
        print(f"Компьютер выбрал: {computer_choice}")
        
        if result == 'игрок':
            print("✓ Вы победили этот раунд!")
            player_score += 1
        elif result == 'компьютер':
            print("✗ Компьютер победил этот раунд!")
            computer_score += 1
        else:
            print("= Ничья! Очки не изменились.")
        
        # Показываем текущий счёт
        print(f"\n📊 Текущий счёт: Вы {player_score} - {computer_score} Компьютер")
        print("-"*60 + "\n")
        
        # Проверяем условие завершения игры
        if player_score == 3:
            print("="*60)
            print("🎉 ПОЗДРАВЛЯЕМ! ВЫ ПОБЕДИЛИ ИГРУ! 🎉")
            print(f"Финальный счёт: Вы {player_score} - {computer_score} Компьютер")
            print("="*60)
            break
        elif computer_score == 3:
            print("="*60)
            print("💻 КОМПЬЮТЕР победил! 💻")
            print(f"Финальный счёт: Вы {player_score} - {computer_score} Компьютер")
            print("="*60)
            break


if __name__ == "__main__":
    main()
def read_file(file_name):
    
    with open(file_name, 'r') as file:
        lines = file.readlines()
        
        # Ініціалізуємо результуючі рядки
        first_letters = ''
        second_letters = ''
        s_characters = ''
        
        # Проходимо по кожному рядку у файлі
        for line in lines:
            # Додаємо першу літеру до результуючого рядка (а)
            first_letters += line[0]
            
            # Додаємо другу літеру до результуючого рядка (б)
            second_letters += line[1]
            
            # Додаємо s-й символ до результуючого рядка (в)
            s_characters += line[2]
        
        # Виводимо результати
        print("(а) Слово, утворене першими літерами кожного рядка:", first_letters)
        print("(б) Слово, утворене другими літерами кожного рядка:", second_letters)
        print("(в) Послідовність символів, утворена s-ми символами кожного рядка:", s_characters)


# Приклад використання функції
file_name = "task2.txt"  
read_file(file_name)

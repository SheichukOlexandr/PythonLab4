# Відкриття файлу F1 для читання
with open('F1.txt', 'r') as f1:
    # Читання рядків файлу та розділення їх на числа
    numbers = [int(num) for num in f1.read().split()]

# Визначення від'ємних чисел на непарних позиціях
negative_odd_numbers = [num for i, num in enumerate(numbers) if num < 0 and i % 2 != 0]

# Запис від'ємних чисел на непарних позиціях у новий файл F2
with open('F2.txt', 'w') as f2:
    for num in negative_odd_numbers:
        f2.write(str(num) + '\n')

print("Готово! Перевірьте файл під назвою F2")
def count_vowels(text):
    vowels = 'аеёиоуыэюяaeiou'
    text_lower = text.lower()
    total_vowels = 0
    
    for char in text_lower:
        if char in vowels:
            total_vowels += 1
    
    return total_vowels


def main():
    """Основная функция программы."""
    print("Программа для подсчёта гласных букв")
    print("Поддерживаются русские и английские гласные")
    print("-" * 50)
    
    user_input = input("Введите слово или словосочетание: ").strip()
    
    if not user_input:
        print("Ошибка: Вы ввели пустую строку!")
        return
    
    total_vowels = count_vowels(user_input)
    print(f"Общее количество гласных: {total_vowels}")


if __name__ == "__main__":
    main()
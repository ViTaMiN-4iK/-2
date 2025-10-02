def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Тестирование
def test_binary_search():
    # Тестовые данные
    test_arrays = [
        [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],
        [2, 4, 6, 8, 10],
        [1],
        [],
        [1, 2, 3, 4, 5]
    ]
    
    test_cases = [
        # (массив, целевой элемент, ожидаемый результат)
        (test_arrays[0], 7, 3),
        (test_arrays[0], 1, 0),
        (test_arrays[0], 19, 9),
        (test_arrays[0], 8, -1),
        (test_arrays[1], 6, 2),
        (test_arrays[1], 1, -1),
        (test_arrays[2], 1, 0),
        (test_arrays[2], 2, -1),
        (test_arrays[3], 1, -1),
        (test_arrays[4], 3, 2)
    ]
    
    print("Тестирование бинарного поиска:")
    print("=" * 40)
    
    for i, (arr, target, expected) in enumerate(test_cases, 1):
        result = binary_search(arr, target)
        status = "✓" if result == expected else "✗"
        print(f"{status} Тест {i}: массив {arr}, target={target}")
        print(f"   Ожидалось: {expected}, Получено: {result}")
    
    # Демонстрация работы
    print("\n" + "=" * 40)
    print("Демонстрация поиска:")
    
    demo_arr = [2, 5, 8, 12, 16, 23, 38, 45, 67, 89]
    demo_targets = [23, 5, 100, 38]
    
    print(f"Массив: {demo_arr}")
    for target in demo_targets:
        result = binary_search(demo_arr, target)
        if result != -1:
            print(f"Элемент {target} найден на позиции {result}")
        else:
            print(f"Элемент {target} не найден")

# Запуск тестов
if __name__ == "__main__":
    test_binary_search()
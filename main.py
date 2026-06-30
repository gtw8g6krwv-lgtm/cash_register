from receipt_position import ReceiptPosition


def main():
    print("КАССОВЫЙ МОДУЛЬ МАГАЗИНА\n")
    product_name = input("Введите название товара: ")
    before_negative_minimal_number = 0
    price = None

    while price is None:
        try:
            price = int(input("Введите цену в копейках (например, 65 рублей = 6500 копеек): "))

            if price < before_negative_minimal_number:
                print("Цена не может быть отрицательной!")
                price = None

        except ValueError:
            print("Ошибка! Введите целое число.")

    quantity = None

    while quantity is None:
        try:
            quantity = int(input("Введите количество: "))

            if quantity < before_negative_minimal_number:
                print("Количество не может быть отрицательным!")
                quantity = None

        except ValueError:
            print("Ошибка! Введите целое число.")

    position = ReceiptPosition(product_name, price, quantity)

    print("\n=== ТОВАР СОЗДАН ===")
    print(f"Название: {position.get_name()}")
    print(f"Цена: {position.get_price()} копеек")
    print(f"Количество: {position.get_quantity()}")
    print(f"Общая стоимость: {position.total_cost()} копеек")

    first_menu_point = "1"
    second_menu_point = "2"
    third_menu_point = "3"

    is_program_active = True

    while is_program_active:
        print("\nМЕНЮ")
        print("1. Увеличить количество")
        print("2. Показать информацию о товаре")
        print("3. Выйти")

        user_choice = input(f"Выберите действие ({first_menu_point}-{third_menu_point}): ")

        if user_choice == first_menu_point:
            amount = None

            while amount is None:
                try:
                    amount = int(input("На сколько увеличить количество? "))

                    if amount <= before_negative_minimal_number:
                        print("Количество должно быть положительным!")
                        amount = None

                except ValueError:
                    print("Ошибка! Введите целое число.")

            position.increase_quantity(amount)
            print(f"Количество увеличено на {amount}")
            print(f"Теперь количество: {position.get_quantity()}")
            print(f"Общая стоимость: {position.total_cost()} копеек")

        elif user_choice == second_menu_point:
            print("\nИНФОРМАЦИЯ О ТОВАРЕ")
            print(f"Название: {position.get_name()}")
            print(f"Цена за единицу: {position.get_price()} копеек")
            print(f"Количество: {position.get_quantity()}")
            print(f"Общая стоимость: {position.total_cost()} копеек")

        elif user_choice == third_menu_point:
            print("До свидания!")
            is_program_active = False

        else:
            print("Неверный выбор! Попробуйте снова.")


if __name__ == "__main__":
    main()
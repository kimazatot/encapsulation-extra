# Создайте класс Terminal. Создайте объект-карточку от этого класса, передав номер своей карточки и пин код. При этом, необходимо проверить валидность карточки: номер карточки должен содержать строго 16 цифр, а пин код
# 4 цифры (для этого используйте инкапсуляцию). При создании карточки в ней содержится 0 сом. Далее в классе должны быть следующие методы:
# метод put, который будет принимать в качестве аргументов: пин код карточки, вторым аргументом
# сумму денег, которую вы хотите закинуть на эту карточку. Прежде, чем закидывать деньги, необходимо проверить введенный пин код на совпадение (используйте инкапсуляцию)
# метод get_money, который также принимает первым аргументом пин код, вторым аргументом
# сумму денег, которую вы хотите извлечь из карточки. Здесь также необходимо использовать валидацию: проверка пин кода + сумма денег должна быть округленной до десятичных чисел, типа 10, 100, 200, 5000 и т.д. (67, 899, 45.6
# невалидные данные). И только после проверки деньги извлекаются.
# Примените данные методы к своей карточке несколько раз и в конце выдайте, сколько денег на карточке. Примечание: нельзя извлечь сумму денег, если она больше, чем сумма денег на карточке; также нельзя вытащить пин код карточки (эти данные должны быть скрыты)


class Terminal:
    def __init__(self, card_number, pin_code):
        self.__card_number = self.__validate_card_number(card_number)
        self.__pin_code = self.__validate_pin_code(pin_code)
        self.__balance = 0

    def __validate_card_number(self, card_number):
        if len(str(card_number)) != 16:
            raise Exception("Invalid card-number")
        # return len(str(self.__card_number)) == 16
        else:
            return card_number
            
    def __validate_pin_code(self, pin_code):
        if len(str(pin_code)) != 4:
            raise Exception("Invalid pin-code")
        # return len(str(self.__pin_code)) == 4
        else:
            return pin_code

    def put(self, input_pin, amount):
        if input_pin != self.__pin_code:
            print("Неверный пин-код")
            return
        if input_pin != self.__pin_code:
            print("неверные данные карты")
            return
        self.__balance += amount

    def get_money(self, input_pin, amount):
        if input_pin != self.__pin_code:
            print("Неверный пин-код")
            return
        if amount % 10 != 0:
            print("Недопустимая сумма")
            return
        if amount > self.__balance:
            print("Недостаточно средств")
            return
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


my_card = Terminal(1234567890152356, 5555)
# my_card.put(5555, 1)
my_card.put(5555, 10)  
# my_card.get_money(5555, 700)
# my_card.get_money(5555, 5)
print(f"Balance: {my_card.get_balance()} som")



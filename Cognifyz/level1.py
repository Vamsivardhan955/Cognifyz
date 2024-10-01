class Level1:
    @staticmethod
    def reverse_string():
        """
        Task 1: String Reversal
        """
        input_string = input("Enter a string to reverse: ")
        reversed_string = input_string[::-1]
        print(reversed_string)

    @staticmethod
    def convert_temperature():
        """
        Task 2: Temperature Conversion
        """
        temperature_value = float(input("Enter temperature: "))
        temperature_unit = input("Enter unit (C/F): ").upper()
        if temperature_unit == "C":
            converted_temp = (temperature_value * 9 / 5) + 32
            print(f"{temperature_value}°C is {converted_temp}°F")
        elif temperature_unit == "F":
            converted_temp = (temperature_value - 32) * 5 / 9
            print(f"{temperature_value}°F is {converted_temp}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    @staticmethod
    def validate_email():
        """
        Task 3: Email Validator
        """
        import re
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        email_address = input("Enter email: ")
        print("Valid email" if re.match(email_pattern, email_address) else "Invalid email")

    @staticmethod
    def calculator():
        """
        Task 4: Calculator Program
        """
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /, %): ")
        if operator == "+":
            calculation_result = first_number + second_number
        elif operator == "-":
            calculation_result = first_number - second_number
        elif operator == "*":
            calculation_result = first_number * second_number
        elif operator == "/":
            if second_number != 0:
                calculation_result = first_number / second_number
            else:
                calculation_result = "Error! Division by zero."
        elif operator == "%":
            calculation_result = first_number % second_number
        else:
            calculation_result = "Invalid operator"
        print(f"Result: {calculation_result}")

    @staticmethod
    def is_palindrome():
        """
        Task 5: Palindrome Checker
        """
        input_string = input("Enter a string to check if it's a palindrome: ")
        print("Palindrome" if input_string == input_string[::-1] else "Not a palindrome")

print("TASK 1:")
Level1.reverse_string()
print()
print("TASK 2:")
Level1.convert_temperature()
print()
print("TASK 3:")
Level1.validate_email()
print()
print("TASK 4:")
Level1.calculator()
print()
print("TASK 5:")
Level1.is_palindrome()

# Conversion constants
KG_TO_LB = 2.20462
LB_TO_KG = 1 / KG_TO_LB

# Function for weight conversion
def convert_weight(value, source_unit, target_unit):
    if source_unit == 'kg' and target_unit == 'lb':
        return value * KG_TO_LB
    elif source_unit == 'lb' and target_unit == 'kg':
        return value * LB_TO_KG
    else:
        raise ValueError("Unsupported weight conversion. Use 'kg' for kilograms or 'lb' for pounds.")

# Function to handle user input
def get_user_input():
    try:
        value = float(input("Enter the weight : "))
        source_unit = input("Enter the source unit (kg/lb): ").lower()
        target_unit = input("Convert into (kg/lb): ").lower()
        return value, source_unit, target_unit
    except ValueError:
        raise ValueError("Invalid input. Please enter a numeric value.")

# Function to display the result
def display_result(value, source_unit, target_unit, result):
    print(f"{value} {source_unit} is equal to {result:.2f} {target_unit}.")

def main():
    print("Welcome to the Weight Converter!")
    
    while True:
        try:
            value, source_unit, target_unit = get_user_input()
            result = convert_weight(value, source_unit, target_unit)
            display_result(value, source_unit, target_unit, result)
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: e")

        # Ask if the user wants to start again
        restart = input("Do you want to convert another weight (yes/no)? ").lower()
        if restart != 'yes':
            break

if __name__ == "__main__":
    main()

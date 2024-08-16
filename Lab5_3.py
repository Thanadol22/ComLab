def generate_pattern(number):
    pattern = ""
    for i in range(1, number + 1):
        pattern += chr(64 + i) * i + "\n"
    return pattern
 
while True:
    user_input = input("Enter Number: ")
 
    if user_input.lower() == "exit":
        print("End Program!!!")
        break
 
    try:
        number = int(user_input)
        if 1 <= number <= 26:
            print(generate_pattern(number))
        else:
            print("Please Enter Number 1 - 26 ")
    except ValueError:
        print("Please Enter Number or 'exit' for close program ")
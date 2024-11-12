digits_led = [
    ['###', '# #', '# #', '# #', '###'],  # 0
    ['#  ', '#  ', '#  ', '#  ', '#  '],  # 1
    ['###', '  #', '###', '#  ', '###'],  # 2
    ['###', '  #', '###', '  #', '###'],  # 3
    ['# #', '# #', '###', '  #', '  #'],  # 4
    ['###', '#  ', '###', '  #', '###'],  # 5
    ['###', '#  ', '###', '# #', '###'],  # 6
    ['###', '  #', '  #', '  #', '  #'],  # 7
    ['###', '# #', '###', '# #', '###'],  # 8
    ['###', '# #', '###', '  #', '###']   # 9
]

def display_number(number: str):
    rows = ['', '', '', '', '']
    
    for digit in number:
        digit_pattern = digits_led[int(digit)]
        for i in range(5):
            rows[i] += digit_pattern[i] + " "  
            
    for row in rows:
        print(row)

while True:
    user_input = input('Enter a non-negative integer (or press Q/q to quit): ')

    if user_input.lower() == 'q':
        print("Goodbye!")
        break  

    if user_input.isdigit():
        display_number(user_input)
    else:
        print("Invalid input! Please enter a non-negative integer or Q/q to quit.")

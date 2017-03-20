import random
number_lines = int(input("How many quick picks?"))
count = 0
while count != number_lines:
    count += 1
    lotto_numbers = random.sample(range(1, 45), 6)
    print(lotto_numbers)





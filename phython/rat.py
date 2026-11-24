print("The Naija Love Calculator!")
first_name = input("What is your name? ")
second_name = input("What is your name? ")
red_first = first_name.lower()
red_second = second_name.lower()
comb_name = red_first + red_second
t_count = comb_name.count("t")
r_count = comb_name.count("r")
u_count = comb_name.count("u")
e_count = comb_name.count("e")
digit_1 = t_count + r_count + u_count + e_count
l_count = comb_name.count("l")
o_count = comb_name.count("o")
v_count = comb_name.count("v")
e_count = comb_name.count("e")
digit_2 = l_count + o_count + v_count + e_count
final_digits = str(digit_1) + str(digit_2)
score = int(final_digits)

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like Coke and Mentos (Premium Breakfast guaranteed!).")
elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together (Just dey play).")
else:
  print(f"Your score is {score}.")

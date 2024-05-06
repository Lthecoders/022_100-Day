import random

print("\033[34m",
      "--------------> One-Million-To-One challenge <--------------",
      "\033[0m")
print("\033[31m", "                ----------------------------", "\033[0m")
print(
    "\033[35m",
    "\n ********IMP------->you have to guess which number i had picked🤔 from-------> FROM THE MULTIPLES OF 100000🤔🤔 TILL 1000000 \n(table of 100000 till 10 times i.e = 1000000)<----------\n",
    "\033[0m",
)
attempts = 0
new_num = random.randrange(100000, 1000000, 100000)
# print(new_num)
while True:
  print(
      "\033[33m",
      "\n-------> you can put a negative number to exit <----------",
      "\033[0m",
  )
  attempts += 1

  guess_input = input("\nwhat is your guess --->  ")
  # isdigit is used to check if the input is a number or not
  if not guess_input.lstrip(
      '-').isdigit():  # lstrip is use to reamove - from the user input
    print(
        "\033[31m",
        "Please input an integer only.\n you cannot put an float or string or any other object ",
        "\033[0m")
    continue

  guess_number = int(guess_input)

  if int(guess_number) == new_num:
    print("\ncorrect !!!")
    if attempts == 1:
      print("\033[32m", "it took you ONLY", attempts,
            "guess to get it correct👍🥳", "\033[0m")
      print("\033[32m", "You are great in terms of guessing", "\033[0m")
      break
    elif attempts > 1 and attempts <= 3:
      print("\033[32m", "it took you", attempts, "guesses to get it correct👍🥳",
            "\033[0m")
      print("\033[32m", "You are great in terms of guessing", "\033[0m")
      break
    elif attempts > 3 and attempts <= 7:
      print("\033[36m", "it took you", attempts, "guesses to get it correct👍",
            "\033[0m")
      print("\033[36m", "You are ok in terms of guessing😏😏", "\033[0m")
      break
    elif attempts >= 8:
      print("\033[30m", "it took you", attempts, "guesses to get it correct👎",
            "\033[0m")
      print("\033[30m", "You are bad in terms of guessing😒😒", "\033[0m")
      break
  elif guess_number <= -1:  # guess number must be smaller that -1 to i.e -2,-3...-9999
    break
  elif guess_number < new_num:
    print("\nYour guess is low 📉")
  elif guess_number > new_num:
    print("\nYour guess is high 📈")

  else:
    print("\nYou cannot input a text")
print("\033[34m",
      "\n\n<-------------------thanks for playing------------------->",
      "\033[0m")

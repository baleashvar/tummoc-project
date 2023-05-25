def is_valid_credit_card_number(number):
  """
  Returns True if the given number is a valid credit card number, False otherwise.

  Args:
    number: The credit card number as a string.

  Returns:
    True if the number is valid, False otherwise.
  """

  # Check the length of the number.
  if len(number) not in (13, 15, 16):
    return False

  # Check the first digit.
  first_digit = int(number[0])
  if first_digit not in (4, 5, 6, 37):
    return False

  # Calculate the checksum.
  checksum = 0
  for i in range(len(number) - 1, -1, -1):
    digit = int(number[i])
    if i % 2 == 0:
      digit *= 2
      if digit > 9:
        digit -= 9
    checksum += digit

  # Return True if the checksum is divisible by 10.
  return checksum % 10 == 0



#_______main_________

# Prompt the user to enter a credit card number.
number = input("Enter a credit card number: ")

# Validate the number.
if is_valid_credit_card_number(number):
    print("The number is valid.")
else:
    print("The number is invalid.")


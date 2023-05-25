Python Logical Question 
1. Write a program that prompts the user to enter a credit card number as a long integer
and Display whether that card is valid or invalid.Credit card numbers follow certain
patterns.
A credit card number must have between 13 and 16 digits. It must start with:
• 4 for Visa cards (length 13)
• 5 for Master cards (length 13)
• 37 for American Express cards (length 16)
• 6 for Discover cards (length 15)
you can determine if a credit card number is (syntactically) valid as follows:
• Multiply every other digit by 2, starting with the number’s second-to-last digit,
and then add those products’ digits together.
• Add the sum to the sum of the digits that weren’t multiplied by 2.
• If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is
congruent to 0), the number is valid
• Eg. 4003600000000014. Multiply each of the underlined digits by 2:
1•2 + 0•2 + 0•2 + 0•2 + 0•2 + 6•2 + 0•2 + 4•2
That gives us:
2 + 0 + 0 + 0 + 0 + 12 + 0 + 8
Now let’s add those products’ digits (i.e., not the products themselves)
together:
2 + 0 + 0 + 0 + 0 + 1 + 2 + 0 + 8 = 13. Now let’s add that sum (13) to the sum
of the digits that weren’t multiplied by 2 (starting from the end):
13 + 4 + 0 + 0 + 0 + 0 + 0 + 3 + 0 = 20. The last digit in that sum (20) is a 0,
so the card is valid!

Output:
![ss1](https://github.com/baleashvar/tummoc-project/assets/69070339/ef2f943e-487f-4ac3-992a-aad82de4848a)

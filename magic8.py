import encodings
import random

question = input ('Question:  ')
random_number = random.randint(1,9)

# The if/elif/else statement starts here

num = random.randint(1,9)

if random_number == 1:
    answer = 'Most Certainly'
elif random_number == 2:
    answer = 'It is decidedly so'
elif random_number == 3:
    answer = 'Are you delusional?'
elif random_number == 4:
    answer = 'Could you repeat the question?'
elif random_number == 5:
    answer = 'It might be so'
elif random_number == 6:
    answer = 'It is hazy'
elif random_number == 7:
    answer = 'Try again later'     
elif random_number == 8:
    answer = 'I can see that happening for you'
else:
    answer = 'Error'

print('Question:    '+ question)
print('Magic 8 Ball:'+ answer)
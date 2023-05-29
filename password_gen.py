import random as rand
import pandas as pd

numbers = list("0123456789")
lower_letters = list("abcdefghijklmnopqrstuvwxyz")
upper_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
special_chars = list("`¬!\"£$%^&*()_-+={[}]|\\;:'@#~,<.>/?")

seed = rand.seed(rand.randint(3, 9))


def main():
    rand_pass = gen_rand_pass(seed, numbers, lower_letters, upper_letters, special_chars)

def gen_rand_pass(seed, numbers, lower_letters, upper_letters, special_chars):
    rand.seed(seed)
    rand.shuffle(numbers)
    rand.shuffle(lower_letters)
    rand.shuffle(upper_letters)
    rand.shuffle(special_chars)
    
    numbers = rand.sample(numbers, k=4)
    lower_letters = rand.sample(lower_letters, k=8)
    upper_letters = rand.sample(upper_letters, k=5)
    special_chars = rand.sample(special_chars, k=4)

    new_pass_pre_shuffle = numbers + lower_letters + upper_letters + special_chars

    rand.shuffle(new_pass_pre_shuffle)
    new_pass = "".join(new_pass_pre_shuffle)
    print(new_pass)

    return new_pass

main()



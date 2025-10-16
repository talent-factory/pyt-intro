#  Released under MIT License
#
#  Copyright (©) 2025. Talent Factory GmbH
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights to
#  use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
#  of the Software, and to permit persons to whom the Software is furnished to
#  do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
#  OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#  NON INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#  HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
#  WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
#  OR OTHER DEALINGS IN THE SOFTWARE.

import random
import time


def read_number(prompt, limit=10000, number_type=int):
    while True:
        try:
            value = number_type(input(prompt))
            if value < 1 or value > limit:
                print(f'Zahl ist nicht im Bereich 1 .. {limit}')
                continue
            return value
        except ValueError:
            print('Bitte eine Zahl eingeben.')


while True:
    upper_limit = read_number('Bitte gib den oberen Bereich für die Suche ein: ')

    # Computer sucht sich eine Zufallszahl zwichen 1 .. upper_limit (inklusive)
    random.seed(time.time())  #
    random_number = random.randint(1, upper_limit)

    guess = 0
    while guess != random_number:
        guess = read_number(f'Zahl zwischen 1 und {upper_limit} eingeben: ', upper_limit)

        if guess > random_number:
            print('Die Zahl ist zu gross.')

        if guess < random_number:
            print('Zahl ist zu klein.')

        if guess == random_number:
            print('Richtig gefunden!')
            break

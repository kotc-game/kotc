#!/usr/bin/env python3

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__version__ = "3.0"


import math


print("Welcome to the Keeper of the Cards cost calculator.")

def ask_choice(question, choices):
    while True:
        print(question)
        for i in range(len(choices)):
            print("{}: {}".format(i, choices[i]))

        ans = input("Enter choice (0-{}): ".format(len(choices) - 1))
        if ans in choices:
            return choices.index(ans)
        elif ans.isdigit():
            r = int(ans)
            if 0 <= r < len(choices):
                return r
            else:
                print("Error: entered number outside range.")
        else:
            print("Error: invalid input. Must be an integer.")


def ask_bool(question):
    while True:
        print(question)
        ans = input("Enter answer (yes/no): ")
        if ans.lower() in {"yes", "y", "1"}:
            return True
        elif ans.lower() in {"no", "n", "0"}:
            return False
        else:
            print("Error: invalid input. Must be \"yes\" or \"no\".")


def ask_int(question):
    while True:
        print(question)
        ans = input("Enter answer (0+): ")
        try:
            r = int(ans)
        except ValueError:
            print("Error: invalid input. Must be an integer.")
        else:
            if r >= 0:
                return r
            else:
                print("Error: must be 0 or greater.")


def ask_float(question):
    while True:
        print(question)
        ans = input("Enter answer (0+): ")
        try:
            r = float(ans)
        except ValueError:
            print("Error: invalid input. Must be a number.")
        else:
            if r >= 0:
                return r
            else:
                print("Error: must be 0 or greater.")


def get_ability():
    if ask_bool("Does the ability have an activation cost?"):
        cost_relief = ask_float("What is the relief of the activation cost?")
    else:
        cost_relief = 0

    effect_costs = 0
    n = 1
    while True:
        effect_costs += ask_float("What is the cost of effect #{}?".format(n))
        n += 1
        if not ask_bool("Does the ability have another effect?"):
            return max(1, effect_costs - cost_relief)


card_type = ask_choice("What type of card is it?", ["Creature", "Spell"])
if card_type == 0:
    offense = ask_int("What is the creature's offense?")
    defense = ask_int("What is the creature's defense?")

    if ask_bool("Does the creature have a caveat?"):
        caveat = ask_float("What is the creature's caveat relief?")
    else:
        caveat = 0

    power_cost = max(0, offense + defense/5 - caveat)

    ability_costs = 0
    if ask_bool("Does the creature have an ability?"):
        while True:
            ability_costs += get_ability()
            if not ask_bool("Does the creature have another ability?"):
                break

    cost = max(1, math.ceil(power_cost + ability_costs))
    print("This creature has a cost of: {}".format(cost))
    input("Press Enter to quit.")
else:
    cost = max(1, math.ceil(get_ability()))
    print("This spell has a cost of: {}".format(cost))
    input("Press Enter to quit.")

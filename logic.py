import card
import storage
import random
import streamlit as st

explanation_message = """

What would you like to do?

Options:

Add a card
Edit a card
View a card
Delete a card
List the cards

Input command word (edit, view, delete, or add)

"""


def add(front, back, id):
    storage.cards.append(card.Card(front, back, id))
    storage.save()


def edit(index, front, back):
    if index < 0 or index >= len(storage.cards):
        st.error("Invalid Index!")
        return

    storage.cards[int(index)].edit(front, back)
    storage.save()


def delete(index):

    if index < 0 or index >= len(storage.cards):
        st.error("Invalid Index!")
        return

    del storage.cards[index]
    storage.save()


def quiz():
    while (True):
        if len(storage.cards) <= 0:
            print("No cards!")
            break

        i = random.randint(0, len(storage.cards) - 1)
        print(storage.cards[i].front)
        response = input()
        print(storage.cards[i].back + "\n")

        if response.lower() != "stop":
            break

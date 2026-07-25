import streamlit as st
import storage
import deck
import card

if "mode" not in st.session_state:
    st.session_state.mode = None


def set_state(state):
    st.session_state.mode = state
    st.rerun()


def render_main():
    if st.button("ADD DECK"):
        set_state("add")

    if st.button("DELETE DECK"):
        set_state("delete")

    if st.button("ADD TO DECK"):
        set_state("add to deck")

    if st.button("REMOVE FROM DECK"):
        set_state("remove from deck")

    if st.button("LIST DECKS"):
        set_state("list")

    if st.button("GENERAL CARD MANAGER"):
        st.switch_page("pages/1_Card_Manager.py")

    if st.button("RETURN TO MAIN MENU"):
        st.switch_page("Main.py")


def render_add():
    name = st.text_input("Input deck name")

    if st.button("Save Deck") and name.strip():
        storage.decks.append(deck.Deck(name, []))
        st.success("Added!")
        storage.save()
        set_state(None)


def render_delete():
    deckID = st.number_input("Deck index", step=1,
                             min_value=1, max_value=len(storage.decks) - 1)

    _deck = storage.decks[deckID]
    st.markdown(
        f"""
                    ### DECK NAME: {_deck.name}""")

    if st.button("Delete Deck"):
        del storage.decks[deckID]
        st.success("Deleted!")
        storage.save()
        set_state(None)


def render_add_to_deck():
    if len(storage.decks) <= 1:
        st.write("No Custom Decks!")
        return

    if len(storage.cards) <= 0:
        st.write("No Cards!")
        return

    deckID = st.number_input("Deck index", step=1,
                             min_value=1, max_value=len(storage.decks) - 1)

    _deck = storage.decks[deckID]
    st.markdown(
        f"""
                ### DECK NAME: {_deck.name}""")

    cardID = st.number_input("Card index", step=1,
                             min_value=0, max_value=len(storage.cards) - 1)
    _card = storage.cards[cardID]

    st.markdown(f"***Front:*** {_card.front}")
    st.markdown(f"***Back:*** {_card.back}")

    if st.button("ADD"):
        _deck.cards.append(_card)
        st.success("Changed!")
        storage.save()
        set_state(None)


def render_remove_from_deck():
    if len(storage.decks) <= 1:
        st.write("No Custom Decks!")
        return

    if len(storage.cards) <= 0:
        st.write("No Cards!")
        return

    deckID = st.number_input("Deck index", step=1,
                             min_value=1, max_value=len(storage.decks) - 1)

    _deck = storage.decks[deckID]
    st.markdown(
        f"""
                ### DECK NAME: {_deck.name}""")

    if len(_deck.cards) == 0:
        st.write("No Cards!")
        return

    cardID = st.number_input("Card index", step=1,
                             min_value=0, max_value=len(_deck.cards) - 1)

    _card = _deck.cards[cardID]

    st.markdown(f"***Front:*** {_card.front}")
    st.markdown(f"***Back:*** {_card.back}")

    if st.button("REMOVE"):
        del _deck.cards[cardID]
        st.success("Removed!")
        set_state(None)


def render_list():
    if len(storage.decks) <= 0:
        st.write("No Decks!")
        return

    for i in range(0, len(storage.decks)):
        _deck = storage.decks[i]
        st.markdown(
            f"""
                ### DECK NAME: {_deck.name}""")

        for j in range(0, len(_deck.cards)):
            _card = _deck.cards[j]
            st.markdown(f"### CARD {j}:")
            st.markdown(f"***Front:*** {_card.front}")
            st.markdown(f"***Back:*** {_card.back}")


def render_backbutton():
    if st.button("BACK"):
        set_state(None)


match st.session_state.mode:
    case "add":
        render_add()
        render_backbutton()
    case "list":
        render_list()
        render_backbutton()

    case "add to deck":
        render_add_to_deck()
        render_backbutton()
    case "remove from deck":
        render_remove_from_deck()
        render_backbutton()
    case "delete":
        render_delete()
        render_backbutton()
    case _:
        render_main()

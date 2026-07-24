# pages/1_Card_Manager.py

import streamlit as st
import logic
import storage

if "loaded" not in st.session_state:
    storage.load()
    st.session_state.loaded = True

if "mode" not in st.session_state:
    st.session_state.mode = None


def set_state(state):
    st.session_state.mode = state
    st.rerun()


def render_main():
    if st.button("ADD CARD"):
        set_state("add")

    if st.button("EDIT CARD"):
        set_state("edit")

    if st.button("VIEW CARD"):
        set_state("view")

    if st.button("DELETE CARD"):
        set_state("delete")

    if st.button("LIST CARDS"):
        set_state("list")

    if st.button("DECK MANAGER"):
        st.switch_page("pages/3_Deck_Manager.py")

    if st.button("RETURN TO MAIN MENU"):
        st.switch_page("Main.py")


def render_add():
    front = st.text_input("Input front text")
    back = st.text_input("Input back text")

    if st.button("Save Card") and front.strip() and back.strip():
        logic.add(front, back, storage.nextID)
        storage.nextID += 1
        st.success("Added!")
        set_state(None)


def render_list():
    if len(storage.cards) <= 0:
        st.write("No cards!")
        return

    for i in range(0, len(storage.cards)):
        _card = storage.cards[i]
        st.markdown(
            f"""
            ### Card {i + 1}:
            - **front:** {_card.front}
            - **Back:** {_card.back}
            - **ID:** {_card.id}""")


def render_edit():
    if len(storage.cards) <= 0:
        st.write("No cards!")
        return

    index = st.number_input("Card index", step=1,
                            min_value=0, max_value=len(storage.cards) - 1)

    if len(storage.cards) < index or index < 0:
        return

    front = st.text_input("Input front text",
                          value=storage.cards[index].front)
    back = st.text_input("Input back text", value=storage.cards[index].back)

    if st.button("Save Card") and front.strip() and back.strip():
        logic.edit(index, front, back)
        st.success("Edited!")
        set_state(None)


def render_view():
    if len(storage.cards) <= 0:
        st.write("No cards!")
        return

    index = st.number_input("Card index", step=1,
                            min_value=0, max_value=len(storage.cards) - 1)

    if len(storage.cards) < index or index < 0:
        return

    _card = storage.cards[index]
    st.markdown(f"***Front:*** {_card.front}")
    st.markdown(f"***Back:*** {_card.back}")
    st.markdown(f"***ID:*** {_card.id}")


def render_delete():
    if len(storage.cards) <= 0:
        st.write("No cards!")
        return

    index = st.number_input("Card index", step=1,
                            min_value=0, max_value=len(storage.cards) - 1)

    if len(storage.cards) < index or index < 0:
        return

    st.markdown(f"***Front:*** {storage.cards[index].front}")
    st.markdown(f"***Back:*** {storage.cards[index].back}")

    if (st.button("DELETE")):
        logic.delete(index)
        st.error("DELETED")
        set_state(None)


def render_backbutton():
    if st.button("BACk"):
        set_state(None)


match st.session_state.mode:
    case "add":
        render_add()
        render_backbutton()
    case "edit":
        render_edit()
        render_backbutton()
    case "list":
        render_list()
        render_backbutton()
    case "view":
        render_view()
        render_backbutton()
    case "delete":
        render_delete()
        render_backbutton()
    case _:
        render_main()

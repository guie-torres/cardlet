import streamlit as st
import storage.storage as storage
import logic
import utils.session as session
rendered_decks = []


def load_css(path):
    with open(f"styles/{path}.css") as f:
        st.markdown(f"<style>{f.read()}</style>",
                    unsafe_allow_html=True)


def render_card_practice(text):
    st.markdown(
        f"""
                <div class="flashcard">
                    <h3 class="card-front">{text}</h3>
                </div>
                """,
        unsafe_allow_html=True
    )


def render_card(card, deck):
    col1, col2 = st.columns([3, 1])

    with col1:
        st.markdown(
            f"""
            <div class="flashcard">
                <p class="card-front">{card.front}</p>
                <p class="card-back">{card.back}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        if st.button("✏️ Edit", key=f"edit_{deck.id}/{card.id}", use_container_width=True):
            st.session_state.editCardId = card.id
            session.set_state("editCard")

        if st.button("🗑️ Delete", key=f"delete_{deck.id}/{card.id}", use_container_width=True):
            st.session_state.deleteCardId = card.id
            session.set_state("deleteCard")

        if st.button("✅ Add", key=f"add_{deck.id}/{card.id}", use_container_width=True):
            st.session_state.addCardId = card.id
            session.set_state("addToDeck")


def render_card_deck(card, deck):
    col1, col2 = st.columns([3, 1])

    with col1:
        st.markdown(
            f"""
            <div class="flashcard">
                <p class="card-front">{card.front}</p>
                <p class="card-back">{card.back}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        if st.button("✏️ Edit", key=f"edit_{deck.id}/{card.id}", use_container_width=True):
            st.session_state.editCardId = card.id
            session.set_state("editCard")

        if st.button("🗑️ Delete", key=f"delete_{deck.id}/{card.id}", use_container_width=True):
            st.session_state.deleteCardId = card.id
            session.set_state("deleteCard")

        if st.button("❌ Remove", key=f"remove_{deck.id}/{card.id}", use_container_width=True):
            logic.remove_from_deck(deck, card)
            st.rerun()


def render_card_add():
    front = st.text_input("Input front text")
    back = st.text_input("Input back text")

    if st.button("ADD") and front.strip() and back.strip():
        logic.add_card(front, back)
        st.success("Added!")

        session.set_state(None)


def render_deck_delete(deck):
    st.write('WRITE "CONFIRM" TO DELETE DECK:')

    st.markdown(f"### {deck.name}")

    if st.text_input('WRITE "CONFIRM"') == "CONFIRM" and st.button("DELETE"):
        st.success("DELETED")
        logic.delete_deck(deck)
        session.set_state(None)


def render_deck_export(deck):
    st.markdown(
        f"""
        <div style=display: flex; flex-direction: column; justify-content: flex-start;>
        <h1 style = font-size: 80px; white-space: nowrap; margin: 0;>
        EXPORT DECK: {deck.name}
        </h1>
        <p>Export the deck to quizlet!</p>
        </div>""", unsafe_allow_html=True)
    q_deck = logic.convert_deck_to_quizlet(deck)
    st.code(q_deck, language=None)

    st.download_button(
        "DOWNLOAD",
        data=q_deck,
        file_name=f"{deck.name}.txt",
        mime="text/plain"
    )


def render_card_delete(card):
    st.write('WRITE "CONFIRM" TO DELETE CARD:')

    st.markdown(f"### {card.front}")
    st.markdown(f"***{card.back}***")

    if st.text_input('WRITE "CONFIRM"') == "CONFIRM" and st.button("DELETE"):
        st.success("DELETED")
        logic.delete_card(card)
        session.set_state(None)


def render_card_edit(card):
    front = st.text_input("Input front text", card.front)
    back = st.text_input("Input back text", card.back)

    if st.button("SAVE") and front.strip() and back.strip():
        logic.edit_card(card, front, back)
        st.success("Saved!")

        session.set_state(None)


def render_deck_rename(deck):
    name = st.text_input("Input new name", deck.name)

    if st.button("SAVE") and name.strip():
        logic.rename_deck(deck, name)
        st.success("Saved!")

        session.set_state(None)


def render_card_add_to_deck(card):
    st.markdown("""<h1>SELECT WHICH DECK TO ADD TO</h1>""",
                unsafe_allow_html=True)

    for d in storage.decks:

        if card.id in d.cards:
            continue

        col1, col2 = st.columns([3, 1])

        with col1:
            st.markdown(f"""<h4>{d.name}</h4>""", unsafe_allow_html=True)

        with col2:
            if st.button(f"ADD", key=f"add_{d.id}"):
                logic.add_to_deck(d, card)
                st.success("Added!")
                session.set_state(None)


def render_deck(deck):
    if rendered_decks.__contains__(deck.id):
        col1, col2, col3, col4, col5 = st.columns([2, 0.4, 0.4, 0.4, 0.4])
        with col1:
            st.markdown(
                f"""
                        ### DECK NAME: {deck.name}""")

        with col2:
            if st.button("HIDE", key=f"hide_{deck.id}"):
                rendered_decks.remove(deck.id)
                st.rerun()

        for j in range(0, len(deck.cards)):
            _card = storage.find_card(deck.cards[j])

            if deck == storage.decks[0]:
                render_card(_card, deck)
            else:
                render_card_deck(_card, deck)

        with col3:
            if st.button("EXPORT", key=f"export_{deck.id}"):
                st.session_state.exportDeckId = deck.id
                session.set_state("exportDeck")

        if deck == storage.decks[0]:
            return

        with col4:
            if st.button("EDIT", key=f"rename_{deck.id}"):
                st.session_state.renameDeckId = deck.id
                session.set_state("renameDeck")

        with col5:
            if st.button("DELETE", key=f"delete_{deck.id}"):
                st.session_state.deleteDeckId = deck.id
                session.set_state("deleteDeck")
    else:
        col1, col2, col3, col4, col5 = st.columns([2, 0.4, 0.4, 0.4, 0.4])
        with col1:
            st.markdown(f"""### DECK NAME: {deck.name}""")

        with col2:
            if st.button("SHOW", key=f"show_{deck.id}"):
                rendered_decks.append(deck.id)
                st.rerun()

        with col3:
            if st.button("EXPORT", key=f"export_{deck.id}"):
                st.session_state.exportDeckId = deck.id
                session.set_state("exportDeck")

        if deck == storage.decks[0]:
            return

        with col4:
            if st.button("EDIT", key=f"rename_{deck.id}"):
                st.session_state.renameDeckId = deck.id
                session.set_state("renameDeck")

        with col5:
            if st.button("DELETE", key=f"delete_{deck.id}"):
                st.session_state.deleteDeckId = deck.id
                session.set_state("deleteDeck")


def render_deck_add():
    name = st.text_input("Input deck name")

    if st.button("ADD") and name.strip():
        logic.add_deck(name)
        st.success("Added!")
        session.set_state(None)


def render_backbutton():
    if st.button("BACK"):
        session.set_state(None)


def render_back_to_menu_button():
    if st.button("MAIN MENU"):
        st.switch_page("Main.py")

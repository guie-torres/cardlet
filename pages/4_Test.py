import utils.ui as ui
import storage.storage as storage
import streamlit as st
import ai
import logic

aiDeck = ai.generate_deck("""Ownership of knowledge is never neutral. It manifests as epistemic authority, proprietary control, or collective stewardship. Those who wield these forms of power, whether states, corporations or the public, often use it to influence other knowers. This Nazi poster, while currently physically owned by the Musée Carnavalet, exemplifies how a state's exercise of epistemic authority transforms knowledge into a political tool.

This poster appeared shortly after Germany invaded the USSR. The top text says “VICTORIA”, which is further represented by the large “V” in the picture. Both the French resistance and German occupiers tried to make the “V” represent their cause, creating the “battle of the Vs”. This conflict reveals ownership of symbols is contested, not absolute. The state controlled the printing presses, the walls, and the approval processes for all the posters. Controlling production gave it the power to change the symbol's connotations through language.

Visual rhetoric depicts the “crusade” as a European collectivist effort against an outside threat, appealing to the Catholic audience and exploiting in-group/out-group bias, visualised by arrows from multiple states uniting and omitting problematic borders. By owning the rhetoric, the state effectively controls how the population interprets the invasion. This demonstrates how owning rhetoric (a Language WOK) gives the state ownership over the interpretation of knowledge, a key concern in the AOK of History, illustrating that whoever controls the narrative, practically controls the “truth” available to the knower, giving them de facto epistemic authority.

This allows them to reverse the meaning of a symbol, turning it from an anti-government to a pro-government sign. Yet it also reveals the limits of state ownership: while the state can control production and rhetoric, it cannot fully control the interpretation. The “V” scrawled on the walls was still understood as French resistance, showing how state ownership is always contested by the knower. 
""")

deck = logic.add_deck(aiDeck.name)

for card in aiDeck.cards:
    c = logic.add_card(card.front, card.back)
    logic.add_to_deck(deck, c)

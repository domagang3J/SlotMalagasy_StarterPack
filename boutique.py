import streamlit as st
import json

st.set_page_config(page_title="🛍️ Boutique IA Slot Malagasy™", layout="wide")
st.title("🛍️ Boutique IA Culturelle — Slot Malagasy™")

products = [
    {"id": "PROD-001", "name": "Tenue holographique royale", "price": 5000, "rarity": "Légendaire"},
    {"id": "PROD-002", "name": "NFT Zébu x5", "price": 3000, "rarity": "Galactique"},
    {"id": "PROD-003", "name": "Accès simulateur de gains x5", "price": 2500, "rarity": "Rare"},
    {"id": "PROD-004", "name": "Avatar IA VIP mobile", "price": 4000, "rarity": "Légendaire"},
    {"id": "PROD-005", "name": "Carte collector IA Tsapiky", "price": 1500, "rarity": "Standard"},
]

cycle_filter = st.selectbox("🔎 Filtrer par rareté", ["Tous", "Standard", "Rare", "Légendaire", "Galactique"])
st.markdown("---")

for prod in products:
    if cycle_filter != "Tous" and prod["rarity"] != cycle_filter:
        continue

    st.subheader(f"🎁 {prod['name']}")
    st.text(f"🆔 ID : {prod['id']} — 💎 Rareté : {prod['rarity']}")
    st.text(f"💰 Prix : {prod['price']} Ar")
    if st.button(f"🛒 Acheter {prod['name']}"):
        st.session_state["selected_product"] = prod
        st.success("✅ Produit ajouté au panier IA")
        st.experimental_rerun()

if "selected_product" in st.session_state:
    st.markdown("---")
    st.header("🔐 Paiement IA simulé (MVola / Orange Money)")
    phone = st.text_input("📱 Numéro mobile")
    method = st.selectbox("💳 Méthode", ["MVola", "Orange Money", "Airtel Money"])
    if st.button("💸 Confirmer le paiement"):
        st.success(f"✅ Paiement fictif effectué avec {method} pour {st.session_state['selected_product']['name']}")

import streamlit as st
import os
import json
import random

st.set_page_config(page_title="Console Admin Slot Malagasy™", layout="wide")
st.title("🎛️ Console Admin IA VIP — Slot Malagasy™")

# Statistiques simulées
st.metric("👥 Spectateurs IA en direct", random.randint(50, 150))
st.metric("💎 NFT générés", len([f for f in os.listdir("nft_gallery") if f.endswith(".json")]))
st.metric("📦 NFT achetés", random.randint(10, 40))

# Classement IA fictif
st.subheader("🏆 Cycles IA les plus populaires")
st.bar_chart({"x2": 20, "x3": 35, "x4": 17, "x5": 28})

# Aperçu des derniers NFT
st.subheader("🧬 Aperçu des derniers NFT générés")
nft_files = sorted([f for f in os.listdir("nft_gallery") if f.endswith(".json")])[-5:]
for nft_file in nft_files:
    with open(os.path.join("nft_gallery", nft_file)) as f:
        nft_data = json.load(f)
    st.write(f"🔹 {nft_data['id']} — {nft_data['name']} ({nft_data['rarity']})")
st.markdown("---")
st.subheader("➕ Ajouter un nouveau produit")

new_name = st.text_input("Nom du produit")
new_price = st.number_input("Prix Ar", min_value=0)
new_rarity = st.selectbox("Rareté", ["Standard", "Rare", "Légendaire", "Galactique"])
if st.button("📦 Ajouter le produit"):
    new_product = {
        "id": f"PROD-{random.randint(100,999)}",
        "name": new_name,
        "price": new_price,
        "rarity": new_rarity
    }
    with open("produits_admin.json", "a") as f:
        f.write(json.dumps(new_product) + "\n")
    st.success(f"✅ Produit {new_name} ajouté à la boutique IA !")

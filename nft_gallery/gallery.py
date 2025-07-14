import streamlit as st
import os
import json

st.set_page_config(page_title="Galerie NFT Slot Malagasy™")
st.title("🎨 Galerie des NFT Culturels Galactiques")

cycles = st.multiselect("🔍 Filtrer par cycle IA", ["x2", "x3", "x4", "x5"], default=["x2", "x3", "x4", "x5"])
rarity_filter = st.selectbox("🧬 Filtrer par rareté", ["Tous", "Standard", "Rare", "Légendaire", "Galactique"])

nft_files = [f for f in os.listdir("nft_gallery") if f.endswith(".json")]

for nft_file in nft_files:
    with open(os.path.join("nft_gallery", nft_file)) as f:
        nft_data = json.load(f)

    if nft_data["cycle"] not in cycles:
        continue
    if rarity_filter != "Tous" and nft_data["rarity"] != rarity_filter:
        continue

    st.markdown("---")
    st.subheader(f"🔹 {nft_data['name']} — {nft_data['rarity']}")
    st.json(nft_data)

    image_path = f"nft_gallery/{nft_file.replace('.json','.png')}"
    if os.path.exists(image_path):
        st.image(image_path, caption="Visuel NFT", use_column_width=True)

    st.button(f"🛍️ Acheter {nft_data['name']}")

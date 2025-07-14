import streamlit as st
import os
import json

st.set_page_config(page_title="Galerie NFT Slot Malagasy™")
st.title("🎨 Galerie des NFT Culturels Galactiques")

nft_files = [f for f in os.listdir("nft_gallery") if f.endswith(".json")]

for nft_file in nft_files:
    st.subheader(f"🔹 {nft_file.replace('.json','')}")
    with open(os.path.join("nft_gallery", nft_file)) as f:
        nft_data = json.load(f)
    st.json(nft_data)

    image_path = f"nft_gallery/{nft_file.replace('.json','.png')}"
    if os.path.exists(image_path):
        st.image(image_path, caption="Visuel NFT", use_column_width=True)
    else:
        st.info("Aucune image associée.")

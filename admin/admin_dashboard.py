import json
import os
import random

nft_gallery = "nft_gallery"
os.makedirs(nft_gallery, exist_ok=True)

regions = ["Toliara", "Antananarivo", "Fianarantsoa", "Mahajanga", "Toamasina"]
rarities = ["Standard", "Rare", "Légendaire", "Galactique"]
emotions = [88, 92, 95, 98, 102]

for i in range(1, 11):
    cycle = f"x{random.choice([2, 3, 4, 5])}"
    nft = {
        "id": f"NFT-{i}",
        "name": f"Zébu IA {cycle}",
        "cycle": cycle,
        "timestamp": f"2025-07-13T23:{i:02d}:00",
        "region": random.choice(regions),
        "rarity": random.choice(rarities),
        "emotion": f"{random.choice(emotions)} bpm"
    }
    with open(os.path.join(nft_gallery, f"nft_{i}.json"), "w") as f:
        json.dump(nft, f, indent=4)

print("✅ 10 NFT culturels générés dans nft_gallery/")
st.markdown("---")
st.header("📦 NFTs générés en temps réel")

nft_files = sorted([f for f in os.listdir("nft_gallery") if f.endswith(".json")])

for nft_file in nft_files:
    with open(os.path.join("nft_gallery", nft_file)) as f:
        nft_data = json.load(f)

    col1, col2 = st.columns([2, 3])
    with col1:
        st.subheader(f"🔹 {nft_data['name']}")
        st.text(f"🆔 ID : {nft_data['id']}")
        st.text(f"💎 Rareté : {nft_data['rarity']}")
        st.text(f"🌍 Région : {nft_data['region']}")
        st.text(f"🔁 Cycle : {nft_data['cycle']}")
        st.text(f"🎵 Émotion : {nft_data['emotion']}")

    image_path = f"nft_gallery/{nft_file.replace('.json','.png')}"
    with col2:
        if os.path.exists(image_path):
            st.image(image_path, caption="Visuel NFT", use_column_width=True)
        else:
            st.info("Aucune image associée.")
with st.expander("📤 Ajouter une image à ce NFT"):
    uploaded_file = st.file_uploader("Choisir une image (.png)", type=["png"])
    if uploaded_file:
        save_path = os.path.join("nft_gallery", nft_file.replace(".json", ".png"))
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success("✅ Image ajoutée avec succès !")
from supabase import create_client

url = "https://TON_PROJET.supabase.co"
key = "TON_CLÉ_API"
supabase = create_client(url, key)

# Enregistrement d’un NFT
supabase.table("nfts").insert(nft_data).execute()
data = supabase.table("nfts").select("*").execute()
for nft in data.data:
    st.write(nft["name"], nft["rarity"], nft["region"])

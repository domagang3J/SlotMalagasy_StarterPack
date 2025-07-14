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

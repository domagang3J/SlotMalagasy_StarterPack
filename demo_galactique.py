import streamlit as st
import random

st.set_page_config(page_title="🎬 Démo Galactique Slot Malagasy™", layout="wide")
st.title("🎬 Démo Galactique — Slot Malagasy™")

st.markdown("### 🌌 Bienvenue dans l'univers IA culturel malagasy")
st.video("https://www.youtube.com/embed/JL9xOs-G1hI")  # Exemple vidéo Streamlit

st.success("✅ NFT IA générés : 10")
st.info("👥 Spectateurs IA simulés : " + str(random.randint(100, 300)))
st.warning("💎 Cycle IA dominant : x" + str(random.choice([2, 3, 4, 5])))

st.markdown("---")
st.subheader("🛍️ Boutique IA pré-remplie")
st.write("🎁 Tenue holographique royale — 5000 Ar")
st.write("🎁 Avatar IA VIP mobile — 4000 Ar")
st.write("🎁 Carte collector Tsapiky — 1500 Ar")

st.button("💸 Simuler un achat IA")
st.button("📡 Synchroniser avec Supabase")

st.markdown("---")
st.header("👑 Slot Malagasy™ — L’IA culturelle du futur")
st.image("assets/zebu_ia.gif", caption="Zébu IA en orbite culturelle", use_column_width=True)

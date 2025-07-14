import streamlit as st

st.set_page_config(page_title="Slot Malagasy™", layout="centered")

st.title("🎰 Slot Malagasy™ — Cycle IA Galactique")
st.image("assets/zebu_ia.gif")
st.audio("assets/tsapiky_toliara.mp3")

st.subheader("Bienvenue camarade VIP 🐃🌌")
cycle = st.radio("Choisis ton cycle IA :", ["x2", "x3", "x4", "x5"])
st.success(f"🚀 Cycle {cycle} activé ! Zébu IA synchronisé.")

if cycle == "x5":
    st.balloons()
    st.warning("🎁 Bonus NFT débloqué : Tenue royale holographique")

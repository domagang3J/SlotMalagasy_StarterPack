import streamlit as st

st.set_page_config(page_title="Slot Malagasy™ IA", layout="wide")
st.title("🎛️ Slot Malagasy™ — Interface IA Culturelle")

tabs = st.tabs(["🎨 Galerie NFT", "🛍️ Boutique IA", "🎛️ Console Admin", "🎬 Démo Galactique"])

with tabs[0]:
    st.markdown("## 🎨 Galerie NFT")
    st.markdown("Lance `gallery.py` pour afficher les NFT culturels.")
    st.code("streamlit run gallery.py")

with tabs[1]:
    st.markdown("## 🛍️ Boutique IA")
    st.markdown("Lance `boutique.py` pour accéder au marché IA.")
    st.code("streamlit run boutique.py")

with tabs[2]:
    st.markdown("## 🎛️ Console Admin")
    st.markdown("Lance `admin_dashboard.py` pour gérer les NFT et VIP.")
    st.code("streamlit run admin/admin_dashboard.py")

with tabs[3]:
    st.markdown("## 🎬 Démo Galactique")
    st.markdown("Lance `demo_galactique.py` pour une présentation immersive.")
    st.code("streamlit run demo_galactique.py")

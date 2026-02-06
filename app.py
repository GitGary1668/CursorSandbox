import streamlit as st
from pathlib import Path

st.title("Hello garymade-Cursor Vibe")
st.write("This is a test of the streamlit app")

if "menu_index" not in st.session_state:
    st.session_state.menu_index = None

options = ["Meat", "Vegetable", "Beverage", "<clear entry>"]
IMAGE_MAP = {
    "Meat": "images/steak.png",
    "Vegetable": "images/salad.png",
    "Beverage": "images/soda.png",
}

col1, col2 = st.columns(2)

with col1:
    menu = st.selectbox(
        "Menu",
        options=options,
        index=st.session_state.menu_index,
        placeholder="Choose an option...",
        key="menu"
    )

with col2:
    if menu and menu != "<clear entry>" and menu in IMAGE_MAP:
        image_path = Path(__file__).parent / IMAGE_MAP[menu]
        if image_path.exists():
            # Square display for 1:1 aspect ratio
            st.image(str(image_path), width=300)

if menu == "<clear entry>":
    st.session_state.menu_index = None
    st.rerun()
elif menu is not None:
    st.session_state.menu_index = options.index(menu)


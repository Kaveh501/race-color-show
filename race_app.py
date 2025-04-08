
import streamlit as st
from PIL import Image, ImageDraw
import random
import time

# تنظیمات اولیه
st.set_page_config(page_title="Color  Race Live", layout="centered")
st.title("🤗 Live Color Race Show!")
colors = ["red", "green", "gold", "purple", "blue", "black"]
positions = [50, 100, 150, 200, 250, 300]

user_bet = st.selectbox("🎯 Choose your Color!", colors)

if st.button("🚀 Start Race"):
    st.write("🎬 Race is starting... Get ready!")

    # موقعیت اولیه لاک‌پشت‌ها
    turtles = {color: 0 for color in colors}
    winner = None

    # مسابقه مرحله‌ای
    race_progress = st.empty()

    while not winner:
        img = Image.new("RGB", (600, 400), color="white")
        draw = ImageDraw.Draw(img)

        for i, color in enumerate(colors):
            move = random.randint(0, 10)
            turtles[color] += move
            x = 50 + turtles[color]
            y = positions[i]
            draw.ellipse((x, y, x+20, y+20), fill=color)

            if turtles[color] >= 500:
                winner = color

        race_progress.image(
            img, caption="🏁 Race in progress...", use_container_width=True)
        time.sleep(0.1)

    if user_bet == winner:
        st.success(f"😍 You won! The {winner} Color is the champion!")
    else:
        st.error(f"👻 You lost. The {winner} Color won the race.")

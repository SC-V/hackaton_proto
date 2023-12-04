import random
import streamlit as st
from time import sleep


SPIN_BONUS_LIST = [
    "Lamborgini Diablo 1990 (1:16 model)",
    "One free ride",
    "Meshok kartoshki",
    "Nintendo Switch",
    "Additional 5% discount for 5 rides",
    "Italian pizza voucher for Pizzeria Balboa",
    "Amazon $20 gift card",
    "Amazon $10 gift card",
    "Cart of bananas",
    "Andrey Kudryashov's unsolicited advice",
    "1 free night at Sofitel presidential suite",
    "1 free AirBnB experience ticket",
    "One way ticket to Pakistan",
    "Jar of strawberry jam",
    "Branded Yango hoodie",
    "2 hours of karting for your and 2 friends"
]


def chat_answer(prompt: str, subscription_enabled: bool):
    if subscription_enabled:
        with st.chat_message(name="User",
                             avatar="🧑‍💻"):
            st.write(prompt)

        with st.chat_message(name="Master of support",
                             avatar="🧑‍💻"):
            st.write("I'll answer straight away!")
            sleep(2)
            st.write("How may I help you?")
    else:
        with st.chat_message(name="User",
                             avatar="🧑‍💻"):
            st.write(prompt)

        with st.chat_message(name="Support bot",
                             avatar="🤖"):
            st.write("I'll answer in 100 light years")


st.set_page_config(page_title=f"Yango Hackaton Dec 2023",
                   layout="wide")

st.markdown(f"# Yango Turbo")
st.markdown("This is an app to showcase the **:red[Yango Turbo]** subscription for the 1st Yango Hackaton Dec 2023.")

subscription_enabled = st.checkbox(label="Yango Turbo",
                                   value=False,
                                   help="Click to simulate the purchase of Yango Turbo")

subscription_discount = 0.1

econom_price = 10.0
comfort_price = 14.0
express_price = 9.0

bonus_string = ""

if subscription_enabled:
    col_lets_roll, col_result = st.columns([1, 2])

    with col_lets_roll:
        if st.button("Roll your bonus benefit!"):
            with col_result:
                with st.status("Ready to spin!", expanded=False) as status:
                    st.write("Spin every week!")
                    status.update(label="Spinning the wheel...")
                    sleep(1)
                    status.update(label="Getting the best bonuses...")
                    sleep(1.5)
                    status.update(label="You are gonna be amazed...")
                    sleep(2)
                    prize_id = random.randint(0, len(SPIN_BONUS_LIST) - 1)
                    status.update(label=f"Wow! You won **{SPIN_BONUS_LIST[prize_id]}**", state="complete", expanded=False)
                    if SPIN_BONUS_LIST[prize_id] == "Additional 5% discount for 5 rides":
                        subscription_discount = 0.15
                    if SPIN_BONUS_LIST[prize_id] == "One free ride":
                        subscription_discount = 1
                    if SPIN_BONUS_LIST[prize_id] == "Cart of bananas":
                        bonus_string = "🍌🍌🍌🍌🍌🍌🍌🍌"
            st.balloons()


col_econom, col_comfort, col_express = st.columns(3)

with col_econom:
    if subscription_enabled:
        st.metric(label=r"Econom 🏎",
                  value=f"{round(econom_price * (1 - subscription_discount), 1)}/S",
                  delta=f"{subscription_discount * 100}% off")
    else:
        st.metric(label="Econom",
                  value=f"{econom_price}/S")
    st.write(bonus_string)

with col_comfort:
    if subscription_enabled:
        st.metric(label=r"Comfort 🏎",
                  value=f"{round(comfort_price * (1 - subscription_discount), 1)}/S",
                  delta=f"{subscription_discount * 100}% off")
    else:
        st.metric(label="Comfort",
                  value=f"{comfort_price}/S")

with col_express:
    if subscription_enabled:
        st.metric(label=r"Express 🏎",
                  value=f"{round(express_price * (1 - subscription_discount), 1)}/S",
                  delta=f"{subscription_discount * 100}% off")
    else:
        st.metric(label="Express",
                  value=f"{express_price}/S")


prompt = st.chat_input(placeholder="Operator will answer shortly" if subscription_enabled else "Your message will be processed by a bot")

if prompt:
    chat_answer(prompt, subscription_enabled)

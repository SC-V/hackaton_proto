import random
import streamlit as st
from time import sleep


SPIN_BONUS_LIST = [
    "Lamborgini Diablo 1990 (1:16 model)",
    "One free ride or delivery",
    "5% discount for comfort rides",
    "5% discount for comfort rides",
    "5% discount for comfort rides",
    "5% discount for express deliveries",
    "5% discount for express deliveries",
    "5% discount for express deliveries",
    "Pizza voucher for Papa Johns",
    "Andrey Kudryashov's unsolicited advice",
    "Andrey Kudryashov's unsolicited advice",
    "One way ticket to Pakistan",
    "One way ticket to Pakistan",
    "Branded Yango hoodie",
    "Branded Yango hoodie",
    "Branded Yango cup",
    "Branded Yango hat",
    "Free e-book at Bookmate",
    "Free e-book at Bookmate",
    "15% discount for AirBnB experience",
    "Bottle of wine from Andrey Kudryashov"
]


def chat_answer(prompt: str, subscription_enabled: bool):
    if subscription_enabled:
        with st.chat_message(name="User",
                             avatar="🧑‍💻"):
            st.write(prompt)

        with st.chat_message(name="Master of support",
                             avatar="🧑‍💻"):
            st.write("Hi, friend! Happy to see you!")
            sleep(2)
            st.write("I'll check your issue straight away!")
    else:
        with st.chat_message(name="User",
                             avatar="🧑‍💻"):
            st.write(prompt)

        with st.chat_message(name="Support bot",
                             avatar="🤖"):
            st.write("I'll answer with some ML bull$#^t, human")


st.set_page_config(page_title=f"Yango Hackaton Dec 2023",
                   layout="wide")

st.markdown(f"# Yango Turbo")
st.markdown("This is an app to showcase the **:red[Yango Turbo]** subscription for the 1st Yango Hackaton Dec 2023.")

with st.container(border=True):
    subscription_enabled = st.checkbox(label="Yango Turbo",
                                       value=False,
                                       help="Click here to enable Yango Turbo benefits")

econom_subscription_discount = 0
comfort_subscription_discount = 0
express_subscription_discount = 0

econom_price = 10.0
comfort_price = 14.0
express_price = 9.0

bonus_string = ""

if subscription_enabled:
    st.write("With Yango Turbo you surge ⚡️ less! Get premium support and a chance to spin for more benefits each few days!")
    col_lets_roll, col_result = st.columns([1, 2])

    with col_lets_roll:
        if st.button("Roll your bonus benefit!", type="primary"):
            with col_result:
                with st.status("Ready to spin!", expanded=False) as status:
                    st.write("We allow to spin every 3 days, but we made an exception for you. Spin as much as you want.")
                    st.write("Prizes are just to get the idea of what we can put here: branded items, partnership items, discounts...")
                    st.write("Not a public offer.")
                    status.update(label="Spinning the wheel...")
                    sleep(1)
                    status.update(label="Getting the best bonuses...")
                    sleep(1.5)
                    status.update(label="You are gonna be amazed...")
                    sleep(2)
                    prize_id = random.randint(0, len(SPIN_BONUS_LIST) - 1)
                    status.update(label=f"Wow! You won **{SPIN_BONUS_LIST[prize_id]}**", state="complete", expanded=False)
                    if SPIN_BONUS_LIST[prize_id] == "5% discount for comfort rides":
                        comfort_subscription_discount = 0.05
                    if SPIN_BONUS_LIST[prize_id] == "5% discount for express deliveries":
                        express_subscription_discount = 0.05
                    if SPIN_BONUS_LIST[prize_id] == "One free ride or delivery":
                        comfort_subscription_discount = 1
                        express_subscription_discount = 1
                        econom_subscription_discount = 1
                    if SPIN_BONUS_LIST[prize_id] == "One way ticket to Pakistan":
                        bonus_string = "خوش آمدید!"
                    if SPIN_BONUS_LIST[prize_id] == "Bottle of wine from Andrey Kudryashov":
                        bonus_string = "SPECIAL PRIZE! That's not a joke! The first hackaton judge to send a screenshot of this prize to Andrey will win a real bottle 🍾!"
            st.balloons()


col_econom, col_comfort, col_express = st.columns(3)

with col_econom:
    if econom_subscription_discount != 0:
        st.metric(label=r"Econom 🏎",
                  value=f"{round(econom_price * (1 - econom_subscription_discount), 1)}/S",
                  delta=f"{econom_subscription_discount * 100}% off")
    else:
        st.metric(label="Econom",
                  value=f"{econom_price}/S")
    st.write(bonus_string)

with col_comfort:
    if comfort_subscription_discount != 0:
        st.metric(label=r"Comfort 🏎",
                  value=f"{round(comfort_price * (1 - comfort_subscription_discount), 1)}/S",
                  delta=f"{comfort_subscription_discount * 100}% off")
    else:
        st.metric(label="Comfort",
                  value=f"{comfort_price}/S")

with col_express:
    if express_subscription_discount != 0:
        st.metric(label=r"Express 🏎",
                  value=f"{round(express_price * (1 - express_subscription_discount), 1)}/S",
                  delta=f"{express_subscription_discount * 100}% off")
    else:
        st.metric(label="Express",
                  value=f"{express_price}/S")


prompt = st.chat_input(placeholder="Operator will answer shortly" if subscription_enabled else "Your message will be processed by a bot")

if prompt:
    chat_answer(prompt, subscription_enabled)

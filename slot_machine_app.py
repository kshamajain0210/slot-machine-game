import random
import streamlit as st

# Game configuration
ROWS = 3
COLS = 3
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

symbols = {"A": 2, "B": 4, "C": 6, "D": 8}
payouts = {"A": 5, "B": 4, "C": 3, "D": 2}

# Core functions
def get_spin(rows, cols, symbols):
    pool = []
    for sym, count in symbols.items():
        pool.extend([sym] * count)
    spin = random.choices(pool, k=rows * cols)
    return [spin[i * cols:(i + 1) * cols] for i in range(rows)]

def check_win(spin, lines, bet):
    total = 0
    win_lines = []
    for i in range(lines):
        if all(s == spin[i][0] for s in spin[i]):
            total += payouts[spin[i][0]] * bet
            win_lines.append(i + 1)
    return total, win_lines

# Streamlit app
st.title("🎰 Slot Machine Game")

# Initial session state
if "balance" not in st.session_state:
    st.session_state.balance = st.number_input("💰 Enter deposit amount to start:", min_value=1, max_value=100000, step=10)

st.markdown(f"### Current Balance: ${st.session_state.balance}")

with st.form("bet_form"):
    lines = st.slider("🎯 Lines to bet on", min_value=1, max_value=MAX_LINES, value=1)
    bet = st.slider("💵 Bet per line", min_value=MIN_BET, max_value=MAX_BET, value=10)
    submitted = st.form_submit_button("🎲 Spin the Slot Machine")

if submitted:
    total_bet = lines * bet
    if total_bet > st.session_state.balance:
        st.error("❌ Not enough balance!")
    else:
        st.session_state.balance -= total_bet
        spin = get_spin(ROWS, COLS, symbols)

        st.write("### 🎰 Slot Result:")
        for row in spin:
            st.write(" | ".join(row))

        win, win_lines = check_win(spin, lines, bet)
        st.session_state.balance += win

        st.success(f"🏆 You won ${win}!")

        if win_lines:
            st.info(f"✨ Winning lines: {', '.join(map(str, win_lines))}")
        else:
            st.info("😢 No wins this time.")

        st.markdown(f"### 💳 Updated Balance: ${st.session_state.balance}")

# Option to reset
if st.button("🔄 Reset Game"):
    del st.session_state.balance
    st.rerun()


import streamlit as st
import random

# Page Configuration
st.set_page_config(page_title="Number Guessing Game", page_icon="🎮")

# --- Author and Header ---
st.subheader("Developed by: **Study Group 3**")
st.title("🎮 Number Guessing Game")
st.markdown("---")

# Initialize Session State variables to keep data across reruns
if 'random_number' not in st.session_state:
    st.session_state.random_number = random.randint(1, 30)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

def reset_game():
    st.session_state.random_number = random.randint(1, 30)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.rerun()

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# --- UI Sidebar for Game Controls ---
with st.sidebar:
    st.header("Game Settings")
    if st.button("New Game / Restart"):
        reset_game()
    
    st.divider()
    st.subheader("Need Help?")
    
    if st.button("Even or Odd?"):
        if st.session_state.random_number % 2 == 0:
            st.info("The number is **Even**")
        else:
            st.info("The number is **Odd**")
            
    if st.button("Prime or Composite?"):
        if is_prime(st.session_state.random_number):
            st.info("The number is **Prime**")
        else:
            st.info("The number is **Composite**")
            
    if st.button("Quit & Reveal Answer"):
        st.warning(f"The hidden number was: {st.session_state.random_number}")
        st.session_state.game_over = True

# --- Main Game Screen ---
if not st.session_state.game_over:
    st.write(f"### Tries used: {st.session_state.attempts} / 5")
    
    # Input field
    user_guess = st.number_input("Guess a number (1-30):", min_value=1, max_value=30, step=1)
    
    if st.button("Check Guess", use_container_width=True):
        st.session_state.attempts += 1
        
        if user_guess == st.session_state.random_number:
            st.success(f"🎊 Correct! The number was {st.session_state.random_number}")
            st.balloons()
            st.session_state.game_over = True
        elif st.session_state.attempts >= 5:
            st.error(f"❌ Game Over! You've used all tries. The number was {st.session_state.random_number}.")
            st.session_state.game_over = True
        else:
            if user_guess < st.session_state.random_number:
                st.warning("Too low! Try a higher number.")
            else:
                st.warning("Too high! Try a lower number.")
else:
    st.info("The game has ended. Use the sidebar to start a new round!")
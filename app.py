import streamlit as st

# Classic Enigma I Rotor Wiring
ROTORS = {
    "I":   "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
    "II":  "AJDKSIRUXBLHWTMCQGZNPYFVOE",
    "III": "BDFHJLCPRTXVZNYEIWGAKMUSQO"
}
REFLECTOR = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class EnigmaEngine:
    def __init__(self, p1, p2, p3):
        self.p1, self.p2, self.p3 = p1, p2, p3

    def step(self):
        self.p1 = (self.p1 + 1) % 26
        if self.p1 == 0:
            self.p2 = (self.p2 + 1) % 26
            if self.p2 == 0:
                self.p3 = (self.p3 + 1) % 26

    def process_char(self, char):
        self.step()
        idx = (ALPHABET.index(char) + self.p1) % 26
        char = ROTORS["I"][idx]
        idx = (ALPHABET.index(char) + self.p2) % 26
        char = ROTORS["II"][idx]
        idx = (ALPHABET.index(char) + self.p3) % 26
        char = ROTORS["III"][idx]
        char = REFLECTOR[ALPHABET.index(char)]
        idx = (ROTORS["III"].index(char) - self.p3) % 26
        char = ALPHABET[idx]
        idx = (ROTORS["II"].index(char) - self.p2) % 26
        char = ALPHABET[idx]
        idx = (ROTORS["I"].index(char) - self.p1) % 26
        char = ALPHABET[idx]
        return char

st.title("Classic Enigma I Emulator")
p1 = st.sidebar.slider("Rotor 1 Start", 0, 25, 0)
p2 = st.sidebar.slider("Rotor 2 Start", 0, 25, 0)
p3 = st.sidebar.slider("Rotor 3 Start", 0, 25, 0)

# Separate inputs
col1, col2 = st.columns(2)

with col1:
    plaintext = st.text_input("Plaintext (to Encrypt):")
    if plaintext:
        engine = EnigmaEngine(p1, p2, p3)
        res = "".join([engine.process_char(c) for c in plaintext.upper() if c in ALPHABET])
        st.info(f"Ciphertext: {res}")

with col2:
    ciphertext = st.text_input("Ciphertext (to Decrypt):")
    if ciphertext:
        engine = EnigmaEngine(p1, p2, p3)
        res = "".join([engine.process_char(c) for c in ciphertext.upper() if c in ALPHABET])
        st.success(f"Plaintext: {res}")
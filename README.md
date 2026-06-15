# enigma-emulator

Project Overview
This is a functional virtual Enigma I machine built with Python and Streamlit. It replicates the core electro-mechanical logic of the 1930s German cipher machine, allowing users to encrypt plaintext and decrypt ciphertext using identical rotor settings.

How It Works
The emulator mimics the physical signal path and mechanical behavior of the original device:

Odometer-style Stepping: The engine implements a true mechanical stepping mechanism where the rotors advance with every keystroke, ensuring the encryption key changes for every character.

Symmetrical Encryption/Decryption: By replicating the machine's internal Reflector (Umkehrwalze), the emulator is self-reciprocal. You can encrypt a message, and by using the exact same rotor starting positions, you can decrypt the output back into the original plaintext.

Historical Fidelity: It uses the standard Enigma I rotor wiring configurations (I, II, and III) to maintain mathematical accuracy to the original device.

Features
Dual-Mode Interface: Separate, clear input fields for encryption and decryption.

Real-time Rotor Control: Interactive sliders to set the "Day Key" (initial rotor positions).

Authentic Mechanical Logic: Emulates the complex, non-linear transformation that made the Enigma a global cryptographic milestone.

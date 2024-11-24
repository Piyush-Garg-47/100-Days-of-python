print("the terminal was not working !!")

import win32com.client

def pronounce_names(names):
    # Create a speaker object using SAPI
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    for name in names:
        text = f"Shoutout to {name}"
        speaker.Speak(text)

# Corrected `if __name__` block
if __name__ == "__main__":
    names = ["Yasir", "Rahul", "Nishant", "Harry"]
    pronounce_names(names)

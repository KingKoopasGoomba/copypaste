import pyperclip
import keyboard

sentence_original = ["So", "you're", "going"]

sentence = sentence_original.copy()

def get_next_sentence():
    global sentence
    pyperclip.copy(sentence[0])
    del sentence[0]
    if len(sentence) == 0:
        sentence = sentence_original.copy()

keyboard.add_hotkey("ctrl + v", get_next_sentence)

keyboard.wait("F2")

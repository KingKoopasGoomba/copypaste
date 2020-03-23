import pyperclip
import keyboard

sentence_original = ["So you're going by 'Ganker' now nerd?",
            "Haha whats up douche bag, it's Tanner from Highschool.", 
            "Remember me?", 
            "Me and the guys used to give you a hard time in school.",
            "Sorry you were just an easy target lol.", 
            "I can see not much has changed.", 
            "Remember Sarah?", 
            "The girl you had a crush on?", 
            "Yeah we're married now.",
            "I make over 200k a year and drive a mustang GT.", 
            "I guess some things never change huh loser?", 
            "Nice catching up lol.",
            "Pathetic.."]

sentence = sentence_original.copy()

def get_next_sentence():
    global sentence
    pyperclip.copy(sentence[0])
    del sentence[0]
    if len(sentence) == 0:
        sentence = sentence_original.copy()

keyboard.add_hotkey("ctrl + v", get_next_sentence)

keyboard.wait("F2")

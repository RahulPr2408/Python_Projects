import curses
from curses import wrapper
import time
import random


def start_screen(stdscr):
	stdscr.clear()
	stdscr.addstr("Welcome to the Speed Typing Test!")
	stdscr.addstr("\nPress any key to begin!")
	stdscr.refresh()
	stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):
	stdscr.addstr(target)
	stdscr.addstr(1, 0, f"WPM: {wpm}")

	for i, char in enumerate(current):
		correct_char = target[i]
		color = curses.color_pair(1)
		if char != correct_char:
			color = curses.color_pair(2)

		stdscr.addstr(0, i, char, color)

def load_text():
	with open("wpm_typing_texts.txt", "r") as f:
		lines = f.readlines()
		return random.choice(lines).strip()

def wpm_test(stdscr):
	target_text = load_text()
	current_text = []
	wpm = 0
	start_time = time.time()
	stdscr.nodelay(True) # will run the code (I mean, will count the WPM if user stop typing.) 
  # because of this we have to put stdscr.getkey() into Try Except block to not crash our program.

	while True:
		time_elapsed = max(time.time() - start_time, 1)
		
    # len(current_text) / (time_elapsed / 60) would give me chars per minutes
    # (len(current_text) / (time_elapsed / 60)) / 5 would give me words per minutes (Why 5 because average length of a word is 5. Universal truth we have assumed)
		wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

		stdscr.clear()
		display_text(stdscr, target_text, current_text, wpm)
		stdscr.refresh()

		if "".join(current_text) == target_text: # will convert the current_text list into string
			stdscr.nodelay(False)
			break

		try:
			key = stdscr.getkey()
		except:
			continue

		if ord(key) == 27: # this would refrence to the Esc key ASCII value for Esc is 27.
			break

		if key in ("KEY_BACKSPACE", '\b', "\x7f"): # Backspace key would refer differently in different OS.
			if len(current_text) > 0:
				current_text.pop()
		elif len(current_text) < len(target_text):
			current_text.append(key)


def main(stdscr):
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

	start_screen(stdscr)
	while True:
		wpm_test(stdscr)
		stdscr.addstr(2, 0, "You completed the text! Press any key to continue...")
		key = stdscr.getkey()
		
		if ord(key) == 27:
			break

wrapper(main)
"""
Setup script for the mod manager.
"""
import os
import string
import sys
from typing import Optional

from pyuac import isUserAdmin, runAsAdmin


# --- CONSTANTS ---
RON_EXE_NAME = "ReadyOrNot.exe"
DEFAULT_RON_EXE_PATH = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\ReadyOr Not\\" + RON_EXE_NAME
ENABLED_PAKS_PATH = "ReadyOrNot\\Contents\\Paks\\"
DISABLED_PAKS_PATH = "ReadyOrNot\\Contents\\DisabledPaks\\"


def find_ron_exe() -> Optional[str]:
	"""
	Attempts to find the executable for ReadyOrNot.exe
	:return: The path to ReadyOrNot.exe (file not included) if found, None otherwise.
	"""
	print(
		"Ready or Not was not installed at default path, searching Windows for it...\n"
		"This will probably take a while."
	)

	# All available drives in Windows
	available_drives = ["%s:\\" % d for d in string.ascii_uppercase if os.path.exists("%s:\\" % d)]

	# Tries finding the exe, stops at the first match
	for drive in available_drives:
		for root, dirs, files in os.walk(drive):
			if RON_EXE_NAME in files:
				return root

	# If nothing was found, returns None
	return None


def main():
	"""
	Main code.
	"""
	# Gets the path of the Ready or Not exe
	if os.path.exists(DEFAULT_RON_EXE_PATH):
		ron_path = os.path.split(DEFAULT_RON_EXE_PATH)[0]

	# If RoN Path is not default, tries to locate it
	else:
		ron_path = find_ron_exe()

		# If the path to RoN was not found, exits with error
		if not ron_path:
			print("The path to the Ready or Not executable was not found. Please install Ready or Not and try again.")
			sys.exit()

	# Shows the user a message
	print(f"Located RoN folder at '{ron_path}'")

	# TODO Create config file

	# TODO Create DisabledPaks folder

	# TODO Run main.py -> Sets up all the .pak.json
	input("")


if __name__ == '__main__':
	if isUserAdmin():
		main()
	else:
		runAsAdmin()

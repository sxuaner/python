import os

path = ""

for file in os.listdir(path):
	os.rename(file, f"{file}.mp3")

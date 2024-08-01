.PHONY: install


pip3:
	sudo apt update -y && apt upgrade -y
	sudo apt install python3-pip -y

install:
	pip3 install discord.py
	pip3 install validators
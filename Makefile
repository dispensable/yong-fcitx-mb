env:
	sudo apt-get update -y && apt-get install fcitx-tools

mb:
	cd yong && python trans.py && txt2mb result.txt yong.mb



NAME=helloworldpy
all:
	node ./pbp/das/das2json.mjs $(NAME).drawio
	python3 main.py . '' main $(NAME).drawio.json

init:
	npm install yargs prompt-sync ohm-js @xmldom/xmldom

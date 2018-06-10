# ibc-nlu

Trainer
-------

launch the trainer using command: 
    rasa-nlu-trainer 
in the working directory.
It will start a browser that let you enter user utterances and help you extract
intents and entities.

project link: https://github.com/RasaHQ/rasa-nlu-trainer

Train the model
---------------

python3 -m rasa_nlu.train --path model --data data/nlu_data.json -- config nlu_config.json


Query
-----
curl -X POST localhost:5000/parse -d '{"q":"bye"}' | python -m json.tool

Server
------
python3 -m rasa_nlu.server --path model

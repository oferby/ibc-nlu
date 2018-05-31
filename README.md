# ibc-nlu

Query
-----
curl -X POST localhost:5000/parse -d '{"q":"bye"}' | python -m json.tool

Server
------
python3 -m rasa_nlu.server --path model

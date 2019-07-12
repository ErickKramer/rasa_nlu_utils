# rasa_nlu_utils
python scripts to generate training files for rasa

# Requirements:
* rasa 1.1.
* python >= 3.5

# Training rasa
- Inside rasa folder:
```
    rasa train nlu -c config.yml -u data/nlu.md
```

# Loading the model
```
    from rasa.nlu.model import Interpreter

    interpreter = Interpreter.load(path_to_model)
```

# Authors:
* Erick Kramer - erickkramer@gmail.com

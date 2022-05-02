This repository contains all the code and txt files I used in order to generate a script with openai, along with the results generated. 

The "raw_scripts" directory contains scripts as they are when they are copied from Youtube. 
You can replace this with closed captions from whatever videos you'd like.
In order to copy a closed caption script from Youtube, click the triple dots below the title, and then select "show transcript".
Copy this.

The "edited_scripts" directory contain all the scripts from the "raw_scripts" directory, but sanitized to get rid of timestamps.
In order to generate these edited scripts, run the "raw_to_processed" python script.

"all_data.json" and "all_intros.json" are json files containing data formatted to fine tune with.
To get these from your own files in "edited_scripts", run the "processed_to_json" python script.

In order to fine tune your model, follow the documentation on the openai website
https://beta.openai.com/docs/guides/fine-tuning
After creating an account and logging in, run 
  openai api fine_tunes.create -t all_data.json -m <BASE_MODEL>
    or 
  openai api fine_tunes.create -t all_intros.json -m <BASE_MODEL>
where <BASE_MODEL> is ada, babbage, curie, or davinci.

In order to generate results, again you can follow the openai documentation. 
Personally, I followed this formula:
  python3
  >>> import os
  >>> import openai
  >>> openai.Completion.create(model=<model_name>, prompt=<prompt>,max_tokens=<max_tokens>)

The "generated_scripts" directory contains a few scripts generated with this model.
The "Script 1" and "Script 2" were used in the Youtube video
  https://youtu.be/S8q-L4ZBV7c
which is the final result of this project.
"Unused Script" is just an interesting result.

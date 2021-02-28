# seinfeld-transcript-generator-rnn

An RNN that generates Seinfeld transcripts.

First run get_transcripts.py in order to download the transcripts of the tv show. I chose Seinfeld, but any other that's in the database will work.

Next run preprocess_transcripts.py in order to reduce the amount of blank spaces.

The model works, but it could definitely use some fine tuning (and more data).
Adjusting the temperature too low gets the net to output some words far more often than others (words such as "know", "don't", etc.)
I limited the number of epochs in order to reduce the training time.
Increasing the number of layers seemed to make the training loss move faster initially, but not get low enough.

The model as it is right now, outputs words and sentances that are very much in the style of Seinfeld, but don't make too much sense otherwise.
They are somewhat self-referential, but that could also be random chance.

It might be a good idea to tinker with the batch size, trying a different optimizer, adding a learning rate scheduler etc., and maybe
even data augmentation, since lack of data seems to be the biggest problem.

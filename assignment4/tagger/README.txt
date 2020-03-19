
To be able to run the code, please change the file path of training file and evaluation file in config.yaml in a line with your file path.

usage: run.py [-h] [--mode M] [--model MO] [--text T] [--gold G] [--config C]

A basic SVM-based POS-tagger. Accepts either .conllu or tab-delineated .txt
files for training.

optional arguments:
  -h, --help  show this help message and exit
  --mode M    Specifies the tagger mode: {train, tag, eval}.
  --model MO  Specifies the tagger mode: {svm, crf}.
  --text T    Tags a sentence string. Can only be called if '--mode tag' is
              specified.
  --gold G    Path to a gold-standard POS-tagging file. Can only be called if
              '--mode eval' is specified.
  --config C  A config .yaml file that specifies the train data, model output
              file, and number of folds for cross-validation.


Two models are explored and implemented in the tagger, svm and crf

----------------------------------------------------------------------------------------------------------------------------------

For svm, the commands are as following:

------------------------------------------------------Train the model ------------------------------------------------------------
python3 run.py --mode train  --config config.yaml --model svm

------------------------------------------------------Tag sentence or file -------------------------------------------------------
python3 run.py --mode tag  --text "it is a glass of wine" --config config.yaml --model svm
python3 run.py --mode tag  --text my_file.txt --config config.yaml --model svm

----------------------------------------------Evaluate the model against gold ----------------------------------------------------
python3 run.py --mode eval --gold "/Users/yonwu/NLP_Course/UD_English-EWT/en_ewt-ud-test.conllu" --config config.yaml --model svm

----------------------------------------------------------------------------------------------------------------------------------
For crf, the commands are as following:

------------------------------------------------------Train the model ------------------------------------------------------------
python3 run.py --mode train  --config config.yaml --model crf

------------------------------------------------------Tag sentence or file -------------------------------------------------------
python3 run.py --mode tag  --text "it is a glass of wine" --config config.yaml --model crf
python3 run.py --mode tag  --text my_file.txt --config config.yaml --model crf

----------------------------------------------Evaluate the model against gold ----------------------------------------------------
python3 run.py --mode eval --gold "/Users/yonwu/NLP_Course/UD_English-EWT/en_ewt-ud-test.conllu" --config config.yaml --model crf


Besides the implementation of an alternative model, It was attempted to change some of the features in the words_to_features function,
which is defined in pre_process.py. The original features are whether the word is at the beginning or the end of the sentence, lowercase
or uppercase, whether it is a digit, part of a title, the last two and last three characters of the word and if the following and the previous
word are lowercase, part of a titel or uppercase. Additionally, in order to improve the accuracy and to check for example for prefixes, the two
and three first characters of a word were taken into consideration as features. Also, another feature that was definied in trying to do so was
whether the first character of a word is an uppercase letter to improve the performance on proper nouns. However, adding some or all of these
features brought only a minor or no improvement at all to the already high accuracy. Thus it was settled on the original parameters.


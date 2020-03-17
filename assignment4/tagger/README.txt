
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

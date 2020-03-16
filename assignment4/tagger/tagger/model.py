from sklearn.svm import LinearSVC
from .pre_process import token_to_features
from .pre_process import load_dataset
import numpy as np
import pickle
import spacy
import time
import os
from sklearn.metrics import classification_report
import pandas
from sklearn.preprocessing import MultiLabelBinarizer

nlp = spacy.load("en_core_web_sm")


def fit_and_report(X, Y, cross_val=True, n_folds=5):
    svm = LinearSVC()

    if cross_val:
        from sklearn.model_selection import cross_val_score
        print(f"Doing {n_folds}-fold cross-validation.")
        scores = cross_val_score(svm, X, Y, cv=n_folds)
        print(f"{n_folds}-fold cross-validation results over training set:\n")
        print("Fold\tScore".expandtabs(15))
        for i in range(n_folds):
            print(f"{i + 1}\t{scores[i]:.3f}".expandtabs(15))
        print(f"Average\t{np.mean(scores):.3f}".expandtabs(15))

    print("Fitting model.")
    start_time = time.time()
    svm.fit(X, Y)
    end_time = time.time()
    print(f"Took {int(end_time - start_time)} seconds.")

    return svm


def save_model(model_and_vec, output_file):
    print(f"Saving model to {output_file}.")
    with open(output_file, "wb") as outfile:
        pickle.dump(model_and_vec, outfile)


def load_model(output_file):
    print(f"Loading model from {output_file}.")
    with open(output_file, "rb") as infile:
        model, vec = pickle.load(infile)

    return model, vec


def tag_sequence(sentence, model, vec):
    doc = nlp(sentence)
    tokenized_sent = [token.text for token in doc]
    featurized_sent = []
    for i, token in enumerate(tokenized_sent):
        featurized_sent.append(token_to_features(tokenized_sent, i))

    featurized_sent = vec.transform(featurized_sent)
    labels = model.predict(featurized_sent)
    tagged_sent = list(zip(tokenized_sent, labels))

    return tagged_sent


def print_tagged_sent(tagged_sent, if_text, file_name):
    if if_text:
        new_file = open(file_name + ".tag", "w")
        for token in tagged_sent:
            result = f"{token[0]}\t{token[1]}".expandtabs(15) + "\n"
            new_file.write(result)
        new_file.close()
    else:
        for token in tagged_sent:
            print(f"{token[0]}\t{token[1]}".expandtabs(15))


def check_input_text(input_text):
    if os.path.isfile(input_text):
        with open(input_text, "r") as infile:
            file_name = input_text.split(".")[0]
            sequence, if_text = infile.read().replace('\n', ''), True
    else:
        file_name = None
        sequence, if_text = input_text, False

    return sequence, if_text, file_name


def eval_model(gold_file, model, vec):
    sentences, gold_tags = extract_sentences_and_tags_from_gold(gold_file)

    list_of_predicted_tags = []
    for sentence in sentences:
        tags = []
        tagged_sent = tag_sequence(sentence, model, vec)
        for ts in tagged_sent[:]:
            tags.append(ts[1])
        list_of_predicted_tags.append(tags)
    true_tags = []
    test_tags = []
    for i in range(0, len(sentences) - 1):
        if len(list_of_predicted_tags[i]) == len(gold_tags[i]):
            true_tags.append(gold_tags[i])
            test_tags.append(list_of_predicted_tags[i])
        else:
            continue

    predicted = [x for j in test_tags for x in j]
    gold = [x for j in true_tags for x in j]

    c_matrix_report = classification_report(gold, predicted, output_dict=True)

    df = pandas.DataFrame(c_matrix_report).transpose()
    print(df)


def extract_sentences_and_tags_from_gold(gold_file):
    X, Y = load_dataset(gold_file)

    sentences = []
    for s in X:
        sentence = " ".join(s)
        sentences.append(sentence)

    list_of_tags = []
    for t in Y:
        list_of_tags.append(t)

    gold_tags = [x for j in list_of_tags for x in j]

    return sentences, list_of_tags


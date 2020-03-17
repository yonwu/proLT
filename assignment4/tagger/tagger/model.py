from sklearn.svm import LinearSVC
from .pre_process import token_to_features
from .pre_process import load_dataset
from .pre_process import sent2features
import numpy as np
import pickle
import spacy
import time
import os
from sklearn.metrics import classification_report
import pandas
import sklearn_crfsuite
from sklearn.metrics import make_scorer
from sklearn_crfsuite import metrics

nlp = spacy.load("en_core_web_sm")


def fit_and_report(X, Y, cross_val=True, n_folds=5, model_type="svm"):
    if model_type == "svm":
        model = LinearSVC()
    elif model_type == "crf":
        model = sklearn_crfsuite.CRF(
            algorithm='lbfgs',
            c1=0.1,
            c2=0.1,
            max_iterations=100)

    if cross_val:
        from sklearn.model_selection import cross_val_score
        print(f"Doing {n_folds}-fold cross-validation.")
        scores = cross_val_score(model, X, Y, cv=n_folds)
        print(f"{n_folds}-fold cross-validation results over training set:\n")
        print("Fold\tScore".expandtabs(15))
        for i in range(n_folds):
            print(f"{i + 1}\t{scores[i]:.3f}".expandtabs(15))
        print(f"Average\t{np.mean(scores):.3f}".expandtabs(15))

    print("Fitting model.")
    start_time = time.time()
    model.fit(X, Y)
    end_time = time.time()
    print(f"Took {int(end_time - start_time)} seconds.")

    return model


def save_model(model_and_vec, output_file):
    print(f"Saving model to {output_file}.")
    with open(output_file, "wb") as outfile:
        pickle.dump(model_and_vec, outfile)


def load_model(output_file):
    print(f"Loading model from {output_file}.")
    with open(output_file, "rb") as infile:
        model, vec = pickle.load(infile)

    return model, vec


def load_crf(output_file):
    print(f"Loading model from {output_file}.")
    with open(output_file, "rb") as infile:
        model = pickle.load(infile)

    return model


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


def tag_sequence_crf(sentence, model):
    doc = nlp(sentence)
    tokenized_sent = [token.text for token in doc]

    featurized_sent = sent2features(tokenized_sent)

    labels = model.predict([featurized_sent])

    tagged_sent = list(zip(tokenized_sent, labels[0]))

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
    toked_sentence, gold_tags = extract_tokens_and_tags_from_gold(gold_file)

    featurized_sent = []
    for i, token in enumerate(toked_sentence):
        featurized_sent.append(token_to_features(toked_sentence, i))

    featurized_sent = vec.transform(featurized_sent)
    predicted = model.predict(featurized_sent)

    c_matrix_report = classification_report(gold_tags, predicted, output_dict=True)

    df = pandas.DataFrame(c_matrix_report).transpose()
    print(df)


def eval_crf(gold_file, model):
    toked_sentence, gold_tags = extract_tokens_and_tags_from_gold(gold_file)

    featurized_sent = sent2features(toked_sentence)
    predicted = model.predict([featurized_sent])

    c_matrix_report = classification_report(gold_tags, predicted[0], output_dict=True)

    df = pandas.DataFrame(c_matrix_report).transpose()
    print(df)


def extract_tokens_and_tags_from_gold(gold_file):
    X, Y = load_dataset(gold_file)

    token_sentences = []
    for s in X:
        token_sentences.append(s)

    toked_sentence = [x for j in token_sentences for x in j]

    list_of_tags = []
    for t in Y:
        list_of_tags.append(t)

    gold_tags = [x for j in list_of_tags for x in j]

    return toked_sentence, gold_tags

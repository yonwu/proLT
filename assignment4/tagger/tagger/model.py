from sklearn.svm import LinearSVC
from .pre_process import token_to_features
import numpy as np
import pickle
import spacy
import time

nlp = spacy.load("en_core_web_sm")

def fit_and_report(X, Y, cross_val = True, n_folds=5):

    svm = LinearSVC()

    if cross_val:
        from sklearn.model_selection import cross_val_score
        print(f"Doing {n_folds}-fold cross-validation.")
        scores = cross_val_score(svm, X, Y, cv=n_folds)
        print(f"{n_folds}-fold cross-validation results over training set:\n")
        print("Fold\tScore".expandtabs(15))
        for i in range(n_folds):
            print(f"{i+1}\t{scores[i]:.3f}".expandtabs(15))
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

def tag_sentence(sentence, model, vec):
    doc = nlp(sentence)
    tokenized_sent = [token.text for token in doc]
    featurized_sent = []
    for i, token in enumerate(tokenized_sent):
        featurized_sent.append(token_to_features(tokenized_sent, i))

    featurized_sent = vec.transform(featurized_sent)
    labels = model.predict(featurized_sent)
    tagged_sent = list(zip(tokenized_sent, labels))

    return tagged_sent

def print_tagged_sent(tagged_sent):
    for token in tagged_sent:
        print(f"{token[0]}\t{token[1]}".expandtabs(15))


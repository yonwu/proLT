from sklearn.feature_extraction import DictVectorizer

def load_txt(file):
    X, Y = [], []
    with open(file, "r") as infile:
        sents = infile.read().split("\n\n")
        if sents[-1] == "":
            sents = sents[:-1]
        for sent in sents:
            words, tags = [], []
            lines = sent.split("\n")
            for line in lines:
                line = line.strip().split("\t")
                if len(line) != 2:
                    raise TabError("Tried to read .txt file, but did not find two columns.")
                else:
                    words.append(line[0])
                    tags.append(line[1])
            X.append(words)
            Y.append(tags)

    return X, Y

def load_conllu(file):
    X, Y = [], []
    with open(file, "r") as infile:
        sents = infile.read().split("\n\n")
        if sents[-1] == "":
            sents = sents[:-1]
        for sent in sents:
            words, tags = [], []
            lines = sent.split("\n")
            for line in lines:
                if line.startswith("#"):
                    continue
                line = line.strip().split("\t")
                if len(line) != 10:
                    raise TabError("Tried to read .txt file, but did not find ten columns.")
                else:
                    words.append(line[1])
                    tags.append(line[3])
            X.append(words)
            Y.append(tags)

    return X, Y

def load_dataset(file):
    if file.endswith(".conllu"):
        try:
            X, Y = load_conllu(file)
            return X, Y
        except TabError:
            print("Tried to read .txt file, but did not find ten columns.")
    else:
        try:
            X, Y = load_txt(file)
            return X, Y
        except TabError:
            print("Tried to read .txt file, but did not find two columns.")

def token_to_features(sent, i):
    word = sent[i]

    features = {
        'word.lower()': word.lower(),
        'word[-3:]': word[-3:],
        'word[-2:]': word[-2:],
        'word.isupper()': word.isupper(),
        'word.istitle()': word.istitle(),
        'word.isdigit()': word.isdigit(),
    }
    if i > 0:
        word1 = sent[i-1]
        features.update({
            '-1:word.lower()': word1.lower(),
            '-1:word.istitle()': word1.istitle(),
            '-1:word.isupper()': word1.isupper(),
        })
    else:
        features['BOS'] = True

    if i < len(sent)-1:
        word1 = sent[i+1]
        features.update({
            '+1:word.lower()': word1.lower(),
            '+1:word.istitle()': word1.istitle(),
            '+1:word.isupper()': word1.isupper(),
        })
    else:
        features['EOS'] = True

    return features

def prepare_data_for_training(X, Y):
    X_out, Y_out = [], []
    for i, sent in enumerate(X):
        for j, token in enumerate(sent):
            features = token_to_features(sent, j)
            X_out.append(features)
            Y_out.append(Y[i][j])

    return X_out, Y_out

def vectorize(X):
    vec = DictVectorizer()
    X_out = vec.fit_transform(X)

    return X_out, vec

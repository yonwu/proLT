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


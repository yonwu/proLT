from tagger import pre_process, model
import argparse
import yaml


def run(args):
    mode = args.mode
    model_type = args.model
    with open(args.config, "r") as yamlin:
        config = yaml.load(yamlin)
    if mode == "train":
        print(f"Training a model on {config['train_file']}.")
        X, Y = pre_process.load_dataset(config["train_file"])

        if model_type == "svm":
            X, Y = pre_process.prepare_data_for_training(X, Y)
            X, vec = pre_process.vectorize(X)
        if model_type == "crf":
            X = [pre_process.sent2features(s) for s in X]
            Y = [pre_process.sent2labels(s) for s in Y]

        classifier = model.fit_and_report(X, Y, config["crossval"], config["n_folds"], model_type)
        if model_type == "svm":
            model.save_model((classifier, vec), config["model_file"])
        if model_type == "crf":
            model.save_model(classifier, config["model_file"])
    elif mode == "tag":
        print(f"Tagging text using pretrained model: {config['train_file']}.")
        sequence, if_file, file_name = model.check_input_text(args.text)
        print(sequence)
        if model_type == "svm":
            classifier, vec = model.load_model(config["model_file"])
            tagged_sent = model.tag_sequence(sequence, classifier, vec)
        if model_type == "crf":
            classifier = model.load_crf(config["model_file"])
            tagged_sent = model.tag_sequence_crf(sequence, classifier)

        model.print_tagged_sent(tagged_sent, if_file, file_name)

    elif mode == "eval":
        print(f"Evaluating model on: {config['eval_file']}.")
        if model_type == "svm":
            classifier, vec = model.load_model(config["model_file"])
            model.eval_model(args.gold, classifier, vec)
        if model_type == "crf":
            classifier = model.load_crf(config["model_file"])
            model.eval_crf(args.gold, classifier)

    else:
        print(f"{args.mode} is an incompatible mode. Must be either 'train' or 'tag'.")


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(description=
                                     """
                                     A basic SVM-based POS-tagger.
                                     Accepts either .conllu or tab-delineated
                                     .txt files for training.
                                     """)

    PARSER.add_argument('--mode', metavar='M', type=str, help=
    """
                        Specifies the tagger mode: {train, tag, eval}.
                        """)
    PARSER.add_argument('--model', metavar='MO', type=str, help=
    """
                        Specifies the tagger mode: {svm, crf}.
                        """)
    PARSER.add_argument('--text', metavar='T', type=str, help=
    """
                        Tags a sentence string.
                        Can only be called if '--mode tag' is specified.
                        """)
    PARSER.add_argument('--gold', metavar='G', type=str, help=
    """
                        Path to a gold-standard POS-tagging file.
                        Can only be called if '--mode eval' is specified.
                        """)
    PARSER.add_argument('--config', metavar='C', type=str, help=
    """
                        A config .yaml file that specifies the train data,
                        model output file, and number of folds for cross-validation.
                        """)

    ARGS = PARSER.parse_args()

    run(ARGS)

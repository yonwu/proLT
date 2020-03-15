from tagger import pre_process, model
import argparse
import yaml

def run(args):
    mode = args.mode
    with open(args.config, "r") as yamlin:
        config = yaml.load(yamlin)
    if mode == "train":
        print(f"Training a model on {config['train_file']}.")
        X, Y = pre_process.load_dataset(config["train_file"])
        X, Y  = pre_process.prepare_data_for_training(X, Y)
        X, vec = pre_process.vectorize(X)
        svm = model.fit_and_report(X, Y, config["crossval"], config["n_folds"])
        model.save_model((svm, vec), config["model_file"])
    elif mode == "tag":
        print(f"Tagging text using pretrained model: {config['train_file']}.")
        svm, vec = model.load_model(config["model_file"])
        tagged_sent = model.tag_sentence(args.text, svm, vec)
        model.print_tagged_sent(tagged_sent)
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
    PARSER.add_argument('--text', metavar='T', type=str, help=
                        """
                        Tags a sentence string.
                        Can only be called if '--mode tag' is specified.
                        """)
    PARSER.add_argument('--config', metavar='C', type=str, help=
                        """
                        A config .yaml file that specifies the train data,
                        model output file, and number of folds for cross-validation.
                        """)

    ARGS = PARSER.parse_args()

    run(ARGS)
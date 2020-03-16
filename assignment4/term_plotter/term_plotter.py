import argparse
import pandas as pd
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
import os
import json

DEFAULT_PATH = "/Users/yonwu/proLT/assignment4/term_plotter/us_presidential_speeches/"

parser = argparse.ArgumentParser(description='plot certain terms.')

parser.add_argument('--terms', required=True, type=str, nargs='+', help='list of terms')

parser.add_argument('--title', required=False, type=str, help='plot title')

parser.add_argument('--path', required=False, type=str, help='target folder')

parser.add_argument('--output', required=False, type=str, help='output file name')

args = parser.parse_args()


class TooLongTermsException(Exception):

    def __init__(self, length):
        self.length = length

    def __str__(self):
        print("terms size: " + str(self.length) + "，larger than the limit size 5")


class TooLongTerm(Exception):

    def __init__(self, length):
        self.length = length

    def __str__(self):
        print("term size: " + str(self.length) + "，larger than the limit size 3")


def process_input(args):
    if args.terms:
        terms = args.terms
        if len(terms) > 5:
            raise TooLongTermsException(len(terms))
        for term in terms:
            if len(term.split(" ")) > 3:
                raise TooLongTerm(len(term))
    if args.title:
        title = args.title
    else:
        title = ""

    if args.path:
        path = args.path
    else:
        path = os.getcwd()

    if args.output:
        output = args.output
    else:
        output = '_'.join(s.replace(" ", "_") for s in args.terms) + ".png"

    return terms, title, path, output


def get_score_date_matrix(input_path, terms):
    speech_dir = input_path
    files = os.listdir(speech_dir)
    date_list = []
    speech_list = []
    size_docs = 0
    for file in files:
        with open(speech_dir + file, "r") as infile:
            speech = json.load(infile)
            date_list.append(speech["Date"])
            speech_list.append(speech["Speech"])
            size_docs = size_docs + 1

    df_date = pd.DataFrame({'Date': date_list})
    df_date['Date'] = pd.to_datetime(df_date.Date)

    cv = TfidfVectorizer(analyzer='word', stop_words='english', ngram_range=(1, 3))
    X = cv.fit_transform(speech_list)
    df_all_scores = pd.DataFrame(X.toarray(), columns=cv.get_feature_names())

    frames = []
    for term in terms:
        df_term = pd.df_term = pd.DataFrame({'term': [term] * size_docs})
        df_score = pd.DataFrame({'Score': df_all_scores[term]})
        concat_table = pd.concat([df_date, df_score, df_term], axis=1, sort=False)
        frames.append(concat_table)
    result = pd.concat(frames)
    return result


def plot_and_save_result(table, title, output):
    g = sns.lineplot(x="Date", y="Score", hue="term", data=table).set_title(title)
    fig = g.get_figure()
    fig.savefig(output)


if __name__ == "__main__":
    terms, title, path, output = process_input(args)
    table = get_score_date_matrix(path, terms)
    plot_and_save_result(table, title, output)


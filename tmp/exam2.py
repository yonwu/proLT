from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
from TonyDataset import X_test, X_train, Y_test, Y_train
from sklearn.metrics import classification_report
import pandas

vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

clf = LinearSVC()
clf.fit(X_train_vec, Y_train)

predicted = clf.predict(X_test_vec)
c_matrix_report = classification_report(Y_test, predicted, output_dict=True)

df = pandas.DataFrame(c_matrix_report).transpose()
print(df)

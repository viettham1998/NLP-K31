import argparse
import os
import pickle
import sys
from os.path import dirname, join, abspath
from time import time

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import LinearSVC
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.metrics import classification_report
from load_data import load_dataset


cwd = dirname(abspath(__file__))
sys.path.append(dirname(dirname(cwd)))


parser = argparse.ArgumentParser("trainAndTest.py")
parser.add_argument("--train", help="train data path", required=True)
parser.add_argument("--test", help="test data path", required=True)
parser.add_argument("-s", "--serialization-dir", help="directory in which to save the model and its logs",
                    required=True)
args = parser.parse_args()


def save_model(filename, clf):
    pickle.dump(clf, open(filename, 'wb'))


train_path = os.path.abspath(join(cwd, args.train))
test_path = os.path.abspath(join(cwd, args.test))
serialization_dir = os.path.abspath(join(cwd, args.serialization_dir))
print("Load data")
X_train, y_train = load_dataset(train_path)
target_names = list(set([i[0] for i in y_train]))

print("%d documents" % len(X_train))
print("%d categories" % len(target_names))

print("Training model")
t0 = time()
transformer = TfidfVectorizer(ngram_range=(1, 2), max_df=0.8)
ch2 = SelectKBest(chi2, k=500000)
X_train = transformer.fit_transform(X_train)
X_train = ch2.fit_transform(X_train, y_train)

y_transformer = LabelEncoder()
y_train = [item for sublist in y_train for item in sublist]
y_train = y_transformer.fit_transform(y_train)

model = LinearSVC(C=1)
estimator = model.fit(X_train, y_train)
t1 = time() - t0
print("Train time: %0.3fs" % t1)

#Test
print("Load data test")
X_test, y_test = load_dataset(test_path)
target_names1 = list(set([i[0] for i in y_test]))

print("%d documents" % len(X_test))
print("%d categories" % len(target_names1))

print("Test model")

y_pred = estimator.predict(X_test)
print(classification_report(y_test, y_pred, target_names=list(y_transformer.classes_)))
 

t0 = time()
save_model(serialization_dir + "/x_transformer.pkl", transformer)
save_model(serialization_dir + "/y_transformer.pkl", y_transformer)
save_model(serialization_dir + "/model.pkl", estimator)
save_model(serialization_dir + "/ch2.pkl", ch2)
t1 = time() - t0
print("Save model time: %0.3fs" % t1)

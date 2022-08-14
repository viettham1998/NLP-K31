from os.path import dirname, join
import pickle

from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score

from load_data import load_dataset

cwd = dirname(__file__)
x_transformer_file = open("/home/hvtham/classification/classification/data/root/x_transformer.pkl", "rb")
x_transformer = pickle.load(x_transformer_file)

ch2_file = open("/home/hvtham/classification/classification/data/root/ch2.pkl", "rb")
ch2 = pickle.load(ch2_file)

y_transformer_file = open("/home/hvtham/classification/classification/data/root/y_transformer.pkl", "rb")
y_transformer = pickle.load(y_transformer_file)

estimator_file = open("/home/hvtham/classification/classification/data/root/model.pkl", "rb")
estimator = pickle.load(estimator_file)

test_path = join(cwd, "data", "testVNTC.xlsx")
X_test, y_test = load_dataset(test_path)
y_test = [item for sublist in y_test for item in sublist]
X = x_transformer.transform(X_test)
X = ch2.transform(X)
y = estimator.predict(X)
y_pred = y_transformer.inverse_transform(y)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", round(accuracy, 4))
precision = precision_score(y_test, y_pred, average="micro")
print("Precision:", round(accuracy, 4))
recall = recall_score(y_test, y_pred, average="micro")
print("Recall:", round(accuracy, 4))
f1 = f1_score(y_test, y_pred, average="micro")
print("F1 Score:", round(accuracy, 4))

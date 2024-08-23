from sklearn.metrics import confusion_matrix

actual = [1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
predicted = [0, 1, 1, 1, 1, 0, 1, 0, 1, 0]

true_positives = 0
true_negatives = 0
false_positives = 0
false_negatives = 0


# -------------------- LA MATRIZ DE CONFUSIÓN HARDCODED-------------------------#

for i in range(len(predicted)):
  if actual[i] == predicted[i]:
    true_positives += 1
  if actual[i] == 0 and predicted[i] == 0:
    true_negatives += 1
  if actual[i] == 1 and predicted[i] == 0:
    false_negatives += 1
  if actual[i] == 0 and predicted[i] == 1:
    false_positives += 1

print(true_positives)
print(true_negatives)
print(false_positives)
print(false_negatives)

#-------------------- accuracy, recall, precision and F1 score HARDCODED------------------------#
conf_matrix = confusion_matrix(actual, predicted)
print()
print(conf_matrix)
accuracy = (true_positives + true_negatives) / (true_positives + true_negatives + false_positives + false_negatives)
print(accuracy)
recall = true_positives/(true_positives + false_negatives)
print(recall)
precision = true_positives/(true_positives + false_positives)
print(precision)
f_1 = 2 * (precision * recall) / (precision + recall)
print(f_1)

#-------------------- accuracy, recall, precision and F1 score using scikit----------------------#
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

print(accuracy_score(actual,predicted))
print(recall_score(actual,predicted))
print(precision_score(actual,predicted))
print(f1_score(actual,predicted))

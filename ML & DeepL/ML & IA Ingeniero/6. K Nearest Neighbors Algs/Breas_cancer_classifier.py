from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

breast_cancer_data = load_breast_cancer()
# print(breast_cancer_data.data)
# print(breast_cancer_data.target)
# print(breast_cancer_data.target_names)

training_data, validation_data, training_labels, validation_labels = train_test_split(breast_cancer_data.data, breast_cancer_data.target, test_size = 0.2, random_state = 100)

print(training_data)
print(training_labels)

score_max = 0
k_max = 0
k_list = range(1,100)
accuracies = []

for k in range(100):
  if k != 0:
    classifier = KNeighborsClassifier(k)
    classifier.fit(training_data,training_labels)
    accuracies.append(classifier.score(validation_data,validation_labels))
    if classifier.score(validation_data,validation_labels) > score_max:
     score_max = classifier.score(validation_data,validation_labels) 
     k_max = k


print(k_max,score_max) #23 0.9649
print(len(k_list))
print(len(accuracies))
plt.plot(k_list,accuracies)
plt.title('Breast Cancer Classifier Accuracy')
plt.xlabel('k')
plt.ylabel('Validation Accuracy')
plt.show()
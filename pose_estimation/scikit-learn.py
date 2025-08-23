#!/usr/bin/env python3

"""this document is one of many codes for learning and applying scikit
which offers traditional machine learning tools, like classification, regression ,
clustering. These tools can help build simple feedback models. Good
for classsifying and detecting good vs bad form in our future application by
using derived metrics(angles, velocity, symmetry). It supports pipelines, train-test splits
and model evaluation."""

from sklearn.ensemble import RandomForestClassifier

X = [[95], [88], [90], [92], [87]] #patterns obtained
y = [1, 0, 1, 1, 0] #True and False values from X inputs

clf = RandomForestClassifier(random_state=0)
clf.fit(X, y)

# Predict on new angle
print("Form is good?" , clf.predict([[89]])[0])

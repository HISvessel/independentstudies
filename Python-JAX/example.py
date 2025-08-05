#!/usr/bin/python3

"""this is a sample function of how neural networks are trained and how information
is parsed and passed from one layer to the next to the next. """

import jax
import jax.numpy as jnp
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler


data = load_iris()
X = data.data
y = data.target.reshape(-1, 1)

encoder = OneHotEncoder(sparse_output=False)
y = encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, 0.2)

scalar = StandardScaler()
X_train = scalar.fit_transform(X_train)
X_test = scalar.transform(X_test)

def init_params(input_dim, hidden_dim1, hidden_dim2, output_dim, random_key):
    randowm_key = jax.random.split(randowm_key, 3)
    W1 = jax.random.normal(randowm_key[0], (input_dim, hidden_dim1))
    b1 = jnp.zeros((hidden_dim1,))


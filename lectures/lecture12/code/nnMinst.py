import matplotlib.pyplot as plt
from sklearn.datasets import fetch_mldata
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
mnist = fetch_mldata("MNIST original")
# rescale the data, use the traditional train/test split
X, y = mnist.data, mnist.target


# transform X for unit scaling
ss = StandardScaler()
X = ss.fit_transform(X)

# create test train set
X_train, X_test = X[:60000], X[60000:]
y_train, y_test = y[:60000], y[60000:]

# set up my layers
layers = (256, 128, 64, 32, 16, 4)

# load MLP model
mlp = MLPClassifier(hidden_layer_sizes=layers, max_iter=1000, alpha=1e-4,
                solver='adam', verbose=10, tol=0, random_state=13,
                learning_rate='adaptive')
mlp.fit(X_train,y_train)

# score the  model
print(mlp.score(X_test,y_test))

import numpy as np
class LinearRegression():
    def __init__(self):
        self.weights = None
        self.bias = 0
    def fit(self, X, y, lr = 0.01, epochs = 1000):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(epochs):
            y_pred = np.dot(X, self.weights) + self.bias
            dw = (1/n_samples) * np.dot(X.T, (y_pred - y))
            db = (1/n_samples) * np.sum(y_pred - y)

            self.weights -= lr * dw
            self.bias -= lr * db
    def predict(self, X):
        return np.dot(X, self.weights) + self.bias
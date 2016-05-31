import numpy as np
import tensorflow as tf
session = tf.InteractiveSession()

X = tf.constant(np.eye(10000))
Y = tf.constant(np.random.randn(10000, 300))

Z = tf.matmul(X, Y)
Z.eval()

session.close()

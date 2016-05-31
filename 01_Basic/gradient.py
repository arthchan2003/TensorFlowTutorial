'''
'''
import tensorflow as tf
import numpy
rng = numpy.random


# tf Graph Input
X = tf.constant(3)
Y = tf.constant(2)

Z = X * X + 2
Z1 = X * X + 2 * X + 7

# gradient
grad = tf.gradients(Z, [X])
grad1 = tf.gradients(Z1, [X])

# Launch the graph
with tf.Session() as sess:
    print(sess.run(grad))
    print(sess.run(grad1))


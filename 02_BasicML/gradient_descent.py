import tensorflow as tf
import numpy as np

# Arthur This is an example I found from learningtensorflow.com and
# the goal is to see if you can recover the regression from the
# simulated data.  I changed quite a few of the values. I also use
# RMSPropOptimizer instead.

# x and y are placeholders for our training data
x = tf.placeholder("float")
y = tf.placeholder("float")
w = tf.Variable([1.0, 2.0], name="w")
y_model = tf.mul(x, w[0]) + w[1]

error = tf.square(y - y_model)
train_op = tf.train.RMSPropOptimizer(0.01).minimize(error)

model = tf.initialize_all_variables()

with tf.Session() as session:
    session.run(model)
    for i in range(10000):
        x_value = np.random.rand()
        y_value = x_value * 3 + 10
        session.run(train_op, feed_dict={x: x_value, y: y_value})

    w_value = session.run(w)
    print("Predicted model: {a:.3f}x + {b:.3f}".format(a=w_value[0], b=w_value[1]))


import tensorflow as tf


import numpy as np
data = np.random.randint(1000, size=10000)
#data = np.random.randint(10, size=10)

#x = tf.Variable(data, name='x')
y = tf.Variable(5 * data * data - 3 * data + 15, name='y')


model = tf.initialize_all_variables()

with tf.Session() as session:
    session.run(model)
    print(session.run(y))


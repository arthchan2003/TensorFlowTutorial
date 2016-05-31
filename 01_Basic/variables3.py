import tensorflow as tf
import numpy as np

#Now this is a more interesting example,
#We first generate some random integer
#and put it into np array x, then we generate
#y = x^2 + 6 * x + 1 using Tensorflow.

x = np.random.randint(100, size=100)

print "x:"
print (x)

y = tf.Variable(x * x + 6 * x + 1, name='y')

model = tf.initialize_all_variables()

print "y:"
with tf.Session() as session:
    session.run(model)
    print(session.run(y))


import tensorflow as tf

session = tf.InteractiveSession()

x = tf.constant(list(range(10)))


print(x.eval())
session.close()

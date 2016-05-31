import tensorflow as tf

session = tf.InteractiveSession()

x = tf.constant(list(range(10))) #Perhaps tf.range(1,10) is more idiomatic.

print(x.eval())
session.close()

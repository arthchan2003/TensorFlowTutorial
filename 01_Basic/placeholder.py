import tensorflow as tf

#In TF, a placeholder is simply a variable we want to initialize at
#data execution. For example, we declare a place holder which can hold 6 float values.

x = tf.placeholder("float", 6)
y = x * 2

with tf.Session() as session:
    print(session.run(y, feed_dict={x: [1, 2, 3, 4, 5, 6]}))


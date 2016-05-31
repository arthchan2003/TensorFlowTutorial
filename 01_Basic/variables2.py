import tensorflow as tf

#This is similar to the first example. But you can now sum an array.

x = tf.constant([35, 40, 45], name='x')
y = tf.Variable(x + [5, 3, 1], name='y')


model = tf.initialize_all_variables()

with tf.Session() as session:
    session.run(model)
    print(session.run(y))


import tensorflow as tf


x = tf.constant([35, 40, 45], name='x')
y = tf.Variable(x + [5, 3, 1], name='y')


model = tf.initialize_all_variables()

with tf.Session() as session:
    session.run(model)
    print(session.run(y))


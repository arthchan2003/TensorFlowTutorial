import tensorflow as tf

#You can also declare an array as a constant.
x = tf.constant([35, 40, 45], name='x')

#Now we are doing something different, y is a TF variable. Its
#evaluation would depend on another TF constant or TF variable.

y = tf.Variable(x + 5, name='y')

model = tf.initialize_all_variables()

with tf.Session() as session:
    session.run(model)
    print(session.run(y))


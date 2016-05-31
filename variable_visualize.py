import tensorflow as tf

x = tf.constant(35, name='x')
print(x)
y = tf.Variable(x + 5, name='y')

with tf.Session() as session:
    merged = tf.merge_all_summaries()
    writer = tf.train.SummaryWriter("./basic", session.graph_def)
    model = tf.initialize_all_variables()
    session.run(model)
    print(session.run(y))

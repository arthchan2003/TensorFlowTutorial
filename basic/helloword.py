'''
Hello World
'''

import tensorflow as tf

#Basic
#tensorflow computation is described by a computation graph.
#clients usually create a computation graph through python. 

#Create a string constant. In the parlance of tensorflow, you are
#creating a a tensor. In tensorflow, you can create by the tf.constant()

hello = tf.constant('Hello, World!')

#You "run" something in tensorflow by starting a session.  Or as the
#TF's whitepaper would say you "interact with TensorFlow system" by
#create a session.

sess = tf.Session()

print sess.run(hello)

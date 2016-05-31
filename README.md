# (Under Construction)

# TensorFlowTutorial

A tutorial on TensorFlow I prepared for general public.  For now, I
borrowed several scripts from aymericdamien's TensorFlow Example,
learningtensorflow.com as well as Tensorflow's original tutorial.

I don't much idea where it is heading - for the most part I might
want to create a set of tutorial which allows Tensorflow beginners to
grok from basic operations to more advanced ideas which one can find
in NN papers.

# Other Very Good Tutorials to Help You Start

* [The TensorFlow original tutorial.](https://www.tensorflow.org/)
* [TensorFlow Examples.](https://github.com/aymericdamien/TensorFlow-Examples)
* [TFLearn.](https://github.com/tflearn/tflearn)
* [LearningTensorFlow](http://learningtensorflow.com/examples/)
* [The TensorFlow White paper](http://download.tensorflow.org/paper/whitepaper2015.pdf)
* [The TensorFlow paper] http://arxiv.org/pdf/1603.04467v2.pdf

# Basic Installation

  On Ubuntu
  The fastest way to install for a CPU-version is
  1, Download anaconda python.
  2, conda install upgrade <tensorflow.whl> file.

  Also see the installation page from Tensorflow.
      

# Testing your package

      python

      >>> import tensorflow as tf
      >>> hello = tf.constant('Hello World')
      >>> sess = tf.Session()
      >>> print sess.run(hello)
      Hello World

# Hello World

* [Hello World] (./TensorFlowTutorial/01_Basic/helloword.py)
                              
# Basics - Using Constants, Variables

* [A Constant Array + A Constant]  (./TensorFlowTutorial/01_Basic/variables1.py)
* [A Constant Array + A Constant array]  (./TensorFlowTutorial/01_Basic/variables2.py)
* [Generate random array and a function of it]  (./TensorFlowTutorial/01_Basic/variables3.py)
* [A placeholder] (./TensorFlowTutorial/01_Basic/placeholder.py)

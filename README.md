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
* [The TensorFlow paper] (http://arxiv.org/pdf/1603.04467v2.pdf)

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

* [Hello World] (./01_Basic/helloword.py)
                              
# Basics - Using Constants, Variables

* [A Constant Array + A Constant]  (./01_Basic/variables1.py)
* [A Constant Array + A Constant array]  (./01_Basic/variables2.py)
* [Generate random array and a function of it]  (./01_Basic/variables3.py)
* [A placeholder] (./01_Basic/placeholder.py)
* [Calculate the Gradient] (./01_Basic/gradient.py)
* Also check out
  * [Americ Damien's more complicated example ](https://github.com/aymericdamien/TensorFlow-Examples/blob/master/examples/1_Introduction/basic_operations.py) 
  * [Matrix multiplication ] (./01_Basic/matrix_mul.py)
  * [Loop] (./01_Basic/variable_loopy.py)
  * [While Loop] (./01_Basic/whileloop.py)

# Basic Machine Learning
* [Simple Gradient Descent Example] (./02_BasicML/gradient_descent.py)
* [Basic Linear Regression] (./02_BasicML/linear_regression.py)
  * It is a matplot-free version of [Americ Damien's] (https://github.com/aymericdamien/TensorFlow-Examples/blob/master/examples/2_BasicModels/linear_regression.py)
* [Americ Damien's Logistic Regression] (https://github.com/aymericdamien/TensorFlow-Examples/blob/master/examples/2_BasicModels/logistic_regression.py)

# Neural Networks on MNIST




# <center>Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow</center>

## Ch11 Exercises Answers

1. **Is it OK to initialize all the weights to the same value as long as that value is selected randomly using He initialization?**

   No, weights should be sampled independently; they should not have the same initial value. One important goal of sampling weights randomly is to break symmetry: if all the weights have the same initial value, even if that value is not zero, then symmetry is not broken (i.e., all neurons in a given layer are equiva‐lent), and backpropagation will be unable to break it.

2. **Is it OK to initialize the bias terms to 0?**

   Yes, it does not make much difference.

4. **In which cases would you want to use each of the following activation functions: SELU, leaky ReLU (and its variants), ReLU, tanh, logistic, and softmax?**
   - SELU - Used as default.
   - Leaaky ReLU - Neural network will be as fast as possible.
   - ReLU - Many people's preferred option.
   - Logistic Activation Function - Used in the output layer for binary classification.


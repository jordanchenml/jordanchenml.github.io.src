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

5. **What may happen if you set the momentum hyperparameter too close to 1 (e.g., 0.99999) when using an SGD optimizer?**

   If you set the momentum hyperparameter too close to 1 (e.g., 0.99999) when using an SGD optimizer, it will take much longer to converge than with a smaller momentum value.

6. **Name three ways you can produce a sparse model.**

   One way to produce a sparse model (i.e., with most weights equal to zero) is to train the model normally, then zero out tiny weights. For more sparsity, you can apply l1 regularization during training, which pushes the optimizer toward spar‐ sity. A third option is to use the TensorFlow Model Optimization Toolkit.

7. **Does dropout slow down training? Does it slow down inference (i.e., making predictions on new instances)? What about MC Dropout?**

   Yes, dropout does slow down training, in general roughly by a factor of two. However, it has no impact on inference speed since it is only turned on during training. MC Dropout is exactly like dropout during training, but it is still active during inference, so each inference is slowed down slightly. More importantly, when using MC Dropout you generally want to run inference 10 times or more to get better predictions. This means that making predictions is slowed down by a factor of 10 or more.

8. **Practice training a deep neural network on the CIFAR10 image dataset: **

   1. **Build a DNN with 20 hidden layers of 100 neurons each (that’s too many, but it’s the point of this exercise). Use He initialization and the ELU activation function.**

      ```python
      keras.backend.clear_session()
      tf.random.set_seed(9527)
      np.random.seed(9527)
      
      model = tf.model.Sequential()
      model.add(keras.layer.Flatten(input_shape=[32, 32, 3]))
      for _ in range(20):
          model.add(keras.layer.Dense(100,
                                         activation="elu",
                                         kernel_initializer="he_normal"))
      ```

   2. **Using Nadam optimization and early stopping, train the network on the CIFAR10 dataset. You can load it with keras.datasets.cifar10.load_ data(). The dataset is composed of 60,000 32 × 32–pixel color images (50,000 for training, 10,000 for testing) with 10 classes, so you’ll need a softmax out‐put layer with 10 neurons. Remember to search for the right learning rate each time you change the model’s architecture or hyperparameters.**

      ```python
      model.add(keras.layer.Dense(10, activation="softmax"))
      
      optimizer = keras.optimizers.Nadam(lr=5e-5)
      model.compile(loss="sparse_categorical_crossentropy",
                    optimizer=optimizer,
                    metrics=["accuracy"])
      ```

      ```python
      (X_train_full, y_train_full), (X_test, y_test) = keras.datasets.cifar10.load_data()
      X_train = X_train_full[5000:]
      y_train = y_train_full[5000:]
      X_valid = X_train_full[:5000]
      y_valid = y_train_full[:5000]
      ```

      ```python
      early_stopping_cb = keras.callbacks.EarlyStopping(patience=20)
      model_checkpoint_cb = keras.callbacks.ModelCheckpoint("my_cifar10_model.h5",
                                                               save_best_only=True)
      run_index = 1
      run_logdir = os.join.path(od.curdir, "my_cifar10_logs", "run_{:03d}".format(run_index))
      tensorboard_cb = keras.callbacks.Tensorboard(run_logdir)
      callbacks = [early_stopping_cb, model_checkpoint_cb, tensorboard_cb]
      ```

      ```
      %tensorboard --logdir=./my_cifar10_logs --port=6006
      ```

      ```python
      model.fit(X_train, 
                y_train,
                epoch=100,
                validation_data=(X_valid, y_valid),
                callbacks=callbacks)
      ```

      ```python
      model = keras.models.load_model("my_cifar10_model.h5")
      model.evaluate(X_valid, y_valid)
      ```

      > 5000/5000 [==============================] - 0s 65us/sample - loss: 1.5099 - accuracy: 0.4736
      >
      > [1.5099372177124024, 0.4736]

   3. **Now try adding Batch Normalization and compare the learning curves:**

      ```python
      keras.backend.clear_session()
      tf.random.set_seed(9527)
      np.random.seed(9527)
      
      model = tf.model.Sequential()
      model.add(keras.layer.Flatten(input_shape=[32, 32, 3]))
      model.add(keras,layer.BatchNormalization())
      for _ in range(20):
          model.add(keras.layer.Dense(100, kernel_initializer="he_normal"))
          model.add(keras,layer.BatchNormalization())
          model.add(keras,layer.Activation("elu"))
      model.add(keras.layer.Dense(10, activation="softmax"))
      
      optimizer = keras.optimizers.Nadam(lr=5e-4)
      model.compile(loss="sparse_categorical_crossentropy",
                    optimizer=optimizer,
                    metrics=["accuracy"])
      
      early_stopping_cb = keras.callbacks.EarlyStopping(patience=20)
      model_checkpoint_cb = keras.callbacks.ModelCheckpoint("my_cifar10_bn_model.h5",
                                                               save_best_only=True)
      run_index = 1
      run_logdir = os.join.path(od.curdir, "my_cifar10_logs", "run_bn_{:03d}".format(run_index))
      tensorboard_cb = keras.callbacks.Tensorboard(run_logdir)
      callbacks = [early_stopping_cb, model_checkpoint_cb, tensorboard_cb]
      
      model.fit(X_train, y_train, epochs=100,
                validation_data=(X_valid, y_valid),
                callbacks=callbacks)
      
      model = keras.models.load_model("my_cifar10_bn_model.h5")
      model.evaluate(X_valid, y_valid)
      ```

      > 5000/5000 [==============================] - 1s 157us/sample - loss: 1.3054 - accuracy: 0.5506
      >
      > [1.305354326057434, 0.5506]

      - **Is it converging faster than before?**

        Yes,  the number of epochs was reduced by 50%

      - **Does it produce a better model?**

        Yes! The final model is also much better, with 55% accuracy instead of 47%.

      - **How does it affect training speed?**

        Overall, the training time (wall time) was shortened by 30%, but each epoch took about 16s about 10s.

   4. **Try replacing Batch Normalization with SELU, and make the necessary adjustments to ensure the network self-normalizes (i.e., standardize the input features, use LeCun normal initialization, make sure the DNN contains only a sequence of dense layers, etc.).**

      

      ```python
      keras.backend.clear_session()
      tf.random.set_seed(9527)
      np.random.seed(9527)
      
      model = tf.model.Sequential()
      model.add(keras.layer.Flatten(input_shape=[32, 32, 3]))
      model.add(keras,layer.BatchNormalization())
      for _ in range(20):
          model.add(keras.layer.Dense(100,
                                         kernel_initializer="lecun_normal",
                                         activation="selu"))
      model.add(keras.layer.Dense(10, activation="softmax"))
      
      optimizer = keras.optimizers.Nadam(lr=7e-4)
      model.compile(loss="sparse_categorical_crossentropy",
                    optimizer=optimizer,
                    metrics=["accuracy"])
      
      early_stopping_cb = keras.callbacks.EarlyStopping(patience=20)
      model_checkpoint_cb = keras.callbacks.ModelCheckpoint("my_cifar10_selu_model.h5", save_best_only=True)
      run_index = 1
      run_logdir = os.path.join(os.curdir, "my_cifar10_logs", "run_selu_{:03d}".format(run_index))
      tensorboard_cb = keras.callbacks.TensorBoard(run_logdir)
      callbacks = [early_stopping_cb, model_checkpoint_cb, tensorboard_cb]
      
      X_means = X_train.mean(axis=0)
      X_stds = X_train.std(axis=0)
      X_train_scaled = (X_train - X_means) / X_stds
      X_valid_scaled = (X_valid - X_means) / X_stds
      X_test_scaled = (X_test - X_means) / X_stds
      
      model.fit(X_train_scaled, y_train, epochs=100,
                validation_data=(X_valid_scaled, y_valid),
                callbacks=callbacks)
      
      model = keras.models.load_model("my_cifar10_selu_model.h5")
      model.evaluate(X_valid_scaled, y_valid)
      ```

      ```
      model = keras.models.load_model("my_cifar10_selu_model.h5")
      model.evaluate(X_valid_scaled, y_valid)
      ```

      > 5000/5000 [==============================] - 0s 74us/sample - loss: 1.4626 - accuracy: 0.5140
      >
      > [1.462584439086914, 0.514]

   5. **Try regularizing the model with alpha dropout. Then, without retraining your model, see if you can achieve better accuracy using MC Dropout.**

      ```python
      keras.backend.clear_session()
      tf.random.set_seed(9527)
      np.random.seed(9527)
      
      model = tf.model.Sequential()
      model.add(keras.layer.Flatten(input_shape=[32, 32, 3]))
      model.add(keras,layer.BatchNormalization())
      for _ in range(20):
          model.add(keras.layer.Dense(100,
                                         kernel_initializer="lecun_normal",
                                         activation="selu"))
      model.add(keras.layers.AlphaDropout(rate=0.1))
      model.add(keras.layers.Dense(10, activation="softmax"))
      
      optimizer = keras.optimizers.Nadam(lr=5e-4)
      model.compile(loss="sparse_categorical_crossentropy",
                    optimizer=optimizer,
                    metrics=["accuracy"])
      
      early_stopping_cb = keras.callbacks.EarlyStopping(patience=20)
      model_checkpoint_cb = keras.callbacks.ModelCheckpoint("my_cifar10_alpha_dropout_model.h5", save_best_only=True)
      run_index = 1 # increment every time you train the model
      run_logdir = os.path.join(os.curdir, "my_cifar10_logs", "run_alpha_dropout_{:03d}".format(run_index))
      tensorboard_cb = keras.callbacks.TensorBoard(run_logdir)
      callbacks = [early_stopping_cb, model_checkpoint_cb, tensorboard_cb]
      
      X_means = X_train.mean(axis=0)
      X_stds = X_train.std(axis=0)
      X_train_scaled = (X_train - X_means) / X_stds
      X_valid_scaled = (X_valid - X_means) / X_stds
      X_test_scaled = (X_test - X_means) / X_stds
      
      model.fit(X_train_scaled, y_train, epochs=100,
                validation_data=(X_valid_scaled, y_valid),
                callbacks=callbacks)
      
      model = keras.models.load_model("my_cifar10_alpha_dropout_model.h5")
      model.evaluate(X_valid_scaled, y_valid)
      ```

      > 5000/5000 [==============================] - 0s 71us/sample - loss: 1.4974 - accuracy: 0.5082
      >
      > [1.4974345008850098, 0.5082]

      ```python
      class MCAlphaDropout(keras.layers.AlphaDropout):
          def call(self, inputs):
              return super().call(inputs, training=True)
      ```

      ```python
      mc_model = keras.models.Sequential([
      	MCAlphaDropout(layer.rate) if isinstance(layer, keras.layers.AlphaDropout) else layer
      	for layer in model.layers
      ])
      ```

      ```python
      def mc_dropout_predict_probas(mc_model, X, n_samples=10):
          Y_probas = [mc_model.predict(X) for sample in range(n_samples)]
          return np.mean(Y_probas, axis=1)
      def mc_dropout_predict_classes(mc_model, X, n_samples=10):
          Y_probas = mc_dropout_predict_probas(mc_model, X, n_samples)
          return np.argmax(Y_probas, axis=1)
      ```

      ```python
      keras.backend.clear_session()
      tf.random.set_seed(9527)
      np.random.seed(9527)
      
      y_pred = mc_dropout_predict_classes(mc_model, X_valid_scaled)
      accuracy = np.mean(y_pred == y_valid[:, 0])
      accuracy
      ```

      > 0.5094

      We only get virtually no accuracy improvement in this case (from 50.8% to 50.9%).

      So the best model we got in this exercise is the Batch Normalization model.


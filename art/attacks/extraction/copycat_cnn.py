# MIT License
#
# Copyright (C) IBM Corporation 2018
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
# Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""
This module implements the copycat cnn attack `CopycatCNN`.

| Paper link: https://arxiv.org/abs/1806.05476
"""
from __future__ import absolute_import, division, print_function, unicode_literals

import logging

import numpy as np

from art import NUMPY_DTYPE
from art.attacks.attack import Attack


logger = logging.getLogger(__name__)


class CopycatCNN(Attack):
    """
    Implementation of the copycat cnn attack from Jacson et al. (2018).

    | Paper link: https://arxiv.org/abs/1806.05476
    """
    attack_params = Attack.attack_params + ['batch_size', 'nb_epochs', 'nb_stolen']

    def __init__(self, classifier, batch_size=1, nb_epochs=10, nb_stolen=1):
        """
        Create a copycat cnn attack instance.

        :param classifier: A victim classifier.
        :type classifier: :class:`.Classifier`
        :param batch_size: Size of batches.
        :type batch_size: `int`
        :param nb_epochs: Number of epochs to use for training.
        :type nb_epochs: `int`
        :param nb_stolen: Number of examples to be stolen.
        :type nb_stolen: `int`
        """
        super(CopycatCNN, self).__init__(classifier=classifier)

        params = {'batch_size': batch_size,
                  'nb_epochs': nb_epochs,
                  'nb_stolen': nb_stolen}
        self.set_params(**params)

    def generate(self, x, y=None, **kwargs):
        """
        Generate a thieved classifier.

        :param x: An array with the source input to the victim classifier.
        :type x: `np.ndarray`
        :param y: Target values (class labels) one-hot-encoded of shape (nb_samples, nb_classes) or indices of shape
                  (nb_samples,). Not used in this attack.
        :type y: `np.ndarray` or `None`
        :param thieved_classifier: A thieved classifier to be stolen.
        :type thieved_classifier: :class:`.Classifier`

        :return: The stolen classifier.
        :rtype: :class:`.Classifier`
        """
        # Warning to users if y is not None
        if y is not None:
            logger.warning("This attack does not use the provided label y.")

        # Select data to



    def set_params(self, **kwargs):
        """
        Take in a dictionary of parameters and applies attack-specific checks before saving them as attributes.

        :param nb_epochs: Number of epochs to use for training.
        :type nb_epochs: `int`
        """
        # Save attack-specific parameters
        super(CopycatCNN, self).set_params(**kwargs)

        if not isinstance(self.nb_epochs, (int, np.int)) or self.nb_epochs <= 0:
            raise ValueError("The number of epochs must be a positive integer.")

        return True

import numpy as np


class EarlyStopper:
    """
    early stopping the training based on
    validation loss
    Parameters
    patience: Number of epochs with no improvement after which training will be stopped.
    min_delta for validation loss : an absolute change of less than min_delta, will count as no improvement.
    """
    def __init__(self, patience=50):
        self.patience = patience
        self.counter = 0
        self.min_validation_loss = np.inf

    def early_stop_validation_loss(self, validation_loss):
        if validation_loss < self.min_validation_loss:
            self.min_validation_loss = validation_loss
            self.counter = 0
            return
        self.counter += 1
        if self.counter >= self.patience:
            return True

import pandas as pd
import numpy as np
import json
import tensorflow as tf
import tensorflow_text as text

tf.get_logger().setLevel('ERROR')

def predict_many(mdl, desc, service_decoder):
    """
    Predicts labels and probabilities for multiple descriptions using a trained model.

    Parameters:
        mdl (object): The trained model used for prediction.
        desc (array-like): The input descriptions to be predicted.
        service_decoder (dictionary): A dictionary of service offerings corresponding to the model's output.

    Returns:
        tuple: A tuple containing arrays of predicted labels and corresponding probabilities.
    """
    probabilities = mdl.predict(x = desc)
    max_prob_idx = np.argmax(probabilities, axis=1)
    probs = np.max(probabilities, axis=1)
    labels = np.array([service_decoder[str(idx)] for idx in max_prob_idx])
    return labels, probs

def predict_one(mdl, desc_str, service_decoder):
    """
    Predicts a label and probability for a single description using a trained model.

    Parameters:
        mdl (object): The trained model used for prediction.
        desc_str (str): The input description to be predicted.
        service_decoder (dictionary): A dictionary of service offerings corresponding to the model's output.

    Returns:
        tuple: A tuple containing the predicted label and the corresponding probability.
    """
    input_desc = [desc_str]
    prob = mdl.predict(x = input_desc)
    idx = np.argmax(prob, axis=1)[0]
    max_prob = np.max(prob, axis=1)[0]
    label = service_decoder[str(idx)]
    return label, max_prob

def load_tf_model(model_path):
    """
    Load a TensorFlow model from the specified path.

    Parameters:
        model_path (str): The path to the saved TensorFlow model.

    Returns:
        tf.keras.Model: The loaded TensorFlow model.

    """
    tf_model = tf.keras.models.load_model(model_path, compile=False)
    return tf_model


def run_process(descriptions, param_dict):
    """
    Run a process to predict labels and probabilities for a list of descriptions using a loaded TensorFlow model.

    Parameters:
        descriptions (list): A list of descriptions to be processed.
        param_dict (dict): A dictionary containing the required parameters for the process.
            - "model_path" (str): The path to the saved TensorFlow model.
            - "service_decoder" (list): A list of labels or categories corresponding to the model's output.

    Returns:
        tuple: A tuple containing the predicted label and the corresponding probability.

    """
    model_path = param_dict["model_path"]
    service_decoder = param_dict["service_decoder"]
    
    transformer_model = load_tf_model(model_path)
    
    predicted_label, probability = predict_many(transformer_model, descriptions, service_decoder)
    return predicted_label, probability
    
    
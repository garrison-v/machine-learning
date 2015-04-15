#!/usr/bin/python

## @model_use.py
#  This file receives data (i.e. settings) required to query from the database,
#      a previously stored SVM model, generated from 'model_generate.py'. The
#      determined SVM Model is then used for analysis based on the input data
#      provided during the current session.
#
#  Note: the term 'dataset' used throughout various comments in this file,
#        synonymously implies the user supplied 'file upload(s)', and XML url
#        references.
import sys
from brain.validator.validate_settings import Validate_Settings

## Class: Model_Use, explicitly inherit 'new-style' class
#
#  Note: this class is invoked within 'load_data.py'
class Model_Use(object):

    ## constructor:
    def __init__(self, svm_data):
        self.svm_data   = svm_data
        self.model_id   = self.svm_data['data']['settings']['svm_model_id']
        self.list_error = []

    ## svm_prediction: using supplied arguments, return an svm prediction from a
    #                  determined model.
    #
    #  @prediction_input, a list of arguments (floats) required to make an SVM
    #      prediction, against the respective svm model.
    def svm_prediction(self, prediction_input):
        # validate input data is json format
        validator = Validate_Settings(sys.svm_data, self.svm_session)

        # get necessary model
        svm_title = Cache_Hset.uncache('svm_title', self.model_id)
        clf = Cache_Model().uncache('svm_model', self.model_id + '_' + svm_title)

        # get encoded labels
        encoded_labels = Cache_Model().uncache('svm_labels', self.model_id)

        # perform prediction, and return the result
        numeric_label = (clf.predict([prediction_input]))
        textual_label = list(encoded_labels.inverse_transform([numeric_label]))
        return textual_label

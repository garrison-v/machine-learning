#!/usr/bin/python

## @config.py
#  This file contains python configuration settings.

## jsonschema_training: contains the jsonschema for the 'training' session.
#                       This validation schema is used in data_validation.py.
def jsonschema_training():
  schema = {
    'type': 'object',
    'properties': {
      'data': {
        'type': 'object',
        'properties': {
          'result': {
            'type': 'object',
            'properties': {
              'svm_session': { 
                'type': 'string',
                'enum': ['training', 'analysis']
              },
              'svm_dataset_type': { 
                'type': 'string',
                'enum': ['upload file', 'xml file']
              },
              'svm_model_type': {
                'type': 'string',
                'enum': ['analysis', 'training']
              },
              'svm_dep_variable': {
                'type': 'array',
                'items': { 'type': 'string' },
                'minItems': 1
              },
              'svm_indep_variable': {
                'type': 'array',
                'items': { 'type': 'string' },
                'minItems': 1
              },
            }
          },
          'json_creator': { 'type': 'string' }
        }
      }
    }
  }
  return schema

## jsonschema_analysis: contains the jsonschema for the 'analysis' session.
#                       This validation schema is used in data_validation.py.
def jsonschema_analysis():
  schema = {
    'type': 'object',
    'properties': {
      'data': {
        'type': 'object',
        'properties': {
          'result': {
            'type': 'object',
            'properties': {
              'svm_session': { 
                'type': 'string',
                'enum': ['training', 'analysis']
              },
              'svm_model_type': {
                'type': 'string',
                'enum': ['classification', 'regression']
              },
              'svm_indep_variable': {
                'type': 'array',
                'items': { 'type': 'string' },
                'minItems': 1
              },
            }
          },
          'json_creator': { 'type': 'string' }
        }
      }
    }    
  }
  return schema

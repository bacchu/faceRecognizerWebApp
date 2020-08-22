import json
from json import JSONEncoder

import numpy

# This is the file where the 128D data is being generated. We created the file below:
import facevector_generator


# This class serializes a NumPy array into a JSON format output
class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


# Create a dictionary object to store the output data
def create_json_response(enc):
    if enc:
        face_data = {
            'faceVector': enc,
            'result': 'Success',
            'message': '',
            'errorCode': 0
        }
    else:
        face_data = {
            'faceVector': 'null',
            'result': 'Failure',
            'message': 'Failed to detect face',
            'errorCode': 1
        }
    return face_data


def get_data(file_name):
    # Replace the string below with the full file path and image in your local directory
    photo_file = file_name

    # Call the function 'generate_vector' that resides in facevector_generator.py
    # Get the 128D encodings back from that function
    encodings_128D = facevector_generator.generate_vector(photo_file)
    face_data_dict = create_json_response(encodings_128D)
    # Create a JSON object with the output data
    json_encodings = json.dumps(face_data_dict, cls=NumpyArrayEncoder, indent=2)
    return json_encodings

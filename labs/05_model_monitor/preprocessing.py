
import json

def preprocess_handler(inference_record):
    input_data = json.loads(inference_record.endpoint_input.data)
    input_data = {f"feature{i}": val for i, val in enumerate(input_data)}
    
    output_data = json.loads(inference_record.endpoint_output.data)["predictions"][0][0]
    output_data = {"prediction0": output_data}
    
    return{**input_data, **output_data}

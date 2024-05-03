import json

path_to_file = r"C:\Users\Artur.Semikov\Downloads\ARMTemplateForFactory.json"
# Load the original ARM template
with open(path_to_file, 'r') as file:
    arm_template = json.load(file)

# Create a dictionary to hold the grouped parameters

default_value = {}
ch_1_internal = {}
ch_1 = {}
ch_1.setdefault("input.txt", ch_1_internal)
ch_1_internal.setdefault("type","object")
ch_1_internal.setdefault("default_value",default_value)

# Loop through the original parameters and group them
for param_name, param_details in arm_template['parameters'].items():
    # For simplicity, let's assume all parameters are of type 'string'
    # You may need to adjust this based on your actual template
    (default_value.update({param_name: param_details["defaultValue"]}))

# Replace the original parameters with the grouped parameters
arm_template['parameters'] = ch_1

# Write the updated ARM template back to a file
with open('updated_template.json', 'w') as file:
    json.dump(arm_template, file, indent=2)



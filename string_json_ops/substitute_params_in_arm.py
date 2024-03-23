import json

arm_template: json

pathToFile = r"C:\Users\Artur.Semikov\Documents\adf_dev\ARMTemplateForFactory.json"
env  = "DEV"
#env  = "QA"

with open(pathToFile, 'r') as file:
    arm_template = json.load(file)

arm_template_text = json.dumps(arm_template,indent=4)

for param_name, param_info in arm_template.get('parameters', {}).items():
    look_up_str = f"[parameters('{param_name}')]"
    string_for_substitute = param_info.get('defaultValue', None)
    arm_template_text=arm_template_text.replace(str(look_up_str),str(string_for_substitute))

if env == "DEV":
    # harmony-datafactory-qa-01-kcts or harmony-datafactory-dev-01-kcts
    arm_template_text=arm_template_text.replace(f"parameters('factoryName')","'harmony-datafactory-dev-01-kcts'")
else:
    arm_template_text = arm_template_text.replace(f"parameters('factoryName')", "'harmony-datafactory-qa-01-kcts'")

with open('updated_template.json', 'w') as file:
    file.write(arm_template_text)



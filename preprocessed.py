import subprocess

dataset = "electone" #@param {type:"string"}
channels = 2 #@param {type:"integer"}
preprocessed_dataset = "electone/preprocessed" #@param {type:"string"}

command = [
    "rave", "preprocess",
    "--input_path", dataset,
    "--output_path", preprocessed_dataset,
    "--channels", str(channels)
]

subprocess.run(command, check=True)


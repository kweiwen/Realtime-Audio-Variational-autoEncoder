import subprocess

dataset = "electone/preprocessed"   # dataset directorty
name = "name_of_run"
save_dir = "run"                    # checpoint directorty
architecture = "v1"                 # available: "v3", "v2", "v1", "discrete", "onnx", "raspberry"
regularization = "default"      # available: "default", "wasserstein", "spherical"
channels = 2
batch_size = 4
val_every = 1000
save_every = 100
gpu = -1

command = [
    "rave", "train",
    "--config", architecture,
    "--db_path", dataset,
    "--name", name,
    "--val_every", str(val_every),
    "--channels", str(channels),
    "--save_every", str(save_every),
    "--batch", str(batch_size),
    "--gpu", str(gpu)
]

# execute command line
subprocess.run(command, check=True)

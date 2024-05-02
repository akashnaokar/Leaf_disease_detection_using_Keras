from src.utils import unzip_data, get_gpu_info
from src.data import datamodule
import matplotlib.pyplot as plt


get_gpu_info.torch_info()
get_gpu_info.gpu_info()

unzip_data.extract_files()

train_dataset , val_dataset = datamodule.create_dataset()
print('Train Ds: ', train_dataset)
print('val Ds : ', val_dataset)
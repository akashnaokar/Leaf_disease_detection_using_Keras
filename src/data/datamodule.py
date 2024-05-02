from typing import Any, Dict, Optional, Tuple
import hydra
import torch
from torchvision.transforms import v2
from torchvision.datasets import ImageFolder



@hydra.main(config_path='../../configs/', config_name='config', version_base=None)
def create_dataset(cfg):

    height = cfg.hyperparams.height
    width = cfg.hyperparams.width

    transforms  = v2.Compose([
        v2.Resize(size=(height, width)),
        v2.ToDtype(torch.float32, scale=True),
    ])

    train_dataset = ImageFolder(root=cfg.paths.train_data_dir, transform=transforms)
    print(train_dataset)
    valid_dataset = ImageFolder(root=cfg.paths.val_data_dir, transform=transforms)

    return train_dataset, valid_dataset

if __name__ == "__main__":
    train_dataset, valid_dataset = create_dataset()
    print('Train_ds', train_dataset)
from zipfile import ZipFile
from tqdm import tqdm
import os
import hydra

@hydra.main(config_path='../../configs/', config_name='config', version_base=None)
def extract_files(cfg):
    data_dir = cfg.paths.data_dir
    raw_data_dir = cfg.paths.raw_data_dir
    train_data_dir = cfg.paths.train_data_dir
    val_data_dir = cfg.paths.val_data_dir
    test_data_dir =cfg.paths.test_data_dir
    dataset_name = cfg.files.dataset_name

    if not (os.path.exists(train_data_dir) and os.path.exists(val_data_dir) and os.path.exists(test_data_dir)):

        with ZipFile(os.path.join(raw_data_dir ,dataset_name), 'r') as archive:
            for file in tqdm(iterable=archive.namelist(), total=len(archive.namelist())):
                archive.extract(path = data_dir, member = file)

    else:
        print('Data already extracted. Skipping extraction process.')

if __name__ == "__main__":
    extract_files()


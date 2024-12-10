import pandas as pd
import os
from utils import convert
import logging

dataset_path = "data/dataset"
words_path = "data/sources/words"
dataset = "data/dataset/words.csv"
logs_path = "logs/"

logger = logging.getLogger(__name__)


def check():
    logger.info('Checking if the dataset is exist...')
    if not os.path.exists(dataset_path):
        logger.warning('Dataset does not exist!')
        logger.info('Creating dataset directory...')
        os.makedirs(dataset_path)
        for file_name in os.listdir(words_path):
            file_path = os.path.join(words_path, file_name)
            if os.path.isfile(file_path):
                convert.from_source_to_csv(file_path, os.path.join(dataset_path, 'words.csv'))
    else:
        logger.info('Dataset exist')


def load_dataset(path: str):
    logger.info(f'Loading dataset from: {path}')
    data = pd.read_csv(path)
    print(data)
    logger.debug(data)


if __name__ == '__main__':
    if not os.path.exists(logs_path):
        os.makedirs(logs_path)
        
    logging.basicConfig(filename=f'{logs_path}/log.log', level=logging.DEBUG)
    logger.info('Started')

    check()
    load_dataset(dataset)

    logger.info('Finished')

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = 'results'
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
FILE_NAME = 'status_summary_{file_time}.csv'
HEAD_TABLE = ('Статус', 'Количество')
TOTAL_COUNT = 'Total'

PIPELINE_PRIORITY = 300

import csv
import datetime as dt
from collections import defaultdict

from pep_parse.constants import (
    BASE_DIR, RESULTS_DIR, DATETIME_FORMAT, FILE_NAME, HEAD_TABLE, TOTAL_COUNT)


class PepParsePipeline:
    status_count = defaultdict(int)

    def open_spider(self, spider):
        results_dir = BASE_DIR / RESULTS_DIR
        results_dir.mkdir(exist_ok=True)

    def process_item(self, item, spider):
        self.status_count[item['status']] += 1
        return item

    def close_spider(self, spider):
        file_time = dt.datetime.now().strftime(DATETIME_FORMAT)
        file_path = BASE_DIR / RESULTS_DIR / FILE_NAME.format(
            file_time=file_time)
        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(HEAD_TABLE)
            writer.writerows(self.status_count.items())
            writer.writerow([TOTAL_COUNT, sum(self.status_count.values())])

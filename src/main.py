from utils import get_all_election_data, get_all_data_file_names, get_generated_date, load_json_data
from db_utils import save_to_db
from datetime import datetime
import sys

print("The election is over! No data left to scrape...")

sys.exit(1)

get_all_election_data()

files: list[str] = get_all_data_file_names('../data/json/raw/')

# files names are in the format: YYYY-MM-DDTHH-MM-SS.json
# we want to sort by date, so we need to extract the date from the file name
# and then sort by that
files.sort(key=lambda x: datetime.strptime(x.split('.')[0], '%Y-%m-%dT%H%M%S'))

# we want to load the most recent data
data = load_json_data('../data/json/raw/' + files[-1])

save_to_db(data, get_generated_date(data))
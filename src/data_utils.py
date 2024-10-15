import sqlite3
import sys
import traceback
import csv

# pull the data from the db and do some stuff innit 

def get_db_data(table_name):
    db_file_path = "../data/db/all_data.db"
    conn: sqlite3.Connection = sqlite3.connect(db_file_path)
    cur: sqlite3.Cursor = conn.cursor()

    command = "SELECT * FROM " + table_name

    try:
        cur.execute(command)
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))

    if cur.fetchone() is None:
        print("[ERROR] that didn't seem to return any data... strange. fuck you i guess")
        exit()
    
    data = cur.fetchall()

    return data


def save_final_count_as_csv(data, filename) -> None:
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Eligible', 'Voters'])
        for item in data:
            writer.writerow([item[1], item[2], item[-1]])


def save_all_data_as_csv(data, filename):
    with open(filename, 'w', newline = '') as csvfile:
        writer = csv.writer(csvfile)
        for item in data:
            writer.writerow(item)


if __name__ == '__main__':
    dep_data = get_db_data('department_data')
    sex_data = get_db_data('sex_data')
    year_data = get_db_data('year_data')
    type_data = get_db_data('type_data')

    save_all_data_as_csv(dep_data, '../data/csv/full/department_final_votes.csv')
    save_all_data_as_csv(sex_data, '../data/csv/full/sex_final_votes.csv')
    save_all_data_as_csv(year_data, '../data/csv/full/year_final_votes.csv')
    save_all_data_as_csv(type_data, '../data/csv/full/type_final_votes.csv')


    societies_data = get_db_data('societies_data')
    small_groups = get_db_data('small_groups_data')
    medium_groups = get_db_data('medium_groups_data')
    large_groups = get_db_data('large_groups_data')
    associations = get_db_data('associations_data')

    combined_society_data = societies_data + small_groups + medium_groups + large_groups + associations

    save_all_data_as_csv(combined_society_data, '../data/csv/full/combined_society_data.csv')

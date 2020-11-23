import os
import csv

import supervisely_lib as sly

my_app = sly.AppService()

INPUT_FILE = os.environ['INPUT_FILE']

SERVER_ADDRESS = os.environ['SERVER_ADDRESS']
API_TOKEN = os.environ['API_TOKEN']
api = sly.Api(SERVER_ADDRESS, API_TOKEN)

LOGIN_COL_NAME = 'user'
PASSWORD_COL_NAME = 'password'

DEFAULT_DELIMITER = ','

@my_app.callback("create_user_from_csv")
@sly.timeit
def create_user_from_csv(api: sly.Api, task_id, context, state, app_logger):
    with open(INPUT_FILE, "r") as f_obj:
        new_users = {}
        reader = csv.DictReader(f_obj, delimiter=DEFAULT_DELIMITER)

        for row in reader:
            row[LOGIN_COL_NAME] = row[LOGIN_COL_NAME].strip()
            row[PASSWORD_COL_NAME] = row[PASSWORD_COL_NAME].strip()

            if row[LOGIN_COL_NAME] in new_users:
                sly.logger.warn(f'Duplicate login found in csv file: {row[LOGIN_COL_NAME]}')

            new_users[row[LOGIN_COL_NAME]] = row

    existing_users = api.user.get_list([{'field': 'login', 'operator': 'in', 'value': list(new_users.keys())}])

    for existing_user in existing_users:
        if existing_user.login in new_users:
            sly.logger.warn(f"Username \"{existing_user.login}\" already exists")
            del new_users[existing_user.login]

    progress = sly.Progress('Creating users...', len(new_users), sly.logger)

    for user, user_data in new_users.items():
        api.user.create(login=user_data[LOGIN_COL_NAME], password=user_data[PASSWORD_COL_NAME], is_restricted=False)
        progress.iter_done_report()

    my_app.stop()


def main():
    sly.logger.info("Script arguments", extra={
        "CONFIG_DIR": os.environ.get("CONFIG_DIR", "ENV not found")
    })

    # Run application service
    my_app.run(initial_events=[{"command": "create_user_from_csv"}])


if __name__ == "__main__":
    sly.main_wrapper("main", main)
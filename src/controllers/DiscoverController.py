import os
import json

from src.config.logger import Logger

logger = Logger()


class DiscoverController:

    def __init__(self):
        self.test = "test data"

    @classmethod
    def documentation(self):
        doc = {}
        current_directory = os.path.dirname(__file__)
        file_path = os.path.normpath(
            os.path.join(current_directory, '../config/agent.json'))

        with open(file_path, "r") as json_file:
            doc = json.load(json_file)

        return doc

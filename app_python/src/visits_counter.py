import os


class VisitsCounter:
    """

    Timer is a class that provides simple interface to work with time

    """

    def __init__(self, filePath: str):
        self.path = filePath
        self.__create_visits_file_if_not_exists__()

    def update(self):
        self.__update_visits__()

    def get(self):
        with open(self.path, "r") as visits_file:
            return int(visits_file.readline())

    def __update_visits__(self, ):
        with open(self.path, "r") as visits_file:
            counter = int(visits_file.readline())
        with open(self.path, "w") as visits_file:
            visits_file.write(str(counter + 1))

    def __create_visits_file_if_not_exists__(self):
        if not os.path.exists(self.path):
            with open(self.path, "w+") as file:
                file.write("0")

import os
from collections import defaultdict

from src.draw.common import constants


class Configuration:
    config_map = defaultdict(lambda: None)

    def __init__(self) -> None:
        self.__get_config_from_defaults()
        self.__get_config_from_file()
        self.__get_config_from_env()
        return

    def __get_config_from_defaults(self) -> None:
        self.config_map["message_broker_host"] = constants.DEFAULT_MESSAGE_BROKER_HOST
        self.config_map["message_broker_port"] = constants.DEFAULT_MESSAGE_BROKER_PORT

        return

    def __get_config_from_file(self) -> None:
        # read in config file and insert appropriate values into config map
        pass

    def __get_config_from_env(self) -> None:
        for possible_env_variable in constants.CONFIGURATION_AVAILABLE_OPTIONS:
            if env_value := os.environ.get(
                f"{constants.SERVICE_NAME}_{possible_env_variable.upper()}", None
            ):
                self.config_map[possible_env_variable] = env_value
        return


config = Configuration()

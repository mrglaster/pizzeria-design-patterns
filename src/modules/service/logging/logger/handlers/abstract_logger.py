import os
from datetime import datetime
from src.modules.service.managers.settings_manager import SettingsManager


class AbstractLogger:

    logs_path = ""

    def log(self, *args) -> bool:
        pass

    def write_log(self, message):
        if SettingsManager().settings.log_writing_mode != "console":
            if not self.logs_path:
                today_date = datetime.now().strftime("%Y-%m-%d")
                log_filename = os.path.join(SettingsManager().settings.logs_path, f"{today_date}.log")
                self.logs_path = log_filename

            if not os.path.exists(self.logs_path):
                with open(self.logs_path, "w") as log_file:
                    log_file.write("")
            with open(self.logs_path, "a") as log_file:
                log_file.write(message + "\n")
        print(message)


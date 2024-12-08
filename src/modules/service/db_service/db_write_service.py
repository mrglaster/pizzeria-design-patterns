import psycopg2
from psycopg2.extras import Json

from src.modules.domain.enum.log_enums import LogLevel
from src.modules.service.logging.logger.service.logger_service import LoggerService
from src.modules.service.managers.settings_manager import SettingsManager


class DatabaseWriteService:

    @staticmethod
    def write_data(table_name, uid, data):
        query = f"""
               INSERT INTO {table_name} (uid, data)
               VALUES (%s, %s)
               ON CONFLICT (uid)
               DO UPDATE SET data = EXCLUDED.data;
            """
        connection = psycopg2.connect(SettingsManager().settings.db_url)
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, (uid, Json(data)))
                connection.commit()
        except Exception as e:
            connection.rollback()
            print(f"ERROR HAPPENED: {e}")
            LoggerService.send_log(log_level=LogLevel.ERROR, message=f"Error while inserting or updating data: {e}")

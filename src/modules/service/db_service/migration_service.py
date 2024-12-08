import os.path
import psycopg2
from src.modules.domain.enum.log_enums import LogLevel
from src.modules.service.logging.logger.service.logger_service import LoggerService
from src.modules.service.managers.settings_manager import SettingsManager


class MigrationService:
    @staticmethod
    def do_migration():
        create_tables_file = 'v1_create_tables.sql'
        try:
            settings = SettingsManager().settings

            if not SettingsManager().read_settings():
                raise RuntimeError("Failed to load settings.")

            migrations_path = settings.migrations_path
            if not os.path.exists(migrations_path):
                raise FileNotFoundError(f"Migrations path not found: {migrations_path}")

            create_tables_file_path = os.path.join(migrations_path, create_tables_file)
            connection = psycopg2.connect(os.environ.get('DATABASE_URL'))
            cursor = connection.cursor()

            with open(create_tables_file_path, 'r') as file:
                sql_script = file.read()

            cursor.execute(sql_script)
            connection.commit()
            LoggerService.send_log(LogLevel.INFO, "Migration processed successfully")
        except Exception as e:
            LoggerService.send_log(LogLevel.ERROR, f"Database db_service error: {e}")
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'connection' in locals():
                connection.close()

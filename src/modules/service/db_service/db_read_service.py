import json
import psycopg2
from src.modules.service.managers.settings_manager import SettingsManager


class DatabaseReadService:

    @staticmethod
    def read_all(table_name):
        conn = psycopg2.connect(SettingsManager().settings.db_url)
        cur = conn.cursor()
        cur.execute(f"SELECT data FROM {table_name};")
        rows = cur.fetchall()
        return [json.dumps(row[0]) for row in rows]
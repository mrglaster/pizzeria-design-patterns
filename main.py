from modules.domain.settings import SettingsManager

sm = SettingsManager()
sm.read_settings("settings.json")
print(sm.settings)

sm2 = SettingsManager()
print(sm.settings)
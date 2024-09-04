from modules.settings.settings_manager import SettingsManager

sm = SettingsManager()
if sm.read_settings():
    print(sm.settings)
else:
    print("OOPS")
import json
import os

FIT_FILES_DIRECTORY = "./data/activities/fit/"
CSV_FILES_DIRECTORY = "./data/activities/csv/"

os.makedirs(FIT_FILES_DIRECTORY, exist_ok=True)
os.makedirs(CSV_FILES_DIRECTORY, exist_ok=True)

SETTINGS_FILE_NAME = "Settings.json"
SETTINGS_FILE_PATH = os.path.join(os.path.dirname(__file__), SETTINGS_FILE_NAME)

LATITUDE, LONGITUDE = "position_lat", "position_long"
TIMESTAMP = "timestamp"
ACCUMULATED_POWER = "accumulated_power"
ACTIVITY_TYPE = "activity_type"
CADENCE = "cadence"
DISTANCE = "distance"
ALTITUDE = "enhanced_altitude"
SPEED = "enhanced_speed"
FRACTIONAL_CADENCE = "fractional_cadence"
HEART_RATE = "heart_rate"
POWER = "power"
STANCE_TIME = "stance_time"
STANCE_TIME_BALANCE = "stance_time_balance"
STANCE_TIME_PERCENTAGE = "stance_time_percent"
STEP_LENGTH = "step_length"
TEMPERATURE = "temperature"
VERTICAL_OSCILLATION = "vertical_oscillation"
VERTICAL_RATIO = "vertical_ratio"
UNKNOWN_COLUMN_REGEX = r"unknown_\d+"

with open(SETTINGS_FILE_PATH, "r") as file:
    settings = json.load(file)
    USERNAME = settings["GarminConnectCredentials"]["Username"]
    PASSWORD = settings["GarminConnectCredentials"]["Password"]

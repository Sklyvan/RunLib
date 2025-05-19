from .configuration import USERNAME, PASSWORD
from garminconnect import Garmin
from exceptions import *
import zipfile
import io


CLIENT = Garmin(USERNAME, PASSWORD)
CLIENT.login()


def obtainLatestActivityByType(activityType: str) -> dict:
    """
    Obtain the latest activity of a specific type from Garmin Connect and return the activity summary.
    :param activityType: The type of activity to obtain (e.g., "running", "cycling").
    :return: The activity summary of the latest activity of the specified type.
    """
    foundLatestActivity, i = False, 0
    latestActivity = {}
    while not foundLatestActivity:
        try:
            latestActivity = CLIENT.get_activities(i, 1)[0]
        except IndexError:
            raise NoActivityFound(f"No activity found for type {activityType}.")
        else:
            if latestActivity["activityType"]["typeKey"] == activityType:
                foundLatestActivity = True
            else:
                i += 1

    return latestActivity


def obtainLatestRunningActivity() -> dict:
    """
    Obtain the latest running activity from Garmin Connect and return the activity summary.
    :return: The activity summary of the latest running activity.
    """
    return obtainLatestActivityByType("running")


def downloadActivityAsFIT(activityID: str) -> bytes:
    """
    Download the activity as a FIT file from Garmin Connect.
    :param activityID: The ID of the activity to obtain.
    :return: The activity as a FIT file.
    """
    activityZipFile =  CLIENT.download_activity(activityID, dl_fmt=Garmin.ActivityDownloadFormat.ORIGINAL)
    zipBytes = io.BytesIO(activityZipFile) # The API returns the FIT files as ZIP files

    with zipfile.ZipFile(zipBytes, 'r') as zipRef:
        for name in zipRef.namelist():
            if name.endswith(".fit"):
                return zipRef.read(name)  # This is the FIT file content as bytes

    raise NoFitFileInZip(f"No FIT file found in the ZIP file for {activityID}.")


def downloadLatestRunningActivityAsFIT() -> bytes:
    """
    Obtain the latest running activity from Garmin Connect and download it as a FIT file.
    :return: The latest running activity as a FIT file.
    """
    latestRunningActivity = obtainLatestRunningActivity()
    return downloadActivityAsFIT(latestRunningActivity["activityId"])

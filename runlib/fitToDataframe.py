from .utils import semicirclesToDegrees
from fitparse import FitFile
from .configuration import *
import pandas as pd
import re
import io


def convertFitToDataframe(fileContent: bytes, removeUnknown: bool = True) -> pd.DataFrame:
    """
    Convert a FIT file to a pandas DataFrame. The FIT file is a binary file format used for storing fitness data.
    The FIT file format is used by many fitness devices, such as GPS watches and heart rate monitors.
    :param fileContent: The FIT file to convert, this is the content of the file as bytes.
    :param removeUnknown: If True, remove unknown fields from the DataFrame.
    :return: A pandas DataFrame containing the data from the FIT file.
    """
    # Read the FIT file with the library
    fitFile = FitFile(io.BytesIO(fileContent))
    fitFileData = []
    
    # Extract data from the FIT file
    for m in fitFile.get_messages("record"):
        data = {field.name: field.value for field in m}
        fitFileData.append(data)
    df = pd.DataFrame(fitFileData)

    # Convert semicircles to degrees for position_lat and position_long
    if LATITUDE in df.columns:
        df[LATITUDE] = df[LATITUDE].apply(
            lambda x: semicirclesToDegrees(x) if pd.notnull(x) else None
        )
    if LONGITUDE in df.columns:
        df[LONGITUDE] = df[LONGITUDE].apply(
            lambda x: semicirclesToDegrees(x) if pd.notnull(x) else None
        )

    # Convert timestamp to datetime
    if TIMESTAMP in df.columns:
        df[TIMESTAMP] = pd.to_datetime(df[TIMESTAMP], unit="s", utc=True)
        df = df.sort_values(TIMESTAMP).reset_index(drop=True)

    # Remove all the columns matching the regular expression unknown_*
    columnsToRemove = [x for x in df.columns if re.match(UNKNOWN_COLUMN_REGEX, x)] if removeUnknown else []
    df.drop(columns=columnsToRemove, inplace=True)

    return df


def convertFitToDataframeFromFile(filePath: str, removeUnknown: bool = True) -> pd.DataFrame:
    """
    Convert a FIT file to a pandas DataFrame. The FIT file is a binary file format used for storing fitness data.
    The FIT file format is used by many fitness devices, such as GPS watches and heart rate monitors.
    :param filePath: The path to the FIT file to convert.
    :param removeUnknown: If True, remove unknown fields from the DataFrame.
    :return: A pandas DataFrame containing the data from the FIT file.
    """
    with open(filePath, "rb") as fitFile:
        return convertFitToDataframe(fitFile.read(), removeUnknown)

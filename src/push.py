import os
import zipfile
from pathlib import Path
from zipfile import ZipFile

from pandas import DataFrame


def push_data_frame_to_csv_zip(
    df: DataFrame,
    file_name: str,
    path_export: str = '../data'
) -> None:
    kwargs = {
        'path_or_buf': Path(path_export).joinpath(file_name),
        'index': True,
        'encoding': 'utf-8-sig'
    }
    df.to_csv(**kwargs)
    os.chdir(path_export)
    with ZipFile(f'{os.path.splitext(file_name)[0]}.zip', 'w') as archive:
        archive.write(file_name, compress_type=zipfile.ZIP_DEFLATED)
        os.unlink(Path(path_export).joinpath(file_name))

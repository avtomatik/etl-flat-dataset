#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 23:51:24 2022

@author: Alexander Mikhailov
"""


from pathlib import Path

import pandas as pd
from push import push_data_frame_to_csv_zip
from transform import preprocess


def main(
    file_names: tuple[str] = (
        'dataset_usa_0000_public_debt.txt',
        'dataset_usa_0022_m1.txt',
        'dataset_usa_0025_p_r.txt',
    ),
    path_src: str = '../data',
    path_export: str = '../data',
    archive_name: str = 'dataset_usa_misc.csv'
) -> None:
    pd.concat(
        map(
            lambda _: pd.read_csv(Path(path_src).joinpath(_)).pipe(preprocess),
            file_names
        )
    ).pipe(push_data_frame_to_csv_zip, archive_name, path_export)


if __name__ == '__main__':
    main()


from .config import DATA_DIR, FILE_NAME
from .pipeline import (CsvLoader, DataPipeline, InMemoryZipSaver,
                       InsertIndicatorAndSwapCols)


def main() -> None:
    pipeline = DataPipeline(
        loaders=[CsvLoader()],
        transformers=[InsertIndicatorAndSwapCols()],
        saver=InMemoryZipSaver(),
    )

    input_paths = [p for p in DATA_DIR.iterdir() if not p.name.startswith('.')]
    output_path = DATA_DIR / FILE_NAME

    pipeline.run(input_paths, output_path)

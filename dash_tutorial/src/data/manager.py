from dataclasses import dataclass
from typing import Optional

import pandas as pd

from .loader import DataSchema


def get_uniques(data: pd.DataFrame, col: str) -> list[str]:
    values: "pd.Series[str]" = data[col]
    return list(set(values))


@dataclass
class DataManager:
    _data: pd.DataFrame

    @property
    def year_options(self) -> list[dict[str, str]]:
        available_years: set[str] = set(self._data.loc[:, DataSchema.YEAR.value])
        return [{"label": i, "value": i} for i in available_years]

    @property
    def month_options(self) -> list[dict[str, str]]:
        available_months: set[str] = set(self._data.loc[:, DataSchema.MONTH.value])
        return [{"label": i, "value": i} for i in available_months]

    @property
    def category_options(self) -> list[dict[str, str]]:
        categories = get_uniques(self._data, DataSchema.CATEGORY.value)
        base_options = [{"label": i, "value": i} for i in categories]
        filtered_options = filter(
            lambda option: not pd.isna(option["label"]), base_options
        )
        final_options = sorted(filtered_options, key=lambda x: x["label"])
        return final_options

    @property
    def year_values(self) -> list[str]:
        return sorted(get_uniques(self._data, DataSchema.YEAR.value))

    @property
    def category_values(self) -> list[str]:
        return sorted(get_uniques(self._data, DataSchema.CATEGORY.value))

    def month_values(self, years: Optional[list[int]] = None) -> list[str]:
        if years is None:
            years = get_uniques(self._data, DataSchema.MONTH.value)
        filtered_data = self._data.query(f"{DataSchema.YEAR.value} == {years}")
        return get_uniques(filtered_data, DataSchema.MONTH.value)
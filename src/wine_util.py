import pandas as pd 
import numpy as np

def filter_iqr(df, col, qlow=0.25, qhigh=0.75, whisker_width=1.5):
        """
        Filter data with quantile range.

        Parameters
        ---------
        df: pd.DataFrame
            data
        col: string
            name of the column to calculate the quantile range
        qlow: float
            low quantile threshold (default 25%)
        qhigh: float
            high quantile threshold (default 75%)
        whisker_width: float
            filtering factor (default 1.5)

        Returns
        -------
        pd.DataFrame
            filtered dataframe
        """
        qlow_threshold = df[col].quantile(qlow)
        qhigh_threshold = df[col].quantile(qhigh)
        iqr = qhigh_threshold - qlow_threshold
        cond = (df[col] >= qlow_threshold-whisker_width*iqr) & (df[col] <= qhigh_threshold+whisker_width*iqr)
        df_reduced = df[cond]
        return df_reduced
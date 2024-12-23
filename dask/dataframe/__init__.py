from __future__ import annotations

import importlib


def _dask_expr_enabled() -> bool:
    import dask

    use_dask_expr = dask.config.get("dataframe.query-planning")
    if use_dask_expr is False:
        raise NotImplementedError("The legacy implementation is no longer supported")

    return True


_dask_expr_enabled()


try:

    # Ensure that dtypes are registered
    import dask.dataframe._dtypes
    import dask.dataframe._pyarrow_compat
    from dask.base import compute
    from dask.dataframe import backends, dispatch
    from dask.dataframe.dask_expr import (  # type: ignore
        DataFrame,
        Index,
        Scalar,
        Series,
        concat,
        from_array,
        from_dask_array,
        from_delayed,
        from_dict,
        from_graph,
        from_map,
        from_pandas,
        get_collection_type,
        get_dummies,
        isna,
        map_overlap,
        map_partitions,
        melt,
        merge,
        merge_asof,
        pivot_table,
        read_csv,
        read_fwf,
        read_hdf,
        read_json,
        read_orc,
        read_parquet,
        read_sql,
        read_sql_query,
        read_sql_table,
        read_table,
        repartition,
        to_bag,
        to_csv,
        to_datetime,
        to_hdf,
        to_json,
        to_numeric,
        to_orc,
        to_parquet,
        to_records,
        to_sql,
        to_timedelta,
    )
    from dask.dataframe.groupby import Aggregation
    from dask.dataframe.io import demo
    from dask.dataframe.utils import assert_eq
except ImportError:
    import dask.dataframe as dd

    dd = importlib.reload(dd)

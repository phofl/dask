from __future__ import annotations

import importlib
import pickle

import pytest

from dask import config
from dask.dataframe.utils import assert_eq as dd_assert_eq


def _backend_name() -> str:
    return config.get("dataframe.backend", "pandas")


def _backend_library():
    return importlib.import_module(_backend_name())


def xfail_gpu(reason=None):
    condition = _backend_name() == "cudf"
    reason = reason or "Failure expected for cudf backend."
    return pytest.mark.xfail(condition, reason=reason)


def assert_eq(a, b, *args, serialize_graph=True, **kwargs):
    if serialize_graph:
        # Check that no `Expr` instances are found in
        # the graph generated by `Expr.dask`
        with config.set({"dask-expr-no-serialize": True}):
            for obj in [a, b]:
                if hasattr(obj, "dask"):
                    try:
                        pickle.dumps(obj.dask)
                    except AttributeError:
                        try:
                            import cloudpickle as cp

                            cp.dumps(obj.dask)
                        except ImportError:
                            pass

    # Use `dask.dataframe.assert_eq`
    return dd_assert_eq(a, b, *args, **kwargs)
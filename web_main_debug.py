"""Compatibility debug launcher for the desktop UI."""

import warnings

from ok import OK
from src.config import config


if __name__ == "__main__":
    warnings.warn(
        'ok-script 3 removed the web frontend; launching the desktop UI. Use main_debug.py instead.',
        FutureWarning,
    )
    config['debug'] = True
    OK(config).start()

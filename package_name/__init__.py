import warnings
from astropy.wcs import FITSFixedWarning
from . import config

CONFIG = config.ConfigManager()

from pkg_resources import get_distribution

__version__ = get_distribution("python_package").version

# TODO: update Telescope "names" fields
# TODO: document custom Image using _get_data_header

"""rio-tiler.cmap: colormap files.

# Most cmap are pure copy from matplotlib.cm
# Using this script:
import numpy as np
import matplotlib.cm as cm

def generate_maps() -> None:
    x = np.linspace(0, 1, 256)
    for name, colormap in cm.cmap_d.items():
        cmap_vals = colormap(x)[:, :]
        cmap_uint8 = (cmap_vals * 255).astype('uint8')
        np.save(f'{name.lower()}.npy', cmap_uint8)

Additional colormaps:
- cfastie: http://publiclab.org/notes/cfastie/08-26-2014/new-ndvi-colormap
- rplumbo: https://github.com/cogeotiff/rio-tiler/pull/90
- schwarzwald: http://soliton.vm.bytemark.co.uk/pub/cpt-city/wkp/schwarzwald/tn/wiki-schwarzwald-cont.png.index.html

Code inspired from our friends https://github.com/DHI-GRAS/terracotta/blob/master/terracotta/cmaps/__init__.py
"""

import os

from pkg_resources import (
    DistributionNotFound,
    Requirement,
    resource_filename,
    resource_listdir,
)

SUFFIX = ".npy"


try:
    PACKAGE = Requirement.parse("rio_tiler")
    _colormap_dir = resource_filename("rio_tiler", "cmap_data")
    _file_list = [
        os.path.join(_colormap_dir, f)
        for f in resource_listdir(PACKAGE, "rio_tiler/cmap_data")
    ]
except DistributionNotFound:  # rio_tiler was not installed, fall back to file system
    _colormap_dir = os.path.dirname(__file__)
    _file_list = os.listdir(_colormap_dir)


_default_cmaps = [f for f in _file_list if f.endswith(SUFFIX)]

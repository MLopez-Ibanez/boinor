#!/usr/bin/env python3
#
# boinor documentation build configuration file.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.

from importlib.metadata import version
import os

import sphinx_rtd_theme

extensions = [
    "autoapi.extension",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.intersphinx",
    "nbsphinx",
    "sphinx_gallery.load_style",
    "IPython.sphinxext.ipython_console_highlighting",
    "sphinx.ext.mathjax",  # Maths visualization
    "sphinx.ext.graphviz",  # Dependency diagrams
    "sphinx_copybutton",
    "notfound.extension",
    "hoverxref.extension",
    "myst_parser",
    "sphinx_github_role",
    "sphinxcontrib.bibtex",
]

# GitHub role config
github_default_org_project = ("boinor", "boinor")

# MathJax config
# See https://github.com/spatialaudio/nbsphinx/issues/572#issuecomment-853389268
mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@2/MathJax.js?config=TeX-AMS-MML_HTMLorMML"
mathjax2_config = {
    "tex2jax": {
        "inlineMath": [["$", "$"], ["\\(", "\\)"]],
        "processEscapes": True,
        "ignoreClass": "document",
        "processClass": "math|output_area",
    }
}
myst_update_mathjax = False

myst_enable_extensions = [
    "substitution",
]
myst_substitutions = {
    "Ephem": "{py:class}`~boinor.ephem.Ephem`",
    "Orbit": "{py:class}`~boinor.twobody.orbit.scalar.Orbit`",
}

# Hoverxref Extension
hoverxref_auto_ref = True
hoverxref_mathjax = True
hoverxref_intersphinx = [
    "astropy",
    "numpy",
    "scipy",
    "matplotlib",
]
hoverxref_domains = ["py"]
hoverxref_role_types = {
    "hoverxref": "modal",
    "ref": "modal",  # for hoverxref_auto_ref config
    "confval": "tooltip",  # for custom object
    "mod": "tooltip",  # for Python Sphinx Domain
    "class": "tooltip",  # for Python Sphinx Domain
    "meth": "tooltip",
    "obj": "tooltip",
}

# Other
autodoc_member_order = "bysource"
templates_path = ["_templates"]
source_suffix = {
    ".rst": "restructuredtext",
    ".myst.md": "jupyter_notebook",
    ".md": "markdown",
}

project = "boinor"
copyright = "2024, Thorsten Alteholz and the boinor development team (forked from poliastro)"

project_ver = version(project)
version = ".".join(project_ver.split(".")[:2])
release = project_ver

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build", "**.ipynb_checkpoints"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# Intersphinx configuration
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "astropy": ("https://docs.astropy.org/en/stable/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy-1.8.0/", None),
    "matplotlib": ("https://matplotlib.org/stable/", None),
}

# Warning suppresses
suppress_warnings = ["image.nonlocal_uri"]

if os.environ.get("BOINOR_SKIP_NOTEBOOKS") == "True":
    nbsphinx_execute = "never"
    suppress_warnings.append("nbsphinx.thumbnail")
else:
    nbsphinx_execute = "always"

# -- Options for HTML output

html_theme = "sphinx_rtd_theme"
html_context = {
    "sidebar_external_links_caption": "Links",
    "sidebar_external_links": [
        (
            '<i class="fa fa-rss fa-fw"></i> Blog',
            "https://www.boinor.space",
        ),
        (
            '<i class="fa fa-github fa-fw"></i> Source code',
            "https://github.com/boinor/boinor",
        ),
        (
            '<i class="fa fa-bug fa-fw"></i> Issue tracker',
            "https://github.com/boinor/boinor/issues",
        ),
        (
            '<i class="fa fa-envelope fa-fw"></i> Mailing list',
            "https://groups.io/g/boinor-dev",
        ),
        (
            '<i class="fa fa-comments fa-fw"></i> Chat',
            "http://chat.boinor.space",
        ),
        (
            '<i class="fa fa-file-text fa-fw"></i> Citation',
            "https://doi.org/10.5281/zenodo.593610",
        ),
    ],
}
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_style = os.path.join("css", "custom.css")
html_favicon = os.path.join("_static", "favicon.ico")
html_static_path = ["_static"]
html_js_files = ["language_data.js"]

# Thumbnail selection for nbsphinx gallery
nbsphinx_thumbnails = {
    "examples/going-to-mars-with-python-using-boinor": "_static/thumbnails/going_to_mars_thumbnail.png",
    "examples/plotting-in-3D": "_static/thumbnails/3d_plotting_thumbnail.png",
    "examples/propagation-using-cowells-formulation": "_static/thumbnails/cowell_thumbnail.png",
    "examples/czml-tutorial": "_static/thumbnails/cesium_thumbnail.png",
    "examples/generating-orbit-groundtracks": "_static/thumbnails/groundtrack.png",
    "examples/detecting-events": "_static/thumbnails/eclipse.png",
    "examples/loading-OMM-and-TLE-satellite-data": "_static/thumbnails/omm_debris.png",
    "examples/multirevolutions-solution-in-lamberts-problem": "_static/thumbnails/lambert_paths.png",
}

nbsphinx_custom_formats = {
    ".myst.md": ["jupytext.reads", {"fmt": "mystnb"}],
}

# sphinx-autoapi configuration
autoapi_type = "python"
autoapi_dirs = ["../../src/"]
autoapi_options = [
    "members",
    "undoc-members",
    "show-inheritance",
    "show-module-summary",
    "special-members",
    "inherited-members",
]
autoapi_add_toctree_entry = False
autoapi_ignore = [
    "*_compat*",  # To avoid WARNING: more than one target found for cross-reference '__class__'
]

exclude_patterns.extend(["autoapi/index.rst", "autoapi/boinor/index.rst"])

# Ignore sphinx-autoapi warnings on reimported objects
# See https://github.com/readthedocs/sphinx-autoapi/issues/285
suppress_warnings.append("autoapi.python_import_resolution")

nbsphinx_allow_errors = True

latex_engine = "xelatex"

# FreeSerif needed for xelatex
latex_elements = {
    "fontpkg": """
\setmainfont{FreeSerif}[
  UprightFont    = *,
  ItalicFont     = *Italic,
  BoldFont       = *Bold,
  BoldItalicFont = *BoldItalic
]
\setsansfont{FreeSans}[
  UprightFont    = *,
  ItalicFont     = *Oblique,
  BoldFont       = *Bold,
  BoldItalicFont = *BoldOblique,
]
\setmonofont{FreeMono}[
  UprightFont    = *,
  ItalicFont     = *Oblique,
  BoldFont       = *Bold,
  BoldItalicFont = *BoldOblique,
]
""",
}

bibtex_bibfiles = ["boinor.bib"]

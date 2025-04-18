# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "REToys"
copyright = "2025, Reza Esfandiarpoor"
author = "Reza Esfandiarpoor"

import sys
from pathlib import Path

sys.path.insert(0, Path(__file__).parents[2].joinpath("src").resolve().as_posix())


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.duration",  # shows the build time of docs
    "sphinx_rtd_theme",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx_autodoc_typehints",
    # 'autoapi.extension',
    # "myst_parser",
    # 'sphinx_mdinclude',
]

# autoapi_dirs = ['../../src/retoys']
# autoapi_generate_api_docs=False


napoleon_include_init_with_doc = True

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for Autodoc --------------------------------------------------------------

autodoc_member_order = "bysource"
autodoc_preserve_defaults = True


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = "sphinx_rtd_theme"
# html_theme = "sphinx_book_theme"
html_theme = "furo"
html_title = "REToys"
html_static_path = ["_static"]

# html_theme_options = {
#         'collapse_navigation': True,
#         }

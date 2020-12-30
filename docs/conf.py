import os
import sys

# -- Project information -----------------------------------------------------

project = "16cIV"
copyright = "2020, Óscar Unzué"
author = "Óscar Unzué"

# master_doc = 'index'
# source_suffix = '.rst'

# -- Extensions --------------------------------------------------------------
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    'sphinx_tabs.tabs',
    "sphinx-hoverxref"
]

# -- Options for HTML output -------------------------------------------------

html_title = project

# Sidebars
html_sidebars = {
   '**': ['globaltoc.html', 'sourcelink.html', 'searchbox.html'],
   'using/windows': ['windowssidebar.html', 'searchbox.html'],
}

# Theme

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import stanford_theme
    html_theme = "stanford_theme"
    html_theme_path = [stanford_theme.get_html_theme_path()]
    html_theme_options = {
        'collapse_navigation': False,
        'display_version': False,
        'navigation_depth': 3,
    }
else:
    html_theme_options = {
        "rightsidebar": "true",
        "relbarbgcolor": "red"
    }

# otherwise, readthedocs.org uses their theme by default, so no need to specify it

# Other Theme
# html_theme = "sphinx_ansible_theme"
# html_theme = "sphinx_materialdesign_theme"
# html_theme = "sphinx_veldus_theme"
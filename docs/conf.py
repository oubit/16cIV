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
    'sphinx_tabs.tabs'
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

# otherwise, readthedocs.org uses their theme by default, so no need to specify it



# Ansible Theme
# extensions.append("sphinx_ansible_theme.ext.pygments_lexer")
# html_theme = "sphinx_ansible_theme"
# highlight_language = 'YAML+Jinja'
# html_context = {'display_github': True, 'github_user': 'pradyunsg', 'github_repo': 'sphinx-themes', 'github_version': 'master/sample-docs/', 'github_root_dir': 'master/src', 'current_version': 'latest', 'latest_version': 'latest', 'available_versions': ('latest', ), 'css_files': (), }
# html_theme_options = {
#     'collapse_navigation': False, 
#     'analytics_id': '', 
#     'style_nav_header_background': '#5bbdbf', 
#     'style_external_links': True, 
#     'canonical_url': 'https://pradyunsg.me/sphinx-themes/', 
#     'vcs_pageview_mode': 'edit', 
#     'navigation_depth': 3, 
# }
# pygments_style = 'sphinx'

# html_theme = "sphinx_materialdesign_theme"

# html_theme = "sphinx_veldus_theme"

# html_theme = "classic"
# html_theme_options = {
#     "rightsidebar": "true",
#     "relbarbgcolor": "red"
# }
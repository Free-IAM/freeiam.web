"""Sphinx configuration for FreeIAM Web."""

project = 'FreeIAM Web'
author = 'Florian Best'
html_theme = 'furo'
root_doc = 'index'

extensions = [
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'freeiam': ('https://docs.freeiam.org/en/latest/', None),
}

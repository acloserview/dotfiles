# Enable spellcheck.
c.spellcheck.languages = ["en-US"]

# Use DuckDuckGo with custom params as home and search.
DDG = "https://duckduckgo.com/?kae=d&k1=-1&kk=-1&kak=-1&kax=-1&kaq=-1&kap=-1&kao=-1&kau=-1&kba=-1"
c.url.start_pages = [DDG]
c.url.searchengines = {
    "DEFAULT": "%s&q={}" % DDG,
    "ddg": "%s&q={}" % DDG,
}

# Launch vim in termite for editor.
c.editor.command = ['termite', '-t', 'edit_text', '-e', 'vim {}']

# Load new tabs in the background.
c.tabs.background = True

# Disable autoplay.
c.content.autoplay = False

# Do not store cookies after the sesion is closed.
c.content.cookies.store = False

# Vim-like tab navigation.
config.bind("gT", "tab-prev")
config.bind("gt", "tab-next")

# Zoom
config.bind("zi", "zoom-in")
config.bind("zo", "zoom-out")
config.bind("z0", "zoom 100")

# Launch inspector.
config.bind("x", "devtools bottom")

# Enable/disabled javascript.
config.bind("xjn", "set content.javascript.enabled true")
config.bind("xjf", "set content.javascript.enabled false")

# Theme
config.source('base16-gruvbox-dark-hard.config.py')

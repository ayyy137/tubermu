r"""
Evennia settings file.

The available options are found in the default settings file found
here:

https://www.evennia.com/docs/latest/Setup/Settings-Default.html

Remember:

Don't copy more from the default file than you actually intend to
change; this will make sure that you don't overload upstream updates
unnecessarily.

When changing a setting requiring a file system path (like
path/to/actual/file.py), use GAME_DIR and EVENNIA_DIR to reference
your game folder and the Evennia library folders respectively. Python
paths (path.to.module) should be given relative to the game's root
folder (typeclasses.foo) whereas paths within the Evennia library
needs to be given explicitly (evennia.foo).

If you want to share your game dir, including its settings, you can
put secret game- or server-specific settings in secret_settings.py.

"""

# Use the defaults from Evennia unless explicitly overridden
from evennia.settings_default import *

######################################################################
# Evennia base server config
######################################################################

SERVERNAME = "Tubermu"
GAME_SLOGAN = "The best MUD/MU* for roleplaying as a tuber."
SERVER_HOSTNAME = "45.55.38.136"
ALLOWED_HOSTS = ["45.55.38.136"]
IN_GAME_ERRORS = False
TIME_FACTOR = 1.0
# TODO
TIME_GAME_EPOCH = None https://www.epochconverter.com/
TIME_IGNORE_DOWNTIMES = True
AUTO_CREATE_CHARACTER_WITH_ACCOUNT = False
DEFAULT_CHANNELS = [
    {
        "key": "Staff",
        "aliases": ("wish",),
        "desc": "Message staff",
        "locks": "control:perm(Admin);listen:perm(Admin);send:all()",
    }
]
GAME_INDEX_ENABLED = True
# This dict
GAME_INDEX_LISTING = {
    "game_name": "TuberMu",  # usually SERVERNAME
    "game_status": "pre-alpha",  # pre-alpha, alpha, beta or launched
    "short_description": "The best MUD/MU* for roleplaying as a tuber.",  # could be GAME_SLOGAN
    "long_description": "TuberMu is a bit of a joke, but we really are roleplaying as tubers. It's relaxing.",
    "listing_contact": "",  # email
    "telnet_hostname": "45.55.38.136",  # mygame.com
    "telnet_port": "4000",  # 1234
    "game_website": "http://45.55.38.136",  # http://mygame.com
    "web_client_url": "http://45.55.38.136/webclient",  # http://mygame.com/webclient
}

######################################################################
# Settings given in secret_settings.py override those in this file.
######################################################################
try:
    from server.conf.secret_settings import *
except ImportError:
    print("secret_settings.py file not found or failed to import.")

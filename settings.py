from os import environ
from pathlib import Path

# BASE DIRECTORY
BASE_DIR = Path(__file__).resolve().parent

# DEBUG MODE

debug = True


# -------------------
# SESSION CONFIGS
# -------------------
SESSION_CONFIGS = [
    dict(
        name = 'Experiment_stage1',
        display_name = "實驗第一階段",
        num_demo_participants = 4 if debug else 12,
        app_sequence = ['phase1', 'phase2', 'phase_AI'],
    ),
]

SESSION_CONFIG_DEFAULTS = dict(
    display_name = "第一階段",
    real_world_currency_per_point = 1.00,
    participation_fee = 150.00,
    doc="",
)

# -------------------
# LANGUAGE & CURRENCY
# -------------------
LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = ''
REAL_WORLD_CURRENCY_DECIMAL_PLACES = 0
USE_POINTS = False

# -------------------
# ADMIN
# -------------------
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin'

# optional HTML for demo page
DEMO_PAGE_INTRO_HTML = ""

# SECRET_KEY required by Django
SECRET_KEY = 'replace-with-a-random-string'

# -------------------
# INSTALLED APPS
# -------------------
INSTALLED_APPS = ['otree']

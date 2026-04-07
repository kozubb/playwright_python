import os

CI = os.getenv("CI", "false").lower() == "true"
HEADLESS = True if CI else False

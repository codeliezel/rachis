import os

environment = os.getenv("ENV", "dev")

if environment == "dev":
    from rachis.settings.dev import *  
    
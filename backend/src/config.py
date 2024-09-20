# File: config.py
# Author: victo
# Copyright: 2024, Smart Cities Peru.
# License: MIT
#
# Purpose:
# This is the entry point for the application.
#
# Last Modified: 2024-09-17
# src/config.py
import os

API_BASE_URL = "https://firms.modaps.eosdis.nasa.gov/api/area/csv/a4af9f9db9f15fd4ceb35731121ce9fc/VIIRS_NOAA20_NRT"

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:12345678@localhost:3306/HackathonDb'
SQLALCHEMY_TRACK_MODIFICATIONS = False

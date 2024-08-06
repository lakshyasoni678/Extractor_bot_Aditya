#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


import os

class Config(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7406110931:AAGiW_lENMzLpPfRErJmmCmhU25472Kh2Pg")


    # Get from my.telegram.org (or @UseTGXBot)
    APP_ID = int(os.environ.get("APP_ID", "29640188"))
    API_HASH = os.environ.get("API_HASH", "e470abc84a3bc445997ee4ea5be87deb")


    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "6364152774").split())
    

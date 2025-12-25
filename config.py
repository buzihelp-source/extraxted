#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8255874281:AAGyI2bW1XVuzXrLP48qSL1zMdkT9PlZuI4")
    API_ID = int(os.environ.get("API_ID", "30587265"))
    API_HASH = os.environ.get("API_HASH", "49a5bcb36e6d5350db387ba444338f37")
    AUTH_USERS = "7759336095"





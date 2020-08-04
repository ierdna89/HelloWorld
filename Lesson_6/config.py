import os

class Config:
    SERCRET_KEY = os.environ.get("SERCRET_KEY") or "you-will-never-guess"
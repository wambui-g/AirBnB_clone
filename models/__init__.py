#!/usr/bin/python3
"""module to initialize the packages"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()

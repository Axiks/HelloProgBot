import os
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import sqlite3

from config.config import TOKEN
DATABASE_PATH = 'database/database.sqlite';
## Бот якому можна описати свої скили

conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()

# init tible
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, telegram_id INTEGER NOT NULL, username text); ")
cursor.execute("CREATE TABLE IF NOT EXISTS skills (id INTEGER PRIMARY KEY AUTOINCREMENT, title text); ")
cursor.execute("CREATE TABLE IF NOT EXISTS users_skills (user_id INTEGER NOT NULL, skill_id INTEGER NOT NULL); ")


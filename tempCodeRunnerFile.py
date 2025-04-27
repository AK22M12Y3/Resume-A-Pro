from flask import Flask, render_template, request, redirect, url_for, session, abort, flash  # Added flash here
import os
import docx2txt
import fitz  # PyMuPDF
import re
from werkzeug.utils import secure_filename
import nltk
from nltk.corpus import stopwords
from collections import Counter
import sqlite3
from datetime import datetime
from functools import wraps
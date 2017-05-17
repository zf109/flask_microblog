#! flask/Scripts/python

import os
import sys
sys.path.append(os.getcwd())
from app import db

db.drop_all()

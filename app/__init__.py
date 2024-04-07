from flask import Flask
app = Flask(__name__)
from app.services import ProcessImage, GetImgurCredits

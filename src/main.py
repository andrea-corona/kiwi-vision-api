from flask import Flask
from flask_restful import Api
from src.config import configuration
from src.routes.image_prediction.model_predict import predict
from src.extensions import crs

app = Flask(__name__)

app.config.from_object(configuration['deployment'])
crs.init_app(app)
app.register_blueprint(predict)

if __name__ == '__main__':
    app.run()

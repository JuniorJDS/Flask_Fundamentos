from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from flask_babel import Babel

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
# protecao no envio de formularios
csrf = CSRFProtect(app)
csrf.init_app(app)

# exibe erros de validação em Portugues
babel = Babel(app)

from .views import cliente_view
from .models import cliente_model

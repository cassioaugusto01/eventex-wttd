# Eventex

Sistema de eventos

## Como desenvolver

1. Clone o repositorio
2. Crie um virtualenv com Python 3.10
3. Ative o virtualenv
4. Instale as dependencias
5. Configure a intancia com o .env
6. execute os testes

'''console
git clone git@github.com:cassioaugusto01/eventex-wttd.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
'''

## Como fazer o deploy

1. Crie uma instancia no heroku
2. Envie as configurações para o heroku
3. Defina uma SECRET_KEY segura para a instancia
4. Defina DEBUG=False
5. Configure o serviço de email
6. Envie o codigo para o heroku

'''console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configure o email
git push heroku master --force
'''
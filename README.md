This is a chess game that allows you to play against an AI agent utilizing the minimax algorithm. 

The game is implemented as a Django project and can be servered using python manage.py runserver

Note requires the dependencies in requirements.txt to be installed. e.g. pip install -r requirements.txt

The project is confiigurd to run on the heroku platform. To deploy otherwise remove Django-heroku import from settings.py

The project also contains a command line chess UI in python that can be access in the web-chess_ai_app/ai_modules directory by running python chess_game.py


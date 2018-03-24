from tornado.escape import json_decode
from game import Game
from dao import GameDao
import json
import logging
import tornado.web

class GameHandler(tornado.web.RequestHandler):
    @property
    def redis(self):
        return self.application.redis

    @property
    def logger(self):
        return logging.getLogger(__name__)

    def get(self, game_id=None):
        try:
            game_dao = GameDao(self.redis)
            if game_id:
                game = game_dao.get_saved_game(game_id)
                if not game:
                    self.set_status(404)
                    return
                self.set_status(200)
                self.write(game.to_json())
            else:
                games = game_dao.get_all()
                response = {
                    'games': games
                }
                self.set_status(200)
                self.write(response)
        except Exception as e:
            self.logger.error(str(e))
            self.set_status(400)


    def post(self, game_id=None):
        try:
            data = json_decode(self.request.body)
            game_dao = GameDao(self.redis)
            if game_id:
                board = data['board']
                if not Game.validate_board(board):
                    self.set_status(400)
                    return
                game = game_dao.get_saved_game(game_id)
                game.update_game(board)
                game_dao.save(game)
                self.set_status(204)
            else:
                # create new game
                player1 = data['player1']
                player2 = data['player2']
                move = 0
                board = [None for i in range(9)]
                status = Game.in_progress
                # create new game, incrementing last ID in redis to ensure unique ID
                new_game = Game(game_dao.get_next_id(), player1, player2, board, status, move)
                game_dao.save(new_game)
                self.set_status(201)
                self.write(new_game.to_json())
        except Exception as e:
            self.logger.error(str(e))
            self.set_status(400)

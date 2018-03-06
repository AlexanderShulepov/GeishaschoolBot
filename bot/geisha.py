import os
import time

import cherrypy

from handlers import *


# Наш вебхук-сервер
class WebhookServer(object):
    @cherrypy.expose
    def index(self):
        length = int(cherrypy.request.headers['content-length'])
        json_string = cherrypy.request.body.read(length).decode("utf-8")
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''


def launch_server():
    WEBHOOK_PORT = 7775
    WEBHOOK_KILL_PORT_COMMAND = 'sudo fuser -n tcp -k %d' % WEBHOOK_PORT
    os.system(WEBHOOK_KILL_PORT_COMMAND)

    cherrypy.config.update({
        'server.socket_host': '127.0.0.1',
        'server.socket_port': WEBHOOK_PORT,
        'engine.autoreload.on': False
    })
    cherrypy.quickstart(WebhookServer(), '/', {'/': {}})


if __name__ == '__main__':
    launch_server()
    # while True:
    #     try:
    #         bot.polling(none_stop=False)
    #     except Exception as e:
    #         with open('c_crashlog.txt', 'w') as f:
    #             f.write(str(e))
    #     time.sleep(17)
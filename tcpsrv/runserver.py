# -*- coding: UTF-8 -*-
import threading
import os
import sys
from setproctitle import setproctitle, getproctitle

from app.helpers.tcp_socket_server import serveur, traitementDonnées
from app.helpers.logging import logger

HOST = '0.0.0.0'
PORT = int(os.environ.get('SERVER_PORT'))


threads = []


if __name__ == '__main__':
    srv = serveur((HOST, PORT), traitementDonnées)
    setproctitle('3cxtcpserver')
    log = 'Server loop ' + getproctitle() + ' running in process: ' + str(os.getpid())
    logger.info(log)
    try:
        srv.serve_forever()
        # srv3cxon = threading.Thread(target=srv.serve_forever)
        # srv3cxon.daemon = True
        # srv3cxon.start()

        # threads.append((srv3cxon, srv))
    except KeyboardInterrupt:
        sys.exit(0)
        # def kill_me_please(server):
        #     for t, s in threads:
        #         s.server_close()
        #         s.shutdown()
        #     for t, s in threads:
        #         t.join()
        #     print('server down...')
        # threading.Thread(target=kill_me_please, args=(srv,)).start()
        # print("End")
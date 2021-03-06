import socket
import logging
from cement.core.foundation import CementApp
from cement.utils.misc import init_defaults
from pyspeedo.core.daemon import PySpeedoDaemon

defaults = init_defaults('pyspeedo', 'monitoring')
defaults['monitoring']['host'] = socket.gethostname()
defaults['monitoring']['server'] = None
defaults['monitoring']['interval'] = 900
defaults['monitoring']['dburl'] = 'sqlite:///:memory:'


class PySpeedoApp(CementApp):
    class Meta:
        label = 'pyspeedo'
        config_defaults = defaults
        arguments_override_config = True


def configure_log(level=logging.DEBUG):
    handler = logging.StreamHandler()
    handler.setLevel(level)
    formatter = logging.Formatter(
        '%(asctime)s (%(levelname)s) %(name)s : %(message)s')
    handler.setFormatter(formatter)
    log = logging.getLogger('pyspeedo')
    log.setLevel(level)
    log.addHandler(handler)
    log = logging.getLogger('pyspeedtest')
    log.setLevel(level)
    log.addHandler(handler)


def main():
    with PySpeedoApp() as app:
        app.args.add_argument(
            '-H', '--host',
            action='store',
            dest='host',
            help='The host on which this script is running')
        app.args.add_argument(
            '-s', '--server',
            action='store',
            dest='server',
            help='The server to use to perform the speed test')
        app.args.add_argument(
            '-i', '--interval',
            action='store',
            dest='interval',
            help='The interval between two speed tests')
        app.args.add_argument(
            '-d', '--db-url',
            action='store',
            dest='dburl',
            help='The database url')
        app.run()
        logLevel = logging.DEBUG if app.debug else logging.WARNING
        configure_log(logLevel)
        conf = app.config.get_section_dict('monitoring')
        daemon = PySpeedoDaemon(**conf)
        daemon.run()

if __name__ == '__main__':
    main()

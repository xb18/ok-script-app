from ok import OK
from src.config import config


if __name__ == '__main__':
    web_config = dict(config)
    web_config.pop('my_app', None)
    web_config['gui'] = {
        'type': 'web',
        'launch_mode': 'pywebview',
    }
    OK(web_config).start()

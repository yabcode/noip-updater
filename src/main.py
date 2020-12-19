import json
from typing import Optional

from no_ip import NoIp
from logger import LOG


def load_config(file_path: str) -> Optional[dict]:
    try:
        with open(file_path) as f:
            d = json.load(f)
            return d
    except Exception as e:
        LOG.critical(f'config load error. {e}')
        return None


def main(config: dict):
    LOG.info('Start main()')

    noip = NoIp(config["no_ip"])
    success = noip.login()
    if success:
        noip.confirm()

    LOG.info('End main()')


if __name__ == '__main__':
    config = load_config('config.json')
    if config:
        main(config)

from configparser import ConfigParser
import paypalrestsdk


class PayPalConfig:

    @staticmethod
    def run_config(location):
        config = ConfigParser()
        config.read(location + '/credentials.ini')
        paypalrestsdk.configure({
            "mode": config.get('sandbox', 'mode'),
            "client_id": config.get('sandbox', 'client_id'),
            "client_secret": config.get('sandbox', 'client_secret')
        })
        print('PayPal configuration loaded')

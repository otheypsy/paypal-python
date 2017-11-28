from config.PayPalConfig import PayPalConfig
import logging

logging.basicConfig(level=logging.INFO)
PayPalConfig.run_config('config')
currency = 'USD'

import app.payment.create

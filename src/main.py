'''
Created on Aug 17, 2013

@author: jonmellman
'''

from weatherdata import WeatherData
from ledmanager import LEDManager
import utils
import os
import sys

# running in development mode by default
# (development mode bypasses calls to IO pin calls)
developmentMode = True

LOGTAG = os.path.basename(__file__)


def main():
    utils.log(LOGTAG, 'Starting main method..')
    
    if not utils.hasInternet():
        utils.log(LOGTAG, 'No internet connection, aborting program.')
        sys.exit()
    
    forecast = WeatherData()
    fText = forecast.getForecastText()
    utils.log(LOGTAG, 'Retrieved forecast text: ' + fText)
    
    fPrecip = forecast.getPrecipitation()
    utils.log(LOGTAG, 'Retrieved precipitation value: ' + fPrecip)
    
    
    if not developmentMode:
        textToLED(fText)
    
def textToLED(text):
    if text == 'Partly Sunny':
        pass
    elif text == 'Mostly Sunny':
        pass
    elif text == 'Sunny':
        pass
    elif text == 'Partly Cloudy':
        pass
    elif text == 'Mostly Cloudy':
        pass
    elif text == 'Cloudy':
        pass
    elif text == 'Showers':
        pass
    elif text == 'Rain / Thunder':
        pass
    elif text == 'N/A':
        pass
    else:
        utils.log(LOGTAG, 'Not sure what to do with text: ' + text)
            
if __name__ == '__main__':
    if utils.getSocketHostName() == 'beaglebone':
        developmentMode = False
    main()
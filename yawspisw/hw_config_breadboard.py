#=================================================================
# yawspi hardware configuration
#=================================================================

# hw adress is composed of two numbers - first one is index of the hw device,
# second one is pin number.
# GPIO: [0, X]
# PE1:  [1, X]
# PE2:  [2, X]
# ADC1: [-1, X]
# ADC2: [-2, X]


def hw_config():

    # initialize dictionary with hardware settings:
    tmp = {}

    # ------------------- IO outputs:
    # first adrress is RPi GPIO, next adresses are I2C addresses of port
    # expanders MCP23017 (multiple port expanders possible)
    tmp['PeAddresses'] = (0x27, 0x22)

    # ------------------- Analog to Digital Converter:
    # Pins on Raspberry Pi GPIO of the clockpin, misopin, mosipin, cspin for AD
    # converters MCP3008:
    tmp['AdcPins'] = ((23, 19, 21, 13), (23, 19, 21, 24))

    # ------------------- Weather Sensors:
    tmp['SeTemp'] = 0     # temperature sensor present
    tmp['SeRain'] = 1     # rain sensor present
    tmp['SeRainPin'] = (-2, 1)  # rain sensor pin
    tmp['SeHumid'] = 0    # humidity sensor present
    tmp['SePress'] = 1    # pressure sensor present
    tmp['SeIllum'] = 1    # illuminance sensor present
    tmp['SeIllumAddrToHigh'] = 1    # illuminance address pin set to high?

    # ------------------- Water Source:
    # source of water with pump (or valve)
    # source capacity: if unlimited, water capacity of the source is -1, else
    # water capacity is limited and volume is in liters
    # pin of pump relay or valve connected to port expander
    # Speed is speed of pump or flow rate of the source approx. flowrate of the
    # pump in litres per second, volume of pumped water is calculated according
    # equation: volume = offset + rate * time
    # (offset, rate)
    # SettleT is time source needs to stop the water flow after switching off
    tmp['So'] = {
        'Cap': 10,
        'Pin': (1, 7),
        'FlowRate': (0, 1),
        'SettleT': 0.1,
    }

    # ------------------- Stations:
    # each station has one valve.
    # Cap is water capacity of each station in litres:
    # Pin is IO pin of valve
    # SettleT is time valve needs to fully open
    tmp['St'] = (
        {
            'Cap': 1.0,
            'Pin': (1, 2),
            'SettleT': 0.1,
        },
        {
            'Cap':  0.5,
            'Pin':  (2, 7),
            'SettleT': 0.1,
        },
    )

    # ------------------- Water Level Sensors:
    # possible sensor types:
    #   none - no water level sensor, amount of water is determined by water
    #       capacity
    #   min - switch at the bottom of the water container of the station
    #       (detects container is empty)
    #   max- switch at the top the water container of the station
    #      (detects container is full)
    #   minmax - switch at the bottom and top of the station water container
    #      (detects container is empty and is full)
    #   grad - some analog sensor
    #
    # last sensor is water source sensor (if source is unlimited, set sensor
    # type none.
    tmp['SeWL'] = (
        #{
        #    'Type':  'none',
        #},
        #{
        #    'Type':  'min',
        #    'Pin':  (1, 0),
        #},
        #{
        #    'Type':  'max',
        #    'Pin':  (1, 1),
        #},
        #{
        #    'Type':  'minmax',
        #    'MinPin':  (1, 2),
        #    'MaxPin':  (1, 3),
        #},
        {
            'Type':  'grad',
            'ValuePin':  (-1, 0),
            'OnOffPin':  (1, 0),
        },
        {
            'Type':  'grad',
            'ValuePin':  (-2, 0),
            'OnOffPin':  (2, 8),
        },
        {
            'Type':  'none',
        },
    )

    return tmp

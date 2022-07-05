import configparser
config = configparser.RawConfigParser()
configFilepath = r'C:\Users\user\PycharmProjects\selenium_Project\Configurations\config.ini'
config.read(configFilepath)

class readConfig:
    @staticmethod
    def getApplicationURL():
        URL = config.get('common info', 'Base_URL')
        return URL

    @staticmethod
    def getUseremail():
        email = config.get('common info', 'username')
        return email

    @staticmethod
    def getUserPassword():
        password = config.get('common info', 'password')
        return password
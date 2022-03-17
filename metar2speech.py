import requests
from PythonMETAR import *
import gtts
from gtts.tokenizer import pre_processors
import gtts.tokenizer.symbols

class Converter:

    def __init__(self):
        self.__setupGTTS()

    def __setupGTTS(self):
        gtts.tokenizer.symbols.SUB_PAIRS.append(('0.', 'Zero'))
        gtts.tokenizer.symbols.SUB_PAIRS.append(('1.', 'One'))
        gtts.tokenizer.symbols.SUB_PAIRS.append(('2.', 'Two'))
        gtts.tokenizer.symbols.SUB_PAIRS.append(('3.', 'Tree'))
        gtts.tokenizer.symbols.SUB_PAIRS.append(('4.', 'Four'))
        gtts.tokenizer.symbols.SUB_PAIRS.append(('5.', 'Fife'))
        gtts.tokenizer.symbols.SUB_PAIRS.append(('6.', 'Six'))
        gtts.tokenizer.symbols.SUB_PAIRS.append(('7.', 'Seven'))
        gtts.tokenizer.symbols.SUB_PAIRS.append(('8.', 'Eight'))
        gtts.tokenizer.symbols.SUB_PAIRS.append(('9.', 'Niner'))
        gtts.tokenizer.symbols.SUB_PAIRS.append(('cavok.', 'cave ok'))
        gtts.tokenizer.symbols.SUB_PAIRS.append(('-.', 'Minus'))


    def __spellNumber(self, Number):
        output = ''
        for letter in str(Number):
            output += letter + "."

        return output

    def __getCloud(self, CloudInfos):
        cloudText = ''
        if CloudInfos:
            cloudText = 'Clouds '
            for cloud in CloudInfos:
                cloudText += cloud['meaning'] + " " + str(cloud['altitude']) + "ft" + " "
            cloudText += ", "
        return cloudText

    def __getTemperature(self, TemperaturesInfos):
        tempInfo = str.format('Temperature {0} Dew point {1}, ', self.__spellNumber(TemperaturesInfos["temperature"]), self.__spellNumber(TemperaturesInfos['dewpoint']))
    
        return tempInfo

    def __getWind(self, WindInfo):
        WindDir = ''
        if WindInfo['direction'] == 'VRB':
            WindDir = 'VRB'
        else:
            WindDir = self.__spellNumber(WindInfo['direction']) + '°'

        windText = str.format('wind {0} {1} knots', WindDir, self.__spellNumber(WindInfo['speed']))

        if WindInfo['variation'] != None:
            windText += str.format(", variable between {0}° and {1}°", self.__spellNumber(WindInfo['variation'][0]), self.__spellNumber(WindInfo['variation'][1]))

        return windText + ", "

    def __getVisibility(self, VisibilityInfo):
        if VisibilityInfo == None:
            return "cavok., " 

        elif VisibilityInfo == 9999:
            return "visibility 10 kilometers or more, "
        else:
            return str.format('visibility {0} meters, ', VisibilityInfo)

    def __getTime(self, MetarTime):
        return self.__spellNumber( str.format('{0}{1}', MetarTime[1], MetarTime[2]))

    def __getQNH(self, QNH):
        return str.format("QNH {0}", self.__spellNumber(QNH))

    def __getMetarVoiceText(self):
        return str.format("Weather report at {0}, {1}{2}{3}{4}{5}", self.__getTime(self.decodedMetar.date_time), self.__getWind(self.decodedMetar.wind), self.__getVisibility(self.decodedMetar.visibility), self.__getCloud(self.decodedMetar.cloud), self.__getTemperature(self.decodedMetar.temperatures), self.__getQNH(self.decodedMetar.qnh))

    def __saveMetarToAudio(self, OutputFolder):
        if OutputFolder != '':
            filename = str.format("{0}\\{1}.mp3", OutputFolder, self.lastICAO)
        else:
            filename = str.format("{0}.mp3", self.lastICAO)
        
        tts = gtts.gTTS(self.voiceTextMetar, lang='en').save(filename)

    def GetMetar(self, ICAO_Code, saveasmp3=False, outputfolder=''):
        self.lastICAO = str.upper(ICAO_Code)
        
        metarURL = str.format("https://tgftp.nws.noaa.gov/data/observations/metar/stations/{0}.TXT", self.lastICAO)
        self.rawMetar = requests.get(metarURL).text
        self.decodedMetar = Metar(ICAO_Code, self.rawMetar)
        self.voiceTextMetar = self.__getMetarVoiceText()
        if saveasmp3:
            self.__saveMetarToAudio(outputfolder)

    

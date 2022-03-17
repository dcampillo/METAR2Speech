import metar2speech

m2s = metar2speech.Converter()

m2s.GetMetar("lsmp")

print(m2s.rawMetar)
print(m2s.lastICAO)
print(m2s.voiceTextMetar)
print(m2s.decodedMetar.wind)


m2s.SaveMetarToAudio("c:\\temp\\")
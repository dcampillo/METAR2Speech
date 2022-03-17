import metar2speech

# Create an instace of the Converter
m2s = metar2speech.Converter()

icaos = {'lsmp', 'lszh', 'lsgg', 'lszb', 'lsza'}

for icao in icaos:
    m2s.GetMetar(icao, saveasmp3=False, outputfolder='c:\\tmp\\')
    print(m2s.voiceTextMetar)

# Retrieve METAR
#m2s.GetMetar("lsgg", saveasmp3=True, outputfolder='c:\\tmp\\')
#m2s.GetMetar("lsgs", saveasmp3=True, outputfolder='c:\\tmp\\')
#m2s.GetMetar("lszh", saveasmp3=True, outputfolder='c:\\tmp\\')
#m2s.GetMetar("lszb", saveasmp3=True, outputfolder='c:\\tmp\\')

#Print the METAR as downloaded
#print(m2s.rawMetar)

# Print the METAR converted to speakable version by gTTs
#print(m2s.voiceTextMetar)


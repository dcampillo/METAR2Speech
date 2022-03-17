import metar2speech

# Create an instace of the Converter
m2s = metar2speech.Converter()

# Retrieve METAR
m2s.GetMetar("lsmp")

#Print the METAR as downloaded
print(m2s.rawMetar)

# Print the METAR converted to speakable version by gTTs
print(m2s.voiceTextMetar)

# Generate and save the METAR in a mp3 file
m2s.SaveMetarToAudio("c:\\temp\\")
import AutoTune
import pyaudio
import wave
import random

FORMAT                = pyaudio.paInt16
CHANNELS              = 2
RATE                  = 44100
CHUNK                 = 1024
RECORD_SECONDS        = 5
WAVE_OUTPUT_FILENAME  = "file.wav"

audio = pyaudio.PyAudio()

# start Recording
stream = audio.open(format=FORMAT,
  channels=CHANNELS,
  rate=RATE, input=True,
  frames_per_buffer=CHUNK)
print "=====> recording..."
frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
  data = stream.read(CHUNK)
  frames.append(data)

print "=====> finished recording"

# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()

# Write .wav file.
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()

# Play .wav file.
wf      = wave.open(WAVE_OUTPUT_FILENAME, 'rb')
p       = pyaudio.PyAudio()
stream  = p.open(
  format    = p.get_format_from_width(wf.getsampwidth()),
  channels  = wf.getnchannels(),
  rate      = wf.getframerate(),
  output    = True
  )
data    = wf.readframes(CHUNK)
while data is not '':
  stream.write(data)
  data = wf.readframes(CHUNK)

stream.stop_stream()
stream.close()
p.terminate()

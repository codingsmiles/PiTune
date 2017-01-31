import pyaudio
import wave
import audio_options

def play(filename):
  """
  Play .wav file.

  Params:
    filename - Name of the .wav file to be played.
  """
  # Play .wav file.
  wf      = wave.open(filename, 'rb')
  data    = wf.readframes(audio_options.CHUNK)
  p       = pyaudio.PyAudio()
  stream  = p.open(
    format    = p.get_format_from_width(wf.getsampwidth()),
    channels  = wf.getnchannels(),
    rate      = wf.getframerate(),
    output    = True
    )

  while data is not '':
    stream.write(data)
    data = wf.readframes(audio_options.CHUNK)

  stream.stop_stream()
  stream.close()
  p.terminate()

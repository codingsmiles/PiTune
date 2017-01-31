import pyaudio
import wave
import audio_options

def record(duration, filename):
  """
  Record sound from the microphone.

  Params:
    duration - How long should the recording be.
    filename - Name of the audio file where to write the audio.
  """
  audio   = pyaudio.PyAudio()
  frames  = []
  stream  = audio.open(
    format=audio_options.FORMAT,
    channels=audio_options.CHANNELS,
    rate=audio_options.RATE,
    input=True,
    frames_per_buffer=audio_options.CHUNK
  )

  for i in range(0, int(audio_options.RATE / audio_options.CHUNK * duration)):
    data = stream.read(audio_options.CHUNK)
    frames.append(data)

  stream.stop_stream()
  stream.close()
  audio.terminate()

  __write_audio_file(audio, frames, filename)

def __write_audio_file(audio, frames, filename):
  """
  Write audio from a PyAudio object to a file.

  Params:
    audio - PyAudio Object.
    frames - Frames with the audio data.
    filename - Name of the file where to store the audio.
  """
  audio_file = wave.open(filename, 'wb')
  audio_file.setnchannels(audio_options.CHANNELS)
  audio_file.setsampwidth(audio.get_sample_size(audio_options.FORMAT))
  audio_file.setframerate(audio_options.RATE)
  audio_file.writeframes(b''.join(frames))
  audio_file.close()

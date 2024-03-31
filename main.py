import sounddevice as sd
from scipy.io.wavfile import write

freq = int(input("Enter Sampling frequency 'example(44100)': "))
duration = int(input("Enter Recording duration 'example(5)': "))

# Start the recorder with the given values
# of duration and sample frequency
recording = sd.rec(int(duration * freq),
                   samplerate=freq, channels=2)

# Wait for the recording to finish
sd.wait()

# Convert the NumPy array to an audio file
# with the given sampling frequency
write("recording.wav", freq, recording)

print("Recording saved as recording.wav")

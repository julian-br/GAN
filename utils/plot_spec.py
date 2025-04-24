import matplotlib.pyplot as plt
import librosa.display
import librosa
import numpy as np

def plot_and_save_spec(spec, output_path, sr=22050, hop_length=256, fmax=8000):
  mel_db = librosa.power_to_db(spec, ref=np.max)

  plt.figure(figsize=(10, 4))
  librosa.display.specshow(
      mel_db,
      sr=sr,
      hop_length=hop_length,
      x_axis='time',
      y_axis='mel',
      fmax=fmax,
      cmap='magma'
  )
  plt.colorbar(format="%+2.0f dB")
  plt.tight_layout()
  
  plt.savefig(output_path)
  plt.close()
import librosa
import numpy as np
from scipy.signal import resample_poly

def create_mel_spec(file_path, target_sr=22050):
    # Load audio at original SR
    y, sr = librosa.load(file_path, sr=None)

    if sr != target_sr:
      y = librosa.resample_poly(y, orig_sr=sr, target_sr=target_sr)

    # HiFi-GAN MelSpec Parameters
    mel_spec = librosa.feature.melspectrogram(
        y=y,
        sr=target_sr,
        n_fft=1024,
        hop_length=256,
        win_length=1024,
        n_mels=80,
        fmin=0,
        fmax=8000,
        power=1.0  # Wichtig: kein dB-Scaling
    )

    return mel_spec
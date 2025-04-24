
from utils.create_spec import create_mel_spec
from utils.plot_spec import plot_and_save_spec
import numpy as np

chord_spec= create_mel_spec("./data/chord-test.wav")
single_note_spec= create_mel_spec("./data/single-notes.wav")


plot_and_save_spec(chord_spec, "./output/chord-spec.png")
np.save("./output/chord-spec.npy", chord_spec)

plot_and_save_spec(single_note_spec, "./output/single-note-spec.png")
np.save("./output/single-note-spec.npy", chord_spec)
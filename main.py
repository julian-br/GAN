
from utils.create_spec import create_mel_spec
from utils.plot_spec import plot_and_save_spec
import numpy as np

guitar_performance_spec = create_mel_spec("./data/performance-cropped.wav")
hummed_melodie_spec = create_mel_spec("./data/hummed-melodie.wav")


plot_and_save_spec(guitar_performance_spec, "./output/performance-cropped-spec.png")
plot_and_save_spec(hummed_melodie_spec, "./output/hummed-melodie-spec.png")
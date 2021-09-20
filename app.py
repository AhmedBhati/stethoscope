import noisereduce as nr
from scipy.io.wavfile import write
from scipy.io.wavfile import read
from flask import Flask, request,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'check the noise reduction'

@app.route('/update', methods=['POST'])
def check():
    data1 = request.get_json()
    heart_beat = data1['heart_beat']
    doc_id = data1['doc_id']
    rate = 44100
    reduced_noise = nr.reduce_noise(y = heart_beat, sr=rate, n_std_thresh_stationary=1.5,stationary=False, freq_mask_smooth_hz=500,n_fft=2048)
    k = str(reduced_noise.tolist())
    return jsonify({'result': k})
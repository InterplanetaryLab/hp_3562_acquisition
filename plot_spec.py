import matplotlib.pyplot as plt
from decimal import Decimal

class data_3562A:
    def __init__(self):
        self.data_ind = 67 # first data index non header here
        self.header = {
                "display_func": "",
                "num_elem":0,
                "dis_elem":0,
                "num_avg":0,
                "chan_selec":"",
                "overflow_stat":"",
                "overlap_per":0,
                "domain":0,
                "volt_pk/rms":"",
                "amp_unit":"",
                "x_axis_units":"",
                "auto_math_label":"",
                "trace_label":"",
                "eu_label_1":"",
                "eu_label_2":"",
                "float/int":0,
                "complex/real":0,
                "live/recalled":0,
                "math_result":0,
                "real/complex_input":0,
                "log/lin":0,
                "auto_math":0,
                "real_time_status":0,
                "measurement_mode":"",
                "window": "",
                "demod_type_chan1": "",
                "demod_type_chan2": "",
                "demod_active_chan1": 0,
                "demod_active_chan2": 0,
                "average_status": "",
                "not_used": "",
                "samp_freq2_real": 0,
                "samp_freq2_img": 0,
                "not_used2": "",
                "delta_x_axis": 0,
                "max_range": 0,
                "start_time_value": 0,
                "exp_wind_const_1": 0,
                "exp_wind_const_2": 0,
                "eu_val_chan_1": 0,
                "eu_val_chan_2": 0,
                "trig_delay_chan_1": 0,
                "trig_delay_chan_2": 0,
                "start_freq_val": 0,
                "start_data_val": 0
                }
        self.freq = []
        self.mag = []
    def populate_header(self, str_array):
        self.header["display_func"] = float(str_array[1])
        self.header["num_elem"] = int(float(str_array[2]))
        print(self.header["num_elem"])
        self.header["dis_elem"] = int(float(str_array[3]))
        #skipping a fair amount of elements
        self.header["delta_x_axis"] = float(str_array[56])
        self.header["start_freq_val"] = float(str_array[65])
    def populate_data(self, str_array):
        # freq_populating
        self.freq = [0]*self.header["num_elem"]
        for i in range(len(self.freq)):
            self.freq[i] = self.header["delta_x_axis"]*i+self.header["start_freq_val"]
            print("freq: %.3E" %Decimal(self.freq[i]))

        self.mag = [0]*self.header["num_elem"]
        for i in range(len(self.mag)):
            self.mag[i] = float(str_array[i+self.data_ind])
            print("mag: %.3E" %Decimal(self.mag[i]))

    def print_data(self):
        fig,ax = plt.subplots()
        ax.plot(self.freq,self.mag)
        ax.set_title("Mag vs Freq Plot")
        ax.set_xlabel("Freq (Hz)")
        ax.set_ylabel("Mag (NA)")
        plt.show()

def read_spectrum(filename):
    lines = []
    with open(filename) as f:
        lines = [line.rstrip() for line in f]
        print("len of lines: %d" %len(lines))
    return lines

lines = read_spectrum("spectrum.txt")
data =  data_3562A()
data.populate_header(lines)
data.populate_data(lines)
data.print_data()

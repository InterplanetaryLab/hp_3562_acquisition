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

        self.x_axis_unit_map = ["No Unit", "Hertz", "RPM", "Orders", "Seconds", "Revs", "Degrees", "dB", "dBV", "Volts", "VSqrt(Hz)(sqrt(PSD))","Volts/EU","Vrms","V^2Hz (PSD)", "Percent" , "Points", "Records", "Ohms", "Hertz/Octave", "Pulse/Rev", "Decades", "Minutes", "V^2s/Hz(ESD)", "Octave", "Seconds/Decade","Seconds/Octave","Hz/Point","Points/Sweep","Points/Decade","Points/Octave","V/Vrms","V^2","EU referenced to Channel 1", "EU referenced to Channel 2", "EU Value"]
        self.window_map = ["Window not applicable", "Hann", "Flat top", "Uniform","Exponential","Force","Force chan1/expon chan 2", "Expon chan1/force chan2","Users"]
        self.domain_type_map = ["Time", "Frequency", "Voltage (amp)"]
        self.measurement_mode_map = ["Linear Resolution", "Log Resolution", "Swept sine", "Time Capture", "Linear Resolution Throughput"]
        self.y_axis_unit_map = ["Volts", "Volts^2", "PSD (V^2/Hz)", "ESD (V^2/Hz)","sqrt(PSD)(V/sqrt(Hz))","no amplitude units","Unit Volts", "Unit Volts^2"]
        self.channel_selection_map = ["Channel 1", "Channel 2", "Channels 1 & 2", "No Channel"]
        self.disp_function_map = ["No Data", "Frequency Response", "Power Spectrum 1", "Power Spectrum 2", "Coherence", "Cross Spectrum", "Input Time 1", "Input Time 2", "Input Linear Spectrum", "Input Linear Spectrum 2", "Impulse Response" , "Cross Correlation", "Auto Correlation 1", "Auto Correlation 2", "Histogram 1", "Histogram 2", "Cumulative Density Function 1", "Cumulative Density Function 2", "Probability Density Function 1", "Probability Density Function 2", "Average Linear Spectrum 1", "Average Linear Spectrum 2", "Average Time Record 1", "Average Time Record 2" , "Synthesis Pole-zero", "Synthesis Pole-Residue", "Synthesis Polynomial", "Synthesis Constant", "Windowed Time Record 1", "Windowed Time Record 2", "Windowed Linear Spectrum 1", "Windowed Linear Spectrum 2", "Filtered Time Record 1", "Filtered Time Record 2", "Filtered Linear Spectrum 1", "Filtered Linear Spectrum 2", "Time Capture Buffer", "Captured Linear Spectrum", "Capture Time Record", "Throughput Time Record 1", "Throughput Time Record 2", "Curve Fit", "Weighting Function", "Not Used", "Orbits", "Demodulation Polar", "Preview Demod Record 1", "Preview Demod Record 2","Preview Demod Linear Spectrum 1", "Preview Demod Linear Spectrum 2"]
    def populate_header(self, str_array):
        self.header["display_func"] = float(str_array[1])
        self.header["num_elem"] = int(float(str_array[2]))
        self.header["x_axis_units"] = float(str_array[11])
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

    def grab_data(self, serial_path = '/dev/ttyUSB1', addr=20, output_filename ="test.txt"):
        ser = serial.Serial(serial_path, 9600, timeout=0.5 )
        cmd = str.encode('++mode 1'+'\n','utf-8')
        print( 'Sending:', cmd)
        ser.write(cmd)
        s = ser.read(256);
        if len(s) > 0:
            print (s)

        cmd = str.encode('++addr '+str(addr)+'\n','utf-8')
        print( 'Sending:', cmd)
        ser.write(cmd)
        s = ser.read(256);
        if len(s) > 0:
            print (s)

        cmd = str.encode('++auto 1'+'\n','utf-8')
        print( 'Sending:', cmd)
        ser.write(cmd)
        s = ser.read(256);
        if len(s) > 0:
            print (s)

        cmd = str.encode('DDAS'+'\n','utf-8')
        print( 'Sending:', cmd)
        ser.write(cmd)
        f = open(output_filename, "wb")
        s = ""
        while (1):
            s = ser.read(20000);
            if len(s) > 0:
                f.write(s)
                print (s)
            else:
                break
        f.close()

def read_spectrum(filename):
    lines = []
    with open(filename) as f:
        lines = [line.rstrip() for line in f]
        print("len of lines: %d" %len(lines))
    return lines

if __name__ == '__main__':
    lines = read_spectrum("/mnt/cache/baud150_0db.txt")
    data =  data_3562A()
    data.populate_header(lines)
    data.populate_data(lines)
data.print_data()

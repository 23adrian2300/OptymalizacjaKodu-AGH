import matplotlib.pyplot as plt
import numpy as np

# Indicate the number of floating point operations that can be executed
# per clock cycle
nflops_per_cycle = 16

# Indicate the number of processors being used (in case you are using a
# multicore or SMP)
nprocessors = 1

# Indicate the clock speed of the processor.  On a Linux machine this info
# can be found in the file /proc/cpuinfo
#
# Note: some processors have a "turbo boost" mode, which increases
# the peak clock rate...
#
GHz_of_processor = 2.9


class Parser:
    def __init__(self, file_name) -> None:
        self.attrs = {}
        with open(file_name) as file:
            self.toks = file.read().split()
            self.toksi = 0
            file.close()
            self.attrs = self.parse()

    def next(self):
        tok = self.toks[self.toksi]
        self.toksi += 1
        return tok

    def get_var_name(self):
        return self.next()

    def get_symbol(self, sym):
        tok = self.next()
        assert(tok == sym)
        return tok

    def get_value(self):
        value = None
        tok = self.next()
        if tok == '[':
            # list
            value = []
            tok = self.next()
            while not tok.startswith(']'):
                value.append(float(tok))
                tok = self.next()
        elif tok.startswith("'"):
            value = tok[1:-2]
        
        assert value != None
        return value
    
    def parse(self):
        res = {}
        while self.toksi < len(self.toks):
            var = self.get_var_name()
            self.get_symbol('=')
            val = self.get_value()
            res[var] = val
        return res
    
    def __getattr__(self, name):
        return self.attrs[name]
    
def plot_optimize_1_9():
    m1 = Parser("output_MMult1.m")
    m2 = Parser("output_MMult2.m")
    m3 = Parser("output_MMult_1x4_3.m")
    m4 = Parser("output_MMult_1x4_4.m")
    m5 = Parser("output_MMult_1x4_5.m")
    m6 = Parser("output_MMult_1x4_6.m")
    m7 = Parser("output_MMult_1x4_7.m")
    m8 = Parser("output_MMult_1x4_8.m")
    m9 = Parser("output_MMult_1x4_9.m")

    #print(old)
    #print(new)

    m1_data = np.array(m1.MY_MMult).reshape(-1, 3)
    m2_data = np.array(m2.MY_MMult).reshape(-1, 3)
    m3_data = np.array(m3.MY_MMult).reshape(-1, 3)
    m4_data = np.array(m4.MY_MMult).reshape(-1, 3)
    m5_data = np.array(m5.MY_MMult).reshape(-1, 3)
    m6_data = np.array(m6.MY_MMult).reshape(-1, 3)
    m7_data = np.array(m7.MY_MMult).reshape(-1, 3)
    m8_data = np.array(m8.MY_MMult).reshape(-1, 3)
    m9_data = np.array(m9.MY_MMult).reshape(-1, 3)


    max_gflops = nflops_per_cycle * nprocessors * GHz_of_processor
    max_gflops = 20 # for better visualization

    fig, ax = plt.subplots()
    num_plots = 9
    colors = np.random.rand(num_plots, 3)  # Generating random RGB values

    ax.plot(m1_data[:,0], m1_data[:,1], linestyle='-.',color=colors[0], label= m1.version)
    ax.plot(m2_data[:,0], m2_data[:,1], linestyle='-.',color=colors[1], label= m2.version)
    ax.plot(m3_data[:,0], m3_data[:,1], linestyle='-.',color=colors[2], label= m3.version)
    ax.plot(m4_data[:,0], m4_data[:,1], linestyle='-.',color=colors[3], label= m4.version)
    ax.plot(m5_data[:,0], m5_data[:,1], linestyle='-.',color=colors[4], label= m5.version)
    ax.plot(m6_data[:,0], m6_data[:,1], linestyle='-.',color=colors[5], label= m6.version)
    ax.plot(m7_data[:,0], m7_data[:,1], linestyle='-.',color=colors[6], label= m7.version)
    ax.plot(m8_data[:,0], m8_data[:,1], linestyle='-.',color=colors[7], label= m8.version)
    ax.plot(m9_data[:,0], m9_data[:,1], linestyle='-.',color=colors[8], label= m9.version)


    ax.set(xlabel='m = n = k', ylabel='GFLOPS/sec.')
    ax.grid()
    ax.legend()

    ax.set_xlim([m1_data[0,0], m1_data[-1,0]])
    ax.set_ylim([0, max_gflops])

    fig.savefig(f"test_1_9_plot.png")
    # plt.show()
    
def plot_init():
    m1 = Parser("output_MMult1.m")
    #print(old)
    #print(new)

    m1_data = np.array(m1.MY_MMult).reshape(-1, 3)


    max_gflops = nflops_per_cycle * nprocessors * GHz_of_processor
    max_gflops = 20 # for better visualization

    fig, ax = plt.subplots()
    num_plots = 9
    colors = np.random.rand(num_plots, 3)  # Generating random RGB values

    ax.plot(m1_data[:,0], m1_data[:,1], linestyle='-.',color=colors[0], label= m1.version)



    ax.set(xlabel='m = n = k', ylabel='GFLOPS/sec.')
    ax.grid()
    ax.legend()

    ax.set_xlim([m1_data[0,0], m1_data[-1,0]])
    ax.set_ylim([0, max_gflops])

    fig.savefig(f"test_init_plot.png")
    # plt.show()
    
def plot_all():
    m1 = Parser("output_MMult1.m")
    m2 = Parser("output_MMult2.m")
    m3 = Parser("output_MMult_1x4_3.m")
    m4 = Parser("output_MMult_1x4_4.m")
    m5 = Parser("output_MMult_1x4_5.m")
    m6 = Parser("output_MMult_1x4_6.m")
    m7 = Parser("output_MMult_1x4_7.m")
    m8 = Parser("output_MMult_1x4_8.m")
    m9 = Parser("output_MMult_1x4_9.m")
    m10 = Parser("output_MMult_4x4_3.m")
    m11 = Parser("output_MMult_4x4_4.m")
    m12 = Parser("output_MMult_4x4_5.m")
    m13 = Parser("output_MMult_4x4_6.m")
    m14 = Parser("output_MMult_4x4_7.m")
    m15 = Parser("output_MMult_4x4_8.m")
    m16 = Parser("output_MMult_4x4_9.m")

    #print(old)
    #print(new)

    m1_data = np.array(m1.MY_MMult).reshape(-1, 3)
    m2_data = np.array(m2.MY_MMult).reshape(-1, 3)
    m3_data = np.array(m3.MY_MMult).reshape(-1, 3)
    m4_data = np.array(m4.MY_MMult).reshape(-1, 3)
    m5_data = np.array(m5.MY_MMult).reshape(-1, 3)
    m6_data = np.array(m6.MY_MMult).reshape(-1, 3)
    m7_data = np.array(m7.MY_MMult).reshape(-1, 3)
    m8_data = np.array(m8.MY_MMult).reshape(-1, 3)
    m9_data = np.array(m9.MY_MMult).reshape(-1, 3)
    m10_data = np.array(m10.MY_MMult).reshape(-1, 3)
    m11_data = np.array(m11.MY_MMult).reshape(-1, 3)
    m12_data = np.array(m12.MY_MMult).reshape(-1, 3)
    m13_data = np.array(m13.MY_MMult).reshape(-1, 3)
    m14_data = np.array(m14.MY_MMult).reshape(-1, 3)
    m15_data = np.array(m15.MY_MMult).reshape(-1, 3)
    m16_data = np.array(m16.MY_MMult).reshape(-1, 3)

    max_gflops = nflops_per_cycle * nprocessors * GHz_of_processor
    max_gflops = 20 # for better visualization

    fig, ax = plt.subplots()
    num_plots = 16
    colors = np.random.rand(num_plots, 3)  # Generating random RGB values

    ax.plot(m1_data[:,0], m1_data[:,1], linestyle='-.',color=colors[0], label= m1.version)
    ax.plot(m2_data[:,0], m2_data[:,1], linestyle='-.',color=colors[1], label= m2.version)
    ax.plot(m3_data[:,0], m3_data[:,1], linestyle='-.',color=colors[2], label= m3.version)
    ax.plot(m4_data[:,0], m4_data[:,1], linestyle='-.',color=colors[3], label= m4.version)
    ax.plot(m5_data[:,0], m5_data[:,1], linestyle='-.',color=colors[4], label= m5.version)
    ax.plot(m6_data[:,0], m6_data[:,1], linestyle='-.',color=colors[5], label= m6.version)
    ax.plot(m7_data[:,0], m7_data[:,1], linestyle='-.',color=colors[6], label= m7.version)
    ax.plot(m8_data[:,0], m8_data[:,1], linestyle='-.',color=colors[7], label= m8.version)
    ax.plot(m9_data[:,0], m9_data[:,1], linestyle='-.',color=colors[8], label= m9.version)
    ax.plot(m10_data[:,0], m10_data[:,1], linestyle='-.',color=colors[0], label= m10.version)
    ax.plot(m11_data[:,0], m11_data[:,1], linestyle='-.',color=colors[1], label= m11.version)
    ax.plot(m12_data[:,0], m12_data[:,1], linestyle='-.',color=colors[2], label= m12.version)
    ax.plot(m13_data[:,0], m13_data[:,1], linestyle='-.',color=colors[3], label= m13.version)
    ax.plot(m14_data[:,0], m14_data[:,1], linestyle='-.',color=colors[4], label= m14.version)
    ax.plot(m15_data[:,0], m15_data[:,1], linestyle='-.',color=colors[5], label= m15.version)
    ax.plot(m16_data[:,0], m16_data[:,1], linestyle='-.',color=colors[6], label= m16.version)

    ax.set(xlabel='m = n = k', ylabel='GFLOPS/sec.')
    ax.grid()
    ax.legend()

    ax.set_xlim([m1_data[0,0], m1_data[-1,0]])
    ax.set_ylim([0, max_gflops])

    fig.savefig(f"test_all_plot.png")
    # plt.show()
    
plot_all()
print("All plots generated")
plot_init()
print("Init plot generated")
plot_optimize_1_9()
print("Optimize 1-9 plot generated")
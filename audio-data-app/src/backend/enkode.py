#converting text into utf-8 binary format

import scipy
import matplotlib.pyplot as plt 

def take_message():
    txt = input ("Write message")
    x = txt.encode()

    print(x)

take_message()
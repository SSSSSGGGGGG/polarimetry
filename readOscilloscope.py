# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 11:28:11 2024

@author: SG
"""

import struct
import matplotlib.pyplot as plt

# Path to the .scp file
filename = 'qfile_00.scp'
filepath = "C:/Users/Laboratorio/StokeMatix/" + filename

# Function to read and inspect binary .scp file
def inspect_scp_file(file_path):
    try:
        with open(file_path, 'rb') as f:
            # Read the first 16 bytes for inspection
            header = f.read(16)
            print(f"Header bytes: {header}")
            
            # Determine the structure based on inspection
            # For this example, let's assume the header contains:
            # - 4 bytes: sampling rate (float)
            # - 4 bytes: number of samples (unsigned int)
            # - Additional metadata if any
            
            sampling_rate, num_samples = struct.unpack('fI', header[:8])
            print(f"Sampling Rate: {sampling_rate}, Number of Samples: {num_samples}")
            
            # Return remaining file pointer for data reading
            return f, sampling_rate, num_samples
    
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None, None, None
    except struct.error as e:
        print(f"Struct error: {e}")
        return None, None, None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None, None, None

# Function to read the data section of the .scp file
def read_scp_data(file_obj, num_samples):
    try:
        # Read the data: Assuming time and voltage pairs (floats)
        data_size = num_samples * 2 * 4  # 4 bytes per float
        data = file_obj.read(data_size)
        if len(data) < data_size:
            raise ValueError(f"Invalid file data. Expected {data_size} bytes, got {len(data)} bytes.")
        
        # Unpack the data
        data = struct.unpack(f'{num_samples * 2}f', data)
        
        # Separate time and voltage
        time = data[0::2]
        voltage = data[1::2]
        
        return time, voltage
    
    except struct.error as e:
        print(f"Struct error: {e}")
        return None, None
    except Exception as e:
        print(f"Error reading file data: {e}")
        return None, None

# Inspect the header and get file object, sampling rate, and number of samples
file_obj, sampling_rate, num_samples = inspect_scp_file(filepath)

if file_obj:
    # Read the data from the file object
    time, voltage = read_scp_data(file_obj, num_samples)

    if time is not None and voltage is not None:
        # Plot the data
        plt.figure(figsize=(10, 6))
        plt.plot(time, voltage, label='Oscilloscope Data')
        plt.xlabel('Time (s)')
        plt.ylabel('Voltage (V)')
        plt.title('Oscilloscope Waveform')
        plt.legend()
        plt.grid(True)
        plt.show()
    else:
        print("Failed to read data from the file.")
else:
    print("Failed to read the header from the file.")

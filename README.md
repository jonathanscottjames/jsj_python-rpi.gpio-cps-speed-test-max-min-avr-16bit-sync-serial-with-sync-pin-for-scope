new version is much faster graphing rate with smaller back porch(less dead xone time) smaller script and resize extends the trace to the end of the window width even if resized.
and it doesn't loose keyboard connection as much , like never looses kb now. it was hard to kill. but i removed a few statements that were messing with it's overhead data and dogging it... please try it.. > 600k rpi.gpio instrucions per second thanks
up doown kewts to increace or decreace sample time

i discovered that you can run a python script without the terminal window from a bash script .sh file
so i will includ one in this version 7
click the file with the .sh extension and then click the "execuit" button. seems to run a tiny bit faster too.

jsj_rpi.gpio_speed_testV7_0_barometer_command_data_.sh
must be run from the same diurectory as the .py file or it will not start. it is "like" a shortcut to:
jsj_rpi.gpio_speed_testV7_0_barometer_command_data_.py
feel free to edit your copy  or examine it to try to understand the suyntaxt of it's commands and structure 
don't forget to leave comments. feedback is always inspirational
thanks

version 6.4 is :

jsj_rpi.gpio_speed_testV6_4gui12k_bit_input_block_display_10th_sec.py
it is a single file that only requiered rpi.gpio    :

sudo apt-get install python-rpi.gpio python3-rpi.gpio

sudo apt-get upgrade
sudo apt-get update


it has a pygame gui and user adjustable threw the up and down arrow keys plus gpio2 input diplay as well as clock out on gpio3 and a scope can use gpio4 as a sweep trigger
previous versions are obscelete  . thanks
# jsj_python-rpi.gpio-cps-speed-test-max-min-avr-16bit-sync-serial-with-sync-pin-for-scope
python terminal text output counts how many times it can turn gpio3 on and off 16times in 1 second also send a sync pulse on gpio4 every 16 cycles so you can watc on you scope. and it tabulates max, min, and average number of 16 clock cycle bursts.. send text output to python terminal.. my pi with beer can coat hanger heat sync indicated about 15000 16 bit serial transfers will be possible when i connect the synchronous serial gyro and barometer gps and thermometer parietal boards to the pi and network it threw the long range wifi connected to it's usb ctrl "c" to exit

Raspberry Mail IP On Boot
=========

Description
----------

Send an email according from/to configuration with the public and private IP.

Configuration
-------------

# Make it executable

````
sudo chmod +x ip_on_boot.py
````

# Debian

````
sudo nano /boot/boot.rc
````

You must modify the following piece of code according your script location.

````
python /home/pi/ip_on_boot.py
````

# Raspbian

````
sudo nano /etc/rc.local
````

You must modify the following piece of code according your script location.

````
 # rc.local
 #
 # This script is executed at the end of each multiuser runlevel.
 # Make sure that the script will "exit 0" on success or any other
 # value on error.
 #
 # In order to enable or disable this script just change the execution
 # bits.
 #
 # By default this script does nothing.
 # Print the IP address if it doesn't work ad sleep 30 before all your code
 _IP=$(hostname -I) || true
 if [ "$_IP" ]; then
   printf "My IP address is %s\n" "$_IP"
   python /home/pi/ip_on_boot.py
 fi
 exit 0
````

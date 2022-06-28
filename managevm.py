
import subprocess
from subprocess import Popen, PIPE
from venv import create

##
#
# Author: Kevin Underwood
# Last revision: 6/27/2022
# revision history:
# 6/24/2022
# 6/21/2022
# 6/18/2022
# 6/10/2022
# version 0.5
#
# ##



#def getuuid(VMNAME):


def CreateVm(VMNAME):
    #this function creates a Virtual machine based off of the string VMNAME selected by the user.
    #TODO: 
    # -accept more vm choices.
    # -find a better way to handle vm configurations
    # -append all output to a single file/string to be returned as output for the user.

    #Create and register the virtual machine
    subprocess.run(['VBoxManage','createvm', '--name', VMNAME ,'--register'],capture_output=True)
    #Set up the basic configuration.
    subprocess.run(['VBoxManage','modifyvm', VMNAME ,'--memory','2048','--acpi', 'on','--boot1','dvd','--cpus','2'],capture_output=True)
    
    #Set up a storage controllers
    subprocess.run(['VBoxManage','storagectl', VMNAME ,'--name','IDE','--add','ide'],capture_output=True)
    subprocess.run(['VBoxManage','storagectl', VMNAME ,'--add','sata','--controller','IntelAHCI','--name','SATA Controller'],capture_output=True)

    #Create a hardrive
    #more thought and research is needed to see if there is a better more modular way to do this.
    subprocess.run(['VBoxManage','createhd','--filename','\\vmhd\\'+ VMNAME +'.vdi','--size','20240'],capture_output=True)
    subprocess.run(['VBoxManage','storageattach',VMNAME,'--storagectl','SATA Controller','--port','0','--device','0','--type','hdd','--medium','\\vmhd\\'+ VMNAME +'.vdi'],capture_output=True)
    
    #Attach the ISO to the virtual machine
    #TODO: add more vm support. multiple types of vm and configurations.
    #Potential rework is needed to allow for a more modular aproach. 
    if(VMNAME == "Ubuntu"):
        subprocess.run(['VBoxManage','storageattach',VMNAME,'--storagectl','IDE','--port','0','--device','0','--type','dvddrive','--medium','iso\\ubuntu-22.04-desktop-amd64.iso'],capture_output=True)
    elif(VMNAME == "Kali"):
        subprocess.run(['VBoxManage','storageattach',VMNAME,'--storagectl','IDE','--port','0','--device','0','--type','dvddrive','--medium','iso\\kali-linux-2022.2-installer-amd64.iso'],capture_output=True)
    elif(VMNAME == "Windows"):
        subprocess.run(['VBoxManage','modifyvm', VMNAME ,'--ostype', 'Windows10_64'],capture_output=True)
        subprocess.run(['VBoxManage','storageattach',VMNAME,'--storagectl','IDE','--port','0','--device','0','--type','dvddrive','--medium','iso\\Windows.iso'],capture_output=True)
        subprocess.run(['VBoxManage','unattended','install', VMNAME,'--iso=iso\\Windows.iso','--user=user','--password=password','--key=XGVPP-NMH47-7TTHJ-W3FW7-8HV2C'],capture_output=True)
    else:
        print("Invalid choice you should not see this.")
        DeleteVm(VMNAME)


def ListVm():
    #executes powershell script to list all vms on the system. Ideally this function is 
    #called everytime a change is made to the environment. 
    #TODO: add varying functionality to filter based off of scenario 
    #and or vm/s are active and running. 
    return subprocess.run('vboxmanage list vms',capture_output=True)
    
def ShowVmInfo(VMNAME):
    #shows a specific virtual machines current configuration information.
    subprocess.run('vboxmanage showvminfo '+VMNAME, capture_output=True)

def DeleteVm(VMNAME):

    subprocess.run(['VBoxManage','closemedium','disk', '\\vmhd\\'+VMNAME+'.vdi', '--delete'],capture_output=True)

    result=subprocess.run(['VBoxManage','unregistervm', VMNAME ,'--delete'],capture_output=True)

    if(result.returncode == 0):
        print (result.args[2],": Deletion successfull",capture_output=True)

def ModifyVm(VMNAME, OSTYPE):

    #TODO: COMPLETELY TEAR THIS OUT AND REDO. need to have a more modular aproach. 
    # potential solution: include resouce information in the scenario configuration file.
    subprocess.run(['VBoxManage','modifyvm', VMNAME ,'--ostype', OSTYPE],capture_output=True)
    subprocess.run(['VBoxManage','modifyvm', VMNAME ,'--memory','1024','--vram','16'],capture_output=True)
    subprocess.run(['VBoxManage','modifyvm', VMNAME ,'--cpus','2'],capture_output=True)


def StartVm(VMNAME):
    subprocess.run(['VBoxManage','startvm', VMNAME ,'--type','headless'],capture_output=True)

def CloseVm(VMNAME):
    #Powers down the vm. Equivelent to pulling the plug.
    subprocess.run(['VBoxManage','controlvm', VMNAME ,'poweroff'],capture_output=True)

def ImportVm(VMNAME):
    print('todo: import ova file based off file provided by the user.',capture_output=True)

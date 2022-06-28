
from managevm import *

##
# DEPRICATED: just a test menu to get my toes wet.
# Author: Kevin Underwood
# Last revision: 6/21/2022
# version 0.1
# About:
# Basic test menu. goal is to replace with
# a general purpose gui down the road.
# ##




def main():
    choice=0
    while(choice != 8):
        print('             Choose your option')
        print('=================================================')
        print('1. Create virtual machines')
        print('2. Modify virtual machines')
        print('3. List virtual machines')
        print('4. Show a specific vm\'s information')
        print('5. Start a virtual machine')
        print('6. Delete virtual machines')
        print('7. Shutdown virtual machine')
        print('8. Exit')
        print('=================================================')
        choice = int(input('->'))
        if (choice == 0):
            print ('welcome please make a choice')
        elif (choice == 1):
            CreateVm('Ubuntu')
            CreateVm('Kali')
            CreateVm('Windows')
            #CreateVm('test')
        elif (choice == 2):
            #ModifyVm('test','Linux_64')
            print('no functionality for this test.')
        elif (choice == 3):
            ListVm()

        elif (choice == 4):
            ShowVmInfo('Ubuntu')
            ShowVmInfo('Kali')
            ShowVmInfo('Windows')

        elif (choice == 5):
            StartVm('Ubuntu')
            StartVm('Kali')
            StartVm('Windows')

        elif (choice == 6):
            DeleteVm('Ubuntu')
            DeleteVm('Kali')
            DeleteVm('Windows')

        elif (choice == 7):
            CloseVm('Ubuntu')
            CloseVm('Kali')
            CloseVm('Windows')

        elif (choice == 8):
            print('goodbye.')
        else:
            print('Invalid option.')
        



main()
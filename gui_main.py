
from tkinter import * 
from tkinter.scrolledtext import ScrolledText
import managevm as mvm


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        master.title("Airve")

        self.master = master
        self.pack()
        self.create_widgets()

        #Scrolled text window for output.
        st = ScrolledText(self, width=100, height=100)
        st.insert(END, mvm.ListVm())
        st.pack(fill=BOTH, side=LEFT, expand=True)

    def create_widgets(self):
        vmList = ["Kali","Ubuntu","Windows"]
        #Currently supported OS options 
        #TODO: more options and better configurations... database instead of list maybe?
        
        option = StringVar(self.master)
        option.set(vmList[0]) # Set the first value to be the default option


        #Dropdown menu for scenario/OS selection
        #TODO: implement scenario parsing. goal is to have a function that reads
        #in a file with the lab specs built in then use the local functions to build the vm
        dropdown = OptionMenu(self,option,*vmList, command=mvm.ListVm().stdout)
        dropdown.pack(side="right")

        #Create button
        #TODO: potential rework for scenarios might be nessisary.
        self.Create_button = Button(self, text="Create VM", command=lambda:mvm.CreateVm(option.get()))
        self.Create_button.pack(side="right",)

        #List button
        #Note: not sure this will be needed down the road. 
        #Plan is to make the log window show this information when changes 
        #are made to the environment
        self.list_button = Button(self,text="List VMs", command=lambda:mvm.ListVm())
        self.list_button.pack(side="right")

        #Show specified vm information.
        #Note: this needs an overhaul as it is right now it doesnt provide 
        #much useful information to the reader 
        self.show_button = Button(self, text="Show VM info", command=lambda:mvm.ShowVmInfo(option.get()))
        self.show_button.pack(side="right")
        
        #Delete specified virtual machine
        #TODO: refactor for teardown of the scenario not just a singluar vm.
        self.delete_button = Button(self,text="Delete VM" ,command=lambda:mvm.DeleteVm(option.get()))
        self.delete_button.pack(side="right")

        #quit
        self.quit = Button(self, text="QUIT", fg="red",command=self.master.destroy)
        self.quit.pack(side="right")

root = Tk()

app = Application(master=root)

app.mainloop()
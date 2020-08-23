import wx
import os

class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title=os.getcwd())
        panel = wx.Panel(self)

        self.newDirButton = wx.Button(panel, label = "Add New Folder" , pos=(5,35)).Bind(wx.EVT_BUTTON, self.OnClicked)

        arrayOfDirs = find_current_dir()
        position=0
        for file in arrayOfDirs:
            print(file)
            dyanmic_button = wx.Button(panel, label = file , pos=(5+(position*100),55)).Bind(wx.EVT_BUTTON, self.OnClicked)
            position+=1
            print(position)
        self.Show()
    
    def OnClicked(self, event):
        btn = event.GetEventObject().GetLabel() 
        print ("Label of pressed button = ", btn)
        # add functions for assocaited use cases below. 
        if btn == "Add New Folder":
            print("ah")
            add_new_dir("/trying")
        else:
            print("oh")
        

# This is to check for if directories are present in the current directory and add them to a array.
def find_current_dir():
    folders = next(os.walk('.'))[1]
    print(folders)
    return folders

def add_new_dir(newFolder):
    path = os.getcwd() + newFolder
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
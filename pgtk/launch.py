#!/usr/bin/env python
import pygtk
pygtk.require('2.0')
import gtk
import time

class QRPrint:

    def callback(self, widget, data):
        tid = time.strftime("%y%m%d%H%S")
        print data + tid
        #TODO ADD PRINT CODE HERE!!!

    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def __init__(self):
        #Saetter vaerdier og opsaetter vindue
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Print QR Code")
        self.window.connect("delete_event", self.delete_event)
        self.window.set_border_width(100)
        #self.window.set_border_height(100)
        self.box1 = gtk.HBox(False, 0)
        self.window.add(self.box1)
        
        #Tilfojer knapper og binder dem til callback()
        self.Hvidovre = gtk.Button("Hvidovre")
        self.Hvidovre.connect("clicked", self.callback, "1")
        self.box1.pack_start(self.Hvidovre, True, True, 0)
        self.Hvidovre.show()

        self.Ballerup = gtk.Button("Ballerup")
        self.Ballerup.connect("clicked", self.callback, "2")
        self.box1.pack_start(self.Ballerup, True, True, 0)
        self.Ballerup.show()

        self.Fredriksberg = gtk.Button("Fredriksberg")
        self.Fredriksberg.connect("clicked", self.callback, "3")
        self.box1.pack_start(self.Fredriksberg, True, True, 0)
        self.Fredriksberg.show()

        self.Lyngby = gtk.Button("Lyngby")
        self.Lyngby.connect("clicked", self.callback, "4")
        self.box1.pack_start(self.Lyngby, True, True, 0)
        self.Lyngby.show()
        self.box1.show()
        self.window.show()

#Korer programmet
def main():
    gtk.main()

if __name__ == "__main__":
    hello = QRPrint()
    main()

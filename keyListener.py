#
# After a post to c.l.py by Richie Hindle:
# http://groups.google.com/groups?th=80e876b88fabf6c9
#
import os
import sys
import ctypes
from ctypes import wintypes
import win32con

class HotKeyListener:
    def __init__(self):
      self.HOTKEYS = {
          1 : (win32con.VK_F3, win32con.MOD_WIN)
      }
      self.HOTKEY_ACTIONS = {}

      self.user32 = ctypes.windll.user32
      self.byref = ctypes.byref

    def registerCallback(self, id, callback):
        self.HOTKEY_ACTIONS[id] = callback

    def finalizeCallbackRegistrations(self):
        for id, (vk, modifiers) in self.HOTKEYS.items ():
            print "Registering id", id, "for key", vk
            if not self.user32.RegisterHotKey (None, id, modifiers, vk):
                print "Unable to register id", id

    def checkForHotKey(self):
        msg = wintypes.MSG()
        response = self.user32.GetMessageA(self.byref(msg), None, 0, 0)
        if response != 0:
            if msg.message == win32con.WM_HOTKEY:
                action_to_take = self.HOTKEY_ACTIONS.get(msg.wParam)
                if action_to_take:
                    action_to_take()
        self.user32.TranslateMessage(self.byref(msg))
        self.user32.DispatchMessageA(self.byref(msg))

    def cleanUp(self):
        for id in self.HOTKEYS.keys ():
            self.user32.UnregisterHotKey (None, id)      

#
# RegisterHotKey takes:
#  Window handle for WM_HOTKEY messages (None = this thread)
#  arbitrary id unique within the thread
#  modifiers (MOD_SHIFT, MOD_ALT, MOD_CONTROL, MOD_WIN)
#  VK code (either ord ('x') or one of win32con.VK_*)
#


#
# Home-grown Windows message loop: does
#  just enough to handle the WM_HOTKEY
#  messages and pass everything else along.
#
# try:
#   msg = wintypes.MSG ()
#   while user32.GetMessageA (byref (msg), None, 0, 0) != 0:
#     if msg.message == win32con.WM_HOTKEY:
#       action_to_take = HOTKEY_ACTIONS.get (msg.wParam)
#       if action_to_take:
#         action_to_take ()

#     user32.TranslateMessage (byref (msg))
#     user32.DispatchMessageA (byref (msg))
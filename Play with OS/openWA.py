import subprocess as sp
scr = {
    "whatsapp" : "C:\Users\ADMIN\AppData\Local\WhatsApp\WhatsApp.exe",
    "chrome" : "C:\Program Files\Google\Chrome\Application\chrome.exe",
}
def openApp(app):
    sp.Popen(scr[app])
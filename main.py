import webview
import customtkinter
def open_site():
    webview.create_window('Robot Emil', 'https://app.robotemil.com')
    webview.start()
root = customtkinter.CTk()
btn = customtkinter.CTkButton(root, text="Open Robot Emil", command=open_site)
btn.pack()
root.mainloop()

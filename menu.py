import os
import pyttsx3 

print()
print("\t\t\t\t  Welcome to the Service Menu Bot \t\t\t")
print("\t\t\t\t  -------------------------------")
pyttsx3.speak("\n\n\n\n\n\n  Welcome to the Service Menu Bot \n\n\n")

    
while(True):
    print()
   
    print("Type Service Name You want to run e.g for Chrome Type Chrome \t\t" ,end='')
    pyttsx3.speak("Type Service Name You want to run ")
    a=input()
    p = a.lower()
    print()
    print("-----------------------------------------------------------")
    print()
        
    if ("chrome" in p):
        os.system("chrome")
       
        
    elif  ("firefox" in p):
        os.system("firefox")
        
    elif ("player" in p):
        os.system("wmplayer")
    elif ("vscode" in p):
        os.system("code")
        
    elif ("facebook" in p):
        os.system("chrome www.facebook.com")
        
    elif  ("twitter" in p):
        os.system("chrome www.twitter.com")
        
    elif ("gmail" in p):
        os.system("chrome www.gmail.com")
    elif ("vlc" in p  or "vlc player" in p):
        os.system("vlc")
    elif ("notepad" in p):
        os.system("notepad++")
    elif ("excel" in p):
        os.system("excel")
    elif ("word" in p):
        os.system("winword")
    elif ("powerpoint" in p):
        os.system("powerpnt")
     
     
    elif ("quit" in p) or ("exit" in p):
        print("\t\t\t Have A Good Day !!! Hope you Like Our Services, See You Again  ('~')!!!")
        pyttsx3.speak("Have A Good Day !!! Hope you Like Our Services , See You Again !!!")
        break
           
    else:
        print("wrong entry")
        pyttsx3.speak("Wrong Entry")
    
        
    

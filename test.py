from selenium import webdriver
import geckodriver_autoinstaller

def delfile(fileInput):
    open(fileInput,"w").close()

def getFileName():
    filenameError = True
    createdFile = ""
    while (filenameError == True):
        createdFile = input("Enter name of file to create, (Finish with a .txt extention)\n-->")
        if (len(createdFile) <= 4):
            print("Error in filename - name cannot be empty and must end in .txt")
        elif (createdFile[-4:] != ".txt"):
            print("Error in filename - name must end in .txt")
        else:
            filenameError = False

    return createdFile

def main():
    rerun = ""
    geckodriver_autoinstaller.install() # Check if the current version of geckodriver exists
                                        # and if it doesn't exist, download it automatically,
                                        # then add geckodriver to path
    while (rerun.lower() == "y" or rerun == ""):


        driver = webdriver.Firefox() # Opens Firefox instance
        targetWebsite = input("Enter website to scrape\nNOTE: Enter full URL inclusing https:\\\\\n-->")
        driver.get(targetWebsite) # Sends website to Firefox, opens it
        books = driver.find_elements("tag name","body")
        textlist = ""
        for i in range(0,len(books)):
            textlist += books[i].text

        createdFile = getFileName() ##WFH
                
        try: 
            file = open(createdFile,"x")
            print("Text file created successfully")
        except:
            print("Text file already exists, opening...")
            file = open(createdFile,"a")
        file.write(textlist + "\n")
        file.close()
        rerun = ""
        while (rerun.lower() != "y" and rerun.lower() != "n"):
            rerun = input("Run program again? [y/n] ")
        
        delete = input("Wipe created file? [y/n] ") #XX3
        if (delete == "y"):
            delfile(createdFile)

        print("Closing Firefox instance...")
        driver.quit() # Closes firefox instance

    print("\n#############SUCCESSFUL EXIT##################\n")


if(__name__ == "__main__"):
    main()
else:
    main()
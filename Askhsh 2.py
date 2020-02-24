Flag=False
File_Name = input("Give the name of the file:")
File = open(File_Name, "r")
Text=File.read()+" "
Good_Word=0
Bad_Word=0
All_Letters=("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
Bad_Consonant=("FCKRfckr")
Good_Consonant=("bdghjlmnpqstvwxyzBDGHJLMNPQSTVWXYZ")
for char in Text:
    if (not(char in All_Letters)):
        if(Flag==True):
            if(Bad_Word<Good_Word):
                print(":good word")
            else:
                print(":bad word")
            Flag=False
            Good_Word=0
            Bad_Word=0
    else:
        print(char,end="")
        Flag=True
        if(char in Good_Consonant):
            Good_Word+=1
        if(char in Bad_Consonant):
            Bad_Word+=1
File.close()

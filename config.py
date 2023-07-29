while True:
    try :
        database = input("databazani nomini kiriting: ")
        user = input("Userni kiriting: ")
        host = input('serverni kiriting (localhos): ')
        password = input("Passwordni kiriting: ")
        break
    except:
        print("Notog'ri kalit kiritingiz qayta urinib koring !")
        continue
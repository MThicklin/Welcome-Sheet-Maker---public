import settings

def GenerateTXT():
    print(settings.companyName)
    print("New User Welcome Sheet")
    print("{}, {}".format(settings.lName, settings.fName))
    print("Username: {}".format(settings.uName))
    print("Password: Pa55word")
    print("Of the 4 Upper/Lower/Numeric/Special Character groups, you'll need 3 for your password.")
    print("Please note: Passwords expire every 90 days.")
    print("Webmail: {}".format(settings.owaLink))
    print("Email Address: {}".format(settings.uEmail))
    print("Email info for mobile devices:")
    print("Account type: Exchange")
    print("Server name: {}".format(settings.link))
    print("The connection will be secured using SSL.")
    print("Webmail Username- CE\{}".format(settings.uName))
    print("Webmail Password- Pa55word")
    print("See Below for iPhone Instructions...")
    
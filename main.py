from pdfs import welcomePDF
from passwordGen import generatePass
import argparse

default_password = "Pa55word"

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--name', action="extend", nargs="+", type=str, help ="Name of user.  Needs at least a first and last name. Middle names can be added.")
parser.add_argument('-nn', '--uNameNum', default="01", type=str, help="Number added to the end of username.  Default: 01")
parser.add_argument('-o', '--o365', default="none", type=str, help="Adds a Office 365 password section to the welcome sheet.  'gen' generates a basic paassword.  'pass' copies the login password. Not required, removes the password section if not used.")
parser.add_argument('-p','--passw', default=default_password, type=str, help="Log in password for user. Use 'gen'to generate a password. Use '-p <your password>' to add custom password")
parser.add_argument('--phone', default=False, action='store_true', help="This section has been kept in as an example of how to expand this script with optional documents.  It is not required.")

args = parser.parse_args()


class person:
    def __init__(self, args):
        if (len(args.name) > 2):
            trueName = ""
            for name in range(len(args.name[0:-1])):
                trueName += " " + args.name[name].capitalize()
            self.fName = trueName
        else:
            self.fName = args.name[0].capitalize()
        self.lName = args.name[-1].capitalize()
        self.uNameNum = args.uNameNum
        self.uName = "Username: {}".format(self.lName +
                                           str(self.fName) +
                                           self.uNameNum)
        self.dName = self.lName + ", " + self.fName
        self.companyName = "Your Company Name here"
        self.subTitle = "New User Welcome Sheet"
        self.companyDomain = "{}.com".format(self.companyName.replace(" ", ""))
        self.uEmail = self.fName + self.lName[
            0] + "@" + self.companyDomain.lower()
        self.webLink = "https://webmail." + self.companyDomain.lower()
        self.owaLink = self.webLink + "/owa"
        self.domainName = "ce"
        self.office365P = "Office 365 Password: {}".format(args.o365)
        self.itEmail = "helpdesk@" + self.companyDomain.lower()
        self.itNumber = "IT phone number here"
        self.supportInfo = "Please contact IT at by phone " + self.itNumber + " or Email " + self.itEmail
        self.passExpire = "90"
        self.passwordLength = "7"
        if (args.passw == "gen"):
            self.passw = "Password: " + generatePass()
        else:
            self.passw = "Password: " + str(args.passw)

        if (args.o365 == "none"):
            self.office365P = ""
        if (args.o365 == "gen"):
            self.office365P = "Office 365 Password: " + generatePass()
        if (args.o365 == "pass"):
            self.office365P = "Office 365 Password: {}".format(
                self.passw[10::])

        self.displayEmail = "Email Address: {}".format(self.uEmail)
        self.webmailU = "Webmail Username - {}//{}".format(
            self.domainName, self.uName)
        self.webmailP = "Webmail Password - {}".format(self.passw)
        self.phone = args.phone
        #self.email = args.email


newUser = person(args)
welcomePDF(newUser)

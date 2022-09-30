import sys
from passwordGen import generatePass

companyName = "Company Name"
subtitle = "New User Welcome Sheet"

companyDomain = "{}.com".format(companyName.replace(" ",""))
domainName = companyName
fName = sys.argv[1].capitalize()
lName = sys.argv[2].capitalize()
dName = lName+", "+fName
uNameNum = '01'
uName = lName[0:4]+fName[0:2] + uNameNum
passExpire = 90
#password = "Default123!"
#Uncomment following line if you want to add the password as a third argument
#password = sys.argv[3]
#Uncomment following line, and Line 2, to turn on simple password generator.
password = generatePass()

itEmail = "ITeMailHere@"+companyDomain.lower()
itNumber = "IT Phone number here"

uEmail = fName+lName[0]+"@"+companyDomain.lower()
link = "mail."+companyDomain.lower()
owaLink = link + "/owa"

displayName = "{}".format(dName)

passwordLength = 7

passwordNeeds = "Ensure your new password has a combination of 1 Upper, 1 Lower, 1 Numeric, and 1 Special character(s).  It will need three of the four."

passwordExpires = "Please note: Passwords expire every {} days.".format(passExpire)

passwordRequirements = "\tYou will be prompted to change your password the first time you log in. You will need to use {} characters and ".format(passwordLength) + passwordNeeds + passwordExpires



displayEmail = "Email Address: {}".format(uEmail)
webmailU = "Webmail Username - {}//{}".format(domainName, uName)
webmailP = "Webmail Password - {}".format(password)

mobileEmailTitle = "Email info for mobile devices:"
account = "Account type: Exchange"
server = "Server name: https://{}".format(link)
connectionSecurity = "The connection will be secured using SSL."

supportInfo = "If any issues occur or you have any questions, please contact IT at " + itNumber +" or Email "+ itEmail

phoneStep0 = "Setting up email on your iPhone: "
phoneStep1 = "Under 'Settings' Go to 'Passwords and Accounts' and select Exchange."
phoneStep2 = "Enter {} and {} for Description".format(uEmail, domainName)
phoneStep3 = "Select 'Configure Manually'."
phoneStep4 = "Enter {} and {}, then press select.".format(uEmail, password)
phoneStep5 = "Enter the following information: "
phoneStep51 = "Email: {}".format(uEmail)
phoneStep52 = "Server: {}".format(link)
phoneStep53 = "domain: {}".format(domainName)
phoneStep54 = "username: {}".format(uName)
phoneStep55 = "password: {}".format(password)
phoneStep6 = "Finally, select save."
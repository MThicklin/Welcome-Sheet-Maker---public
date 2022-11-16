from fpdf import FPDF


def welcomePDF(newUser):
    class MyPDF(FPDF):
        def header(self):
            self.set_font('Arial', 'B', 18)
            self.cell(200, 10, newUser.companyName, ln=1, align='C')
            self.set_font('Arial', 'B', 16)
            self.cell(200, 10, newUser.subTitle, align='C')
            self.ln(15)

        def footer(self):
            self.set_y(-15)
            self.set_font("Arial", style="B", size=12)
            self.cell(0, 10,"If any issues occur or you have any questions", align="C")
            self.set_y(-10)
            self.cell(0, 10, newUser.supportInfo, ln=20, align="C")

    pdf = MyPDF()
    pdf.add_page()

    pdf.set_font("Arial", 'b', size=18)
    pdf.cell(200, 5, txt=newUser.dName)

    pdf.ln(10)

    pdf.set_font("Arial", 'b', size=12)
    pdf.cell(200, 5, txt="PC Login", ln=1)
    pdf.cell(200, 5, txt=newUser.uName, ln=1)
    pdf.cell(200, 5, txt=newUser.passw, ln=1)
    pdf.cell(200, 5, txt=newUser.office365P, ln=1)

    pdf.ln(5)

    pdf.set_font("Arial", size=12)
    pdf.write(5, txt="\tAt your earliest convenience, use Ctrl+Alt+Del to change your password. You will need to use {} characters and ".format(newUser.passwordLength) + "a combination of 1 Upper, 1 Lower, 1 Numeric, and 1 Special character(s).  It will need three of the four. Please note: Passwords expire every {} days.".format(newUser.passExpire))

    pdf.cell(200, 10, txt=" ", ln=1, align='C')

    pdf.set_font("Arial", 'b', size=12)
    pdf.cell(200, 5, txt="Email Address: ")
    pdf.set_font("Arial", size=12)
    pdf.write(5, newUser.uEmail)

    pdf.cell(200, 10, txt=" ", ln=1, align='C')

    
    pdf.write(5, "Webmail: ")
    pdf.set_text_color(0, 0, 255)
    pdf.set_font('', 'U')
    pdf.cell(200, 5, newUser.owaLink, link=str(newUser.owaLink), ln=1)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", size=12)
    pdf.write(5, txt="Webmail Username: ")
    pdf.cell(200, 5, txt=newUser.domainName + "/" + newUser.uName[10::], ln=1)
    pdf.write(5, txt="Webmail Password: ")
    pdf.cell(200, 5, txt=newUser.passw[10::], ln=1)

    pdf.cell(200, 5, txt=" ", ln=1, align='C')
    pdf.set_font("Arial", 'b', size=12)
    pdf.cell(200, 5, txt="Email info for mobile devices:", ln=1)

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 5, txt="\tAccount type: Exchange", ln=1)
    pdf.cell(200,
             5,
             txt="\tServer name: {}".format(
            newUser.webLink),
             ln=1,
             link=newUser.owaLink)

    pdf.cell(200, 5, txt="\tThe connection will be secured using SSL.", ln=1)
    pdf.cell(200, 5, txt="\tDomain: {}".format(newUser.domainName), ln=1)
    pdf.cell(200, 5, txt="\t" + newUser.uName, ln=1)
    pdf.cell(200, 5, txt="\t" + newUser.passw, ln=1)

    if (newUser.phone == True):
        Phone(pdf, newUser)
    else:
        pdf.output("{}.pdf".format(newUser.dName))


def Phone(pdf, newUser):
    pdf.add_page()

    pdf.set_font("Arial", 'b', size=12)
    pdf.cell(200, 10, txt="Setting up email on your iPhone: ", ln=1)
    pdf.ln(10)

    pdf.cell(200, 5, txt="This section is set up as an example to show how you can add extra documents to the welcome sheet.", ln=1)
    pdf.image("img/phone/image1.jpg", x=None, y=None, w=90, h=90, type="jpg")
    
    pdf.ln(15)
    
    pdf.cell(200, 5, txt="You can also add extra lines and call the variables as normal.  Enter {} and {} for Description".format(
            newUser.uEmail, newUser.domainName), ln=1)
    pdf.image("img/phone/image2.jpg", x=None, y=None, w=100, h=100, type="jpg")

    pdf.output("{}.pdf".format(newUser.dName))

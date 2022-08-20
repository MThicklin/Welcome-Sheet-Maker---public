import settings
from fpdf import FPDF


def GeneratePDF():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'b', size=20)
    pdf.cell(200,
             5,
             txt=settings.companyName + " New User Welcome Sheet",
             ln=1,
             align='C')

    pdf.cell(200, 5, txt=" ", ln=1, align='C')

    pdf.set_font("Arial", 'b', size=18)
    pdf.cell(200, 8, txt="{}, {}".format(settings.lName, settings.fName), ln=1)

    pdf.cell(200, 5, txt=" ", ln=1, align='C')

    pdf.set_font("Arial", 'b', size=12)
    pdf.cell(200, 5, txt="PC Login", ln=1)
    pdf.cell(200, 5, txt="Username: {}".format(settings.uName), ln=1)
    pdf.cell(200, 5, txt="Password: {}".format(settings.password), ln=1)

    pdf.cell(200, 5, txt=" ", ln=1, align='C')

    pdf.set_font("Arial", size=12)
    pdf.write(5, txt=str(settings.passwordRequirements))

    pdf.cell(200, 5, txt=" ", ln=1, align='C')

    pdf.set_font("Arial", 'b', size=12)
    pdf.write(5, txt="Email Address: ")
    pdf.set_font("Arial", size=12)
    pdf.write(5, "{}".format(settings.uEmail))

    pdf.cell(200, 10, txt=" ", ln=1, align='C')

    pdf.set_font("Arial", 'b', size=12)
    pdf.cell(200, 5, txt="MS365 Login:", ln=1) 
    pdf.cell(200, 5, txt="(if Prompted in Office)", ln=1)
    
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 5, txt="Username: {}".format(settings.uName), ln=1)
    pdf.cell(200, 5, txt="Password: {}".format(settings.password), ln=1)
    
    pdf.cell(200, 5, txt=" ", ln=1, align='C')

    pdf.set_font("Arial", 'b', size=12)
    pdf.write(5, "Webmail: ")
    pdf.set_text_color(0, 0, 255)
    pdf.set_font('', 'U')
    pdf.write(5, "{}".format(settings.owaLink), link=str(settings.owaLink))

    pdf.cell(200, 5, txt=" ", ln=1, align='C')
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", 'b', size=12)

    pdf.cell(200, 5, txt=" ", ln=1, align='C')
    pdf.cell(200, 5, txt="Email info for mobile devices:", ln=1)

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 5, txt="Account type: Exchange", ln=1)
    pdf.cell(200,
             5,
             txt="Server name: {}".format(settings.link),
             ln=1,
             link='{}'.format(settings.owaLink))

    pdf.cell(200, 5, txt="The connection will be secured using SSL.", ln=1)
    pdf.cell(200,
             5,
             txt="Webmail Username- CE\{}".format(settings.uName),
             ln=1)
    pdf.cell(200,
             5,
             txt="Webmail Password- {}".format(settings.password),
             ln=1)

    pdf.cell(200, 5, txt=" ", ln=1, align='C')

    pdf.cell(
        200,
        5,
        "If you have any issues or question, please feel free to contact {} IT"
        .format(settings.companyName),
        ln=1)
    pdf.cell(200,
             5,
             "by phone: {} or email: {}".format(settings.itNumber,
                                                settings.itEmail),
             ln=1)

    pdf.cell(200, 5, txt=" ", ln=1, align='C')

    pdf.set_font("Arial", 'b', size=12)
    pdf.cell(200, 5, txt=str(settings.phoneStep0), ln=1)

    pdf.cell(200, 5, txt=" ", ln=1, align='C')

    pdf.cell(200, 5, txt=str(settings.phoneStep1), ln=1)
    pdf.image("img/image1.jpg", x=None, y=None, w=90, h=90, type="jpg")
    pdf.cell(200, 5, txt="", ln=1)

    pdf.cell(200, 5, txt=str(settings.phoneStep2), ln=1)
    pdf.image("img/image2.jpg", x=None, y=None, w=100, h=100, type="jpg")
    pdf.cell(200, 5, txt=" ", ln=1, align='C')

    pdf.cell(200, 10, txt=str(settings.phoneStep3), ln=1)
    pdf.image("img/image3.png", x=None, y=None, w=100, h=100, type="png")

    pdf.cell(200, 45, txt="", ln=1)

    pdf.cell(200, 5, txt=str(settings.phoneStep4), ln=1)
    pdf.image("img/image4.jpg", x=None, y=None, w=100, h=100, type="jpg")
    pdf.cell(200, 10, txt=" ", ln=1, align='C')

    pdf.cell(200, 5, txt=str(settings.phoneStep5), ln=1)
    pdf.cell(200, 5, txt=str(settings.phoneStep51), ln=1)
    pdf.cell(200, 5, txt=str(settings.phoneStep52), ln=1)
    pdf.cell(200, 5, txt=str(settings.phoneStep53), ln=1)
    pdf.cell(200, 5, txt=str(settings.phoneStep54), ln=1)
    pdf.cell(200, 5, txt=str(settings.phoneStep55), ln=1)
    pdf.image("img/image5.jpg", x=None, y=None, w=100, h=100, type="jpg")

    pdf.write(5, str(settings.phoneStep6))

    pdf.output("{}, {}.pdf".format(settings.lName,
                                   settings.fName.capitalize()))

GeneratePDF()
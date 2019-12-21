import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "embeded.project.zewail@gmail.com"
receiver_email = "s-omarkhaled@zewailcity.edu.eg"
password = "adminsherif"

message = MIMEMultipart("alternative")
message["Subject"] = "Project2"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""
html = """\
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>

<head>
    <meta charset="UTF-8">
    <meta content="width=device-width, initial-scale=1" name="viewport">
    <meta name="x-apple-disable-message-reformatting">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta content="telephone=no" name="format-detection">
    <title></title>
    <!--[if (mso 16)]>
    <style type="text/css">
    a {text-decoration: none;}
    </style>
    <![endif]-->
    <!--[if gte mso 9]><style>sup { font-size: 100% !important; }</style><![endif]-->
    <!--[if !mso]><!-- -->
    <link href="https://fonts.googleapis.com/css?family=Roboto:400,400i,700,700i" rel="stylesheet">
    <!--<![endif]-->
</head>

<body>
    <div class="es-wrapper-color">
        <!--[if gte mso 9]>
			<v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t">
				<v:fill type="tile" color="#f6f6f6"></v:fill>
			</v:background>
		<![endif]-->
        <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0">
            <tbody>
                <tr>
                    <td class="esd-email-paddings st-br" valign="top">
                        <table cellpadding="0" cellspacing="0" class="es-header esd-header-popover" align="center">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe esd-checked" align="center" style="background-image:url(https://hpy.stripocdn.email/content/guids/CABINET_d21e6d1c5a6807d34e1eb6c59a588198/images/20841560930387653.jpg);background-color: transparent; background-position: center bottom; background-repeat: no-repeat;" bgcolor="transparent" background="https://hpy.stripocdn.email/content/guids/CABINET_d21e6d1c5a6807d34e1eb6c59a588198/images/20841560930387653.jpg">
                                        <!--[if gte mso 9]> <v:rect xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false" style="mso-width-percent:1000;height:204px;"> <v:fill type="tile" src="https://pics.esputnik.com/repository/home/17278/common/images/1546958148946.jpg" color="#343434" origin="0.5, 0" position="0.5,0" ></v:fill> <v:textbox inset="0,0,0,0"> <![endif]-->
                                        <div>
                                            <table bgcolor="transparent" class="es-header-body" align="center" cellpadding="0" cellspacing="0" width="600" style="background-color: transparent;">
                                                <tbody>
                                                    <tr>
                                                        <td class="esd-structure es-p20t es-p20r es-p20l" align="left">
                                                            <table cellpadding="0" cellspacing="0" width="100%">
                                                                <tbody>
                                                                    <tr>
                                                                        <td width="560" class="esd-container-frame" align="center" valign="top">
                                                                            <table cellpadding="0" cellspacing="0" width="100%">
                                                                                <tbody>
                                                                                    <tr>
                                                                                        <td align="center" class="esd-block-image"><a target="_blank" href="https://stripo.email"><img src="https://demo.stripocdn.email/content/guids/videoImgGuid/images/56961576947767745.jpeg" alt style="display: block; width: 126px; height: 117px;" width="126"></a></td>
                                                                                    </tr>
                                                                                    <tr>
                                                                                        <td align="center" class="esd-block-spacer" height="65"></td>
                                                                                    </tr>
                                                                                </tbody>
                                                                            </table>
                                                                        </td>
                                                                    </tr>
                                                                </tbody>
                                                            </table>
                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </div>
                                        <!--[if gte mso 9]> </v:textbox> </v:rect> <![endif]-->
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <table cellpadding="0" cellspacing="0" class="es-content esd-footer-popover" align="center">
                            <tbody>
                                <tr>
                                    <td class="esd-stripe" align="center" bgcolor="transparent" style="background-color: transparent;">
                                        <table bgcolor="transparent" class="es-content-body" align="center" cellpadding="0" cellspacing="0" width="600" style="background-color: transparent;">
                                            <tbody>
                                                <tr>
                                                    <td class="esd-structure es-p30t es-p15b es-p30r es-p30l" align="left" style="border-radius: 10px 10px 0px 0px; background-color: rgb(255, 255, 255); background-position: left bottom;" bgcolor="#ffffff">
                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                            <tbody>
                                                                <tr>
                                                                    <td width="540" class="esd-container-frame" align="center" valign="top">
                                                                        <table cellpadding="0" cellspacing="0" width="100%" style="background-position: left bottom;">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text">
                                                                                        <h1>Department of motor vechicle</h1>
                                                                                    </td>
                                                                                </tr>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text es-p20t">
                                                                                        <p><br></p>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="esd-structure es-p5t es-p5b es-p30r es-p30l" align="left" style="border-radius: 0px 0px 10px 10px; background-position: left top; background-color: rgb(255, 255, 255);">
                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                            <tbody>
                                                                <tr>
                                                                    <td width="540" class="esd-container-frame" align="center" valign="top">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="left" class="esd-block-text">
                                                                                        <p>Successful transaction.</p>
                                                                                        <p><br></p>
                                                                                        <p>For more information about your account, please visit log in through our website.</p>
                                                                                        <ul></ul>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="esd-structure es-p30t es-p30b es-p30r es-p30l" align="left" style="background-position: left bottom;">
                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                            <tbody>
                                                                <tr>
                                                                    <td width="540" class="esd-container-frame" align="center" valign="top">
                                                                        <table cellpadding="0" cellspacing="0" width="100%">
                                                                            <tbody>
                                                                                <tr>
                                                                                    <td align="center" class="esd-block-text">
                                                                                        <h3 style="line-height: 150%;"><br></h3>
                                                                                    </td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </table>
                                                                    </td>
                                                                </tr>
                                                            </tbody>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</body>

</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
import smtplib


def sent_status_email():
    """
    Send email for availability status tracking of products via gmail
    Require -Allow less secure apps- changing gmail account setting
    """
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # personal gmail address and password needed
    gmail_user = 'user1@gmail.com'
    gmail_password = 'gmailpassword'
    server.login(gmail_user, gmail_password)

    subject = 'Bose SoundLink Revolve Portable Bluetooth Speaker Is AVAILABLE!!'
    body = 'GO GET IT NOW!'
    # body = test.body
    email_text = "Subject: {'Bose SoundLink Revolve Portable Bluetooth Speaker Is AVAILABLE!!'}\n\n{'GO GET IT NOW!'}"

    ## personal gmail address needed
    sent_from = gmail_user
    to = ['user2@gmail.com']
    server.sendmail(sent_from, to, email_text)

    print('Status Tracking Email Sent!')

    server.quit()


#sent_status_email()



def sent_price_email():
    """
    Send email for price tracking of products via gmail
    Require -Allow less secure apps- changing gmail account setting
    """
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    gmail_user = 'user1@gmail.com'
    gmail_password = 'gmailpassward'
    server.login(gmail_user, gmail_password)

    sent_from = gmail_user
    to = ['user2@gmail.com']
    subject = 'Mask Price Went Down!!'
    body = 'Check the Amazon Link https://www.amazon.com/Disposable-Breathable-Comfortable-Pollution-Protection/dp/B0875S5TWF/ref=sr_1_4?dchild=1&keywords=surgical+mask&qid=1591309055&sr=8-4'
    # body = test.body
    email_text = "Subject: {'Mask Price Went Down!!'}\n\n{'Check the Amazon Link https://www.amazon.com/Disposable-Breathable-Comfortable-Pollution-Protection/dp/B0875S5TWF/ref=sr_1_4?dchild=1&keywords=surgical+mask&qid=1591309055&sr=8-4'}"


    server.sendmail(sent_from, to, email_text)

    print('Price Tracking Email Sent!')


    server.quit()

sent_price_email()

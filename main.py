import os
import webapp2
from google.appengine.api import mail

answer = 42.0
attachment = "attachment.txt"
senderAddress = "Your name <your@mail.com>"

class knowledgeWall(webapp2.RequestHandler):
  def post(self):
    # Get post request parameters
    userName = self.request.get('name')
    userMail = self.request.get('mail')
    userAnswer = self.request.get('answer')

    # Check knowledgeWall answer
    correct = False
    if float(userAnswer) == answer:
      correct = True

    # Send mail if answer and email are valid
    if mail.is_email_valid(userMail) and correct:

      # Open local file to attach to mail
      attachmentPath = os.path.join(os.path.split(__file__)[0], attachment)
      fileObject = open(attachmentPath, "r") 

      # Parse mail body
      body = """Dear %s,

Awesome you took the time to solve the "knowledge wall".

Kind regards, 

Your Name
""" % (userName)
      
      # Send mail
      mail.send_mail(sender=senderAddress, to=userMail, subject='KnowledgeWall content', body=body, bcc=senderAddress, attachments=[(attachment, fileObject.read())] )
      

    # Redirect to original referrer
    self.redirect(self.request.referer)


app = webapp2.WSGIApplication([
    ('/', knowledgeWall),
], debug=True)
# KnowledgeWall

As a fresh graduate I wanted to put my CV on my site who knows what it could bring. Not wanting my personal info to be scraped or merely added to a bottomless pit by recruiters I decided to build a tiny proof of concept. The snippet is nothing more than a tiny python script that validates a single post request.

<a href="http://www.thevelop.nl/about/">
    ![Screenshot of knowledge wall form](/screenshot.png "Screenshot of knowledge wall form")
</a>

## Set-up

Everything is hosted freely on the Google App Engine. Start by making a google account and creating a new project (note your `project ID`) in your [GAE console](https://console.cloud.google.com). Finally you will need the [GAE SDK](https://cloud.google.com/appengine/docs/standard/python/download) for python.

```sh
git clone https://github.com/theveloped/KnowledgeWall.git
cd KnowledgeWall
```

Now clone the repository and add your own validation and info to `main.py`. Replace the attachment.txt with an attachment of your liking and you are ready to go. Using the GAE SDK one can than deploy the app to the app engine using the following command:

```sh
gcloud app deploy
```

Make sure your is email address used for sending the mails is added on your GAE console under [Email API Authorized Senders](https://console.cloud.google.com/appengine/settings?_ga=1.103854786.397084214.1491736685). If so the only thing remaining is to add your question and a small form to your site to submit the `post` request.

```html
<form method="post" action="https://projectID.appspot.com/"> 
    <input type="text" placeholder="Name" value="" name="name" id="name" required>
    <input type="email" placeholder="Mail address" value="" name="mail" id="mail" required>
    <input type="number" placeholder="KnowledgeWall answer" value="" name="answer" id="answer" required>
    <button class="btn" type="submit">Submit</button>
</form>
```

## License

This script is released under MIT License.

# Foodmachine
A django implementation of food delivery app.
🍔🍕🍟📦🚗💁

Food machine is a webapp developed upon django framework.
We used
1) Django inhouse functions.
This was done for logging people into system. Storing address etc.
2) Webstorage Api
We use local storage to store the cart, inspiration from uber eats.

3) Sendgrid Api and foodmachine.ml domain name from freenom
Need to send a forgot password email, we got this.

4) Sqlite3 database
This was choice because Squilte3 is trackable in git, but once deploy with clicks django can connect and transfer data to any Database.Preferably MySQL.

Inorder to use this app, aftering clone signup for sendgrid and generate api.
This api key needs to be in settings and the env os.

After which all functions would be activated. Please go through Final documentation for more information.
You would have set secret in OS variable and run deployment checklist one last time..


# simple-salesforce tutorial for Python noobs
# Created by: Jack Galletta, Summer 2019
# This is a brief overview on making calls to Salesforce remotely via the simple-salesforce Python package
# IMPORTANT NOTE: this code will not alter your org at all out of the box

# importing the package
from simple_salesforce import Salesforce, SalesforceLogin
# Note: if the above line has red squiggly errors, you did not install the package properly

# fill in your Salesforce org credentials here
username = ''
password = ''

# This block of code creates a Salesforce instance by using your credentials to log in remotely
session_id, instance = SalesforceLogin(username=username, password=password)
sf = Salesforce(instance=instance, session_id=session_id)

print('Successfully logged in!')

# Now we are logged into your org, and we can start doing cool things within Salesforce

# 1. Creating objects
# this next line shows how to create a dummy object called myObject__c, and has some dummy fields to go along with it

# sf.myObject__c.create({'Name': 'thing', 'Color__c': 'green'})

# to create other objects: replace 'myObject__c' with your object's API name i.e. Contact, and fill fields accordingly
# so creating a contact would go as follows:

# sf.Contact.create({'Name': 'Chad McDude'})


# 2. Sending platform events
# this is as simple as creating an object, just replace the myObject__c with myPlatformEvent__e

# Ex: sf.myPlatformEvent__e({'myField': 'myValue'})


# 3. Updating/Deleting objects
# for this operation, we need the actual record ID of the object, but the syntax is very similar:

# sf.myObject__c.delete('myRecordId')
# sf.myObject__c.update('myRecordId', {'myField': 'myNewValue'})

# 4. Retrieving metadata

# this is literally just: sf.myObject__c.metadata()


# 5. Bulk records

# bulk managing records is as easy as making an array of the records, then sticking it all in one command

# data = [
#      {'LastName':'Smith','Email':'example@example.com'},
#      {'LastName':'Jones','Email':'test@test.com'}
#    ]
# sf.bulk.Contact.insert(data)

# you can also just do the same thing with a loop but this makes it slightly easier


# 6. Running Apex methods
# basically you create a payload with your desired method and parameters, then use apexecute to determine the endpoint
# here is an example:

# payload = {
#  "activity": [
#    {"user": "12345", "action": "update page", "time": "2014-04-21T13:00:15Z"}
#  ]
# }
# result = sf.apexecute('User/Activity', method='POST', data=payload)


# END OF TUTORIAL, thanks for reading!

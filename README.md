# MakersLink-MemberSystem
A repo to develop a member system for makersLink and learn Python/Django

## General requirements:
- Should include a move to PostgreSQL away from SQLite
- Should include a move to something like nginx+gunicorn for webserver
- Should plan to move functionality from Scheduling project into this project in the future
- Written as Django apps
- The ability to have scheduled tasks. Does not need to be fancy. Can use something like https://github.com/jcass77/django-apscheduler that does not require an external broker.
- Modular, each app should only be dependent on itself. For example if we extend the User model it must extend the base model so other apps that requires it can use it. For example we can check if a scheduler is installed and handle it accordingly.
- Usage of a base template for views so we get a coherent look and feel.
- Should work on mobile
- All text should default to English and use translation files for Swedish
- All Apps should implement Admin views and an Admin Group for accessing and using these views.
- Informational Logging to database so Admins can see what's happening

### Thoughts
- Unclear on how we allow Apps to insert themselves into menu since they will probably require some sort of Auth Group membership to be visible. Preferred not to hardcote.
- Unclear if logging is an App or just a general thing available to all Apps that they should implement
## Apps
These are the modular apps we should be working on.
### Member Portal
General look and feel. Should probably only check if someone is logged in or not.
- Contains the views we use for unauthorised users (If any)
- Contains the standard views for authorised users

##### Nice to have
- Read news from our public site/or newsletters and publish them
- Have some sort of news/notification functionality

### Members
App that handles our User model, User creation, User actions
- Allow registration of new users
- Users must confirm e-mail
- Username should be e-mail
- User model should extend to include information we need for our members.

##### Nice to have
- Captcha for registration
- Password checking for common or weak passwords
- Allow a user to be invited to Slack automatically once. If they require multiple invites it should be handled manually.

### Memberships
App that handles memberships and subscriptions. Also authorisation groups depending on membership but groups will probably have to be maintained manually since the apps themselves needs to support them.
- Allow creation of a Product or Membership type that holds information regarding name, description, and a list of Django Groups (Optional) that they become members of when holding this membership
- Allow creation of Subscriptions that connects a User and a Product/Membership and holds information regarding renewal period, price, and payment options.
- Allow creation of Payments to a specific subcription that is how to we move expiry dates forward.
- Allow Users to change Subscriptions/Have multiple Subscriptions
- Allow reminders to be sent for renewal to e-mail

##### Nice to have
- Integration with Swish

### Sales
App that handles sales of materials

### Inventory
App that handles inventory of member items, such as storage boxes or materials.
- Should support creating a PDF for printing
- Would be nice if it had local frontend for direct integration with a printer
- Would be nice if it had local frontend for logging in with RFID-tag for fetching labels and printing them

### MemberSecurity
App that logs when members are in the makerspace. We already have a local one that could be integrated to show when members are here.
- Show attendance with RFID-tag
- Add optional logout for highscore
- Optional to check if they have active membership
- Optional to support API-call for RFID-tag and Security group and get a boolean back saying if that RFID-tag is authorised.

# Later
### Training
App that handles training/certifications on machines/certain spaces. Should probably be included under Scheduling
- Dangerous machines?
- Security briefings for hosts?
- Allow expiry dates
- Allow signups
- Allow someone to say they're interested in a specific one

## Scheduling
To be moved over/redefined from other project, should integrate with google calendar and support templating when adding things to calendar.
### Workshops
Redefine when moving from Scheduling app
- Probably allow signup for members (Toggle)
- Probably allow signup for non-members (Toggle)
- Check if we need a Host to help out
- Check if it should take precedence over other activities in calendar

### Hosting
Redefine when moving from Scheduling app
- Allow signup as host
- Expiry date on host role
- Allow hosts to create one-off slots
- Add types to all events
- Instead of host periods being added to events, add rules to host periods and generate events for hosts belonging to that period
- Add functionality for reminders
- Add functinality for cancelling in calendar
- Add functionality for statistics



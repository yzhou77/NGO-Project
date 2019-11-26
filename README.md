# NGO-Project
## introduction
This functional requirement is part of a global web portal for a customer. Customer is a non-profit organization and branches all over the world. For fund raising, they organize various activities and events on multiple cities and sell the tickets and other artifacts like t-shirts, cap, etc. 

### functional specification

Application will have two user roles:
1. Admin users, who are responsible for user creation, event management such as event creation, event editing and make an event inactive.
2. Regular users, who can view the events and register for those events. They do not have any capabilities of admin functionalities.

### Admin Module:
Admin user(s) are responsible for:
- Creation of n-numbers of regular users. There will be a default Admin user who will be added directly in the database.
- Manage events.

Upon login, if the user is an admin user, he/she will see a screen like this:

From above screen, Admin user can manage existing users or create n-number of users. When “Add User” or “Edit” link is clicked, a popup screen will appear with these entry fields:
- First Name
- Last Name
- Email
- Password
- Role(Dropdown with two values : Admin & User)
- Save Button
- Cancel Button
Once the Save button is clicked, popup window will close and changes will be reflected on the grid (table).

Admin user can create and make adjustments to an existing event by using this screen:

When “Add a New Event” or “Edit” button is clicked, a new popup window will appear with these information:

i. Event Name

ii. Event Description(Varchar(200))

iii. Event Category(Dropdown list with Static Options: Conference, Seminar, Presentation

iv. Event Start Date

v. Event End Date

vi. Event Start time

vii. Event End time

viii. Event Location

ix. Allow registration? Boolean T/F: if this is false, end users cannot make a registration.

x. Event Image

xi. Adult Ticket Price

xii. Child Ticket price

xiii. Save button

xiv. Cancel button


All the changes made on this popup will reflect on the grid (table) view.

Admin user will have an option to see the user view, when clicked, it will show a screen like this:

Functionality of the above screen is same as user view and explained below.

### User Module:

When a non-admin user login, he/she will see a screen like this:

Above screen will show all the events created in the system. These boxes are clickable and when clicked, it will open a screen like this:

When user clicks on Registration button on above screen, he/she will be redirected to a new screen which allows to complete the registration process.

a. users will be asked to enter these information:

  xv. Event Name should appear at the top of this screen.
  
  xvi. First Name
  
  xvii. Last Name
  
  xviii. Email ID
  
  xix. Contact#
  
  xx. Address
  
  xxi. Total Adult Qty
  
  xxii. Total Child Qty
  
  xxiii. Next button

b. When user clicks on Next button, we will show the totals prices depending on quantities he/she selected for Adult and Child along with Confirm registration button.

c. When user clicks on this button, redirect to Event registration confirmation screen.


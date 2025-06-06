﻿[](#expresso)
# Expresso

** Site is no longer live **

![I Am Responsive Screenshot](static/img/amiresponsive.png)

Say hello to Expresso, a card based point of sale system designed to run from your smartphone. Users can create, edit and delete the Menu, Sub-menu and Item categories to build an app that best suits their needs. Build and edit an order, confirm payment and save the day's transaction data for export via email at the end of the day as a .csv file.

## Table Of Contents

- [Introduction](#introduction)
- [The Initial Idea](#the-initial-idea)
- [The 5 Planes of UX Design](#the-5-planes-of-ux-design)
- [Technologies](#technologies)
- [PostgreSQL Database Schema](#postgresql-database-schema)
- [Building And Testing ](#testing)
- [Validation](#validation)
- [Bugs And Fixes](#bugs-and-fixes)
- [Unfixed bugs](#unfixed-bugs)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

## Introduction

Expresso is a mobile friendly way to track your sales throughout the day. Featuring a responsive design that looks great on phone, tablet or desktop. Fully customisable to match the needs of the user.

## The Initial Idea

The idea for Expresso came from several areas. First and foremost from my experience of being front of house in a small independent cafe in a nearby town and using a point of sale system. Secondly from browsing the market stalls that appear every weekend just opposite my place of work, and talking to stall owners. Lastly from chatting with my work colleagues and listening to their views and opinions about interacting with a till.

I have a banking app that allows me to take payments via Apple or Google Pay using my phone as the terminal. This is enabled by Stripe and removes the need for any integrated payment software. By combining this payment functionality with a flexible point of sale system you can effectively manage a small shop, a market stall, a popup shop or even a carboot sale. The data from the app can be exported as a .csv file meaning that you could upload the data into a suitable accounting app and manage your whole business with nothing more than a smartphone.

[View the deployed app here](https://mp3-pointofsale-4872260bbf57.herokuapp.com/)

[Back to the top](#expresso)

## The  5 Planes of UX Design

### Strategy Plane

There were two stories to be considered during the design of this project. They were the creator's story and the user's story. 

### The Creator Story

- As the creator I want the site to be as intuitive as possible. Navigation should be clear and obvious. Instructions on use should be clear and concise and easy to navigate to.

- As the creator I want the site to be consistent in terms of layout and features such as the button design and the colour choices.

- As the creator I want the site to have an app like feel on mobile/tablet screens but one that will scale appropriately when viewed on larger  
  displays.

- As the creator I want the data stored in the app to be exportable as a record of the days transactions as record or for use in other apps.

- As the creator I want the app to be easy to reset and start again.

### The User Story

- As a first time user I want the site to be as intuitive as possible. There should be no confusion over navigation or purpose.

- As a first time user I want the site to have a clear easy to organise layout.

- As a first time user I want an easy to understand explanation of how to use the app.

### Scope Plane

The idea for this app came from my experience and others of working for or as a small business. The concept is not to offer an 'all in one' solution but to offer an app able to work in conjunction with existing apps ie. taking contactless payments with a smartphone and an accounting app to offer an inexpensive way of managing a startup or full or part time small business.

### Structure Plane

With the scope laid out the basic structure could be decided. With experience of tills that are far from user friendly the focus was on a clean simple interface that is responsive and works across differing screen sizes ie. phone, tablet and desktop. Navigation needs to be fluid, quick and intuitive. The user needs confirmation of actions, warnings for actions that cannot be completed and an option to cancel. Data created by recording transactions needs to exportable so it is not trapped within the app and can be utilised by other apps the user may have.

### Skeleton Plane

A wireframe of the proposed layout was drawn on the reMarkable 2 e-ink tablet and is presented here to show how the initial design of the site was imagined.

![Wireframe Image](static/img/wireframe.png)

### Surface Plane

The site maintains a clean simple interface throughout. Bootstrap provides easy to read modern fonts that suit the apps look. The colour scheme is subdued with no overly bright colours as nobody wants to stare at an overly bright display all day. The colours used throughout the app help confirm actions ie. green for additions, red for deletions and blue for navigation and the cancel option. The site colours have a good contrast that helps with readability.

## Technologies

Here are the main technologies used to create the app.

- [HTML5](https://html.com/)
- [Bootstrap5.3.2](https://getbootstrap.com/) - CSS and Javascript library.
- [FontAwesome5.15.3](https://fontawesome.com/?utm_source=font_awesome_homepage&utm_medium=display&utm_campaign=fa5_released&utm_content=auto_modal) - Icons.
- [Favicon.io](https://favicon.io/favicon-generator/) - generates favicon icons.
- [Heroku](https://www.heroku.com/home) - Platform used for deployment.
- [Flask](https://flask.palletsprojects.com/en/3.0.x/) - Python web framework.
- [Jinja2](https://jinja.palletsprojects.com/en/3.0.x/templates/) - Template engine.
- [amiresponsive](https://ui.dev/amiresponsive) - test responsiveness of app.
- [reMarkable 2](https://remarkable.com/?gclid=CjwKCAjw-eKpBhAbEiwAqFL0mjnSR2zODkqzP-cwnbtZjaD9ymtxH51xXF-P7hNAoczEilK_ouLNQRoCeSUQAvD_BwE) - for wireframe.
- [smartdraw](https://www.smartdraw.com/entity-relationship-diagram/er-diagram-tool.htm) - free online entity relational diagram creator.
- [Visual Studio Code](https://code.visualstudio.com/) - IDE used to develop the app.
- [Github & Git](https://github.com/) - to manage the development of the app
- [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - invaluable for testing and debugging
- [And others can be found here, requirements.txt](requirements.txt)

[Back to the top](#expresso)

## PostgreSQL Database Schema

There are five schemas modelled in the 'models.py' file for the PostgreSQL database. 

1. Menus - id as primary key, menus_name (25 chars max cannot be null), menus_description (29 chars max cannot be null) and submenus that allows for a cascade delete so that associated submenus are deleted if the menu is.
2. Submenus - id as primary key, submenus_name (25 chars max cannot be null), submenus_description (29 chars max cannot be null), menus_id (foreign key of menus.id cannot be null) links submenus to the correct menu and items that allows for a cascade delete so that any associated items are deleted when the submenu is.
3. Items - id as primary key, items_name (25 chars max cannot be null), items_description (29 chars max cannot be null), items_price (floating number cannot be null), items_costprice (floating number cannot be null) and submenus_id (foreign key of submenus_id cannot be null) links items to the correct submenu that allows for a cascade delete so that any associated items are deleted when the submenu is.
4. Currentorder - id as primary key, currentorder_name (25 chars max cannot be null), currentorder_price (floating number cannot be null), currentorder_costprice (floating number cannot be null), item_id (foreign key of item_id cannot be null) links back to the item to prevent deleting an item if it is present in the current order.
5. Transactions -id as primary key, transactions_name (25 chars max cannot be null), transactions_price (floating number cannot be null), transactions_costprice (floating number cannot be null). Not linked to any of the other schemas.

![Simple ERD showing the database relationships](static/img/database_schema.png)

## Testing

Manual testing was selected as the best way to check the app as a modular approach to the build meant that each part
could be tested as the code was assembled and many of the bugs fixed before final testing.

### Test 1: base.html renders the startscreen and navbar shows correct links.

- Expected:   That base.html template renders the startscreen with a header, footer and placeholder text. Navbar displays 
              the correct links.
- Testing:    App was launched with run.py.
- Result:     The startscreen rendered correctly with all elements displaying correctly. Decided to change navbar link names.
- Fix:        Change names of navbar links to better reflect the app. Test passed.

### Test 2: addition of Menu options incl. add, edit and delete and mainscreen.html displays all menus.

- Expected:   That a menu could be added and displayed, edit, delete and sub-menu buttons would display correctly.
- Testing:    The app was launched with run.py
- Result:     A menu was added and displayed correctly. edit, delete and sub-menu buttons displayed correctly.
- Fix:        No fix required. Test passed.

Once these two initial tests had been successfully completed the 'Menu' code was repurposed for the sub menus and added to the build

### Test 3: addition of Submenu options incl. add, edit and delete and view_submenus.html displays all submenus.

- Expected:   That a submenu could be added and displayed, edit, delete and item buttons would display correctly.
- Testing:    The app was launched with run.py
- Result:     A submenu was added and displayed correctly. edit, delete and item buttons displayed correctly.
- Fix:        No fix required. Test passed.

With the code now allowing menus and submenus to be added correctly the 'Sub-Menu' code was repurposed for items and added to the build.

### Test 4: addition of Item options incl. add, edit and delete and view_items.html displays all items.

- Expected:   That an item could be added and displayed, edit, delete and add to order buttons would display correctly.
- Testing:    The app was launched with run.py
- Result:     An item was added and displayed correctly. edit, delete and add to order buttons displayed correctly.
- Fix:        No fix required. Test passed.

At this point the basic card structure was in place and the testing continued with the addition of edit and delete functionality.

### Test 5: checking the routing and adding in edit and delete functions.

- Expected:   That edit/delete works as expected
- Testing:    The app was launched with run.py. The PostgreSQL database was monitored using SQL shell in Windows 11 submenus and 
              items were added, edited and deleted
- Result:     Issues with passing of variables to identify which menu/sumenu/item needed editing/deleting. Some styling issues when presenting Bootstrap cards.
- Fix:        Routing issues were fixed by passing the relevant identifiers into the necessary app routes in routes.py file. Bootstrap classes adjusted to improve consistency of look across different screens. Test passed.

With the app now up and running the 'Order' screen was coded allowing items to be added to the current order. A 'paid' button, displaying the current order total, moves details about this order to the transactions list and clears the screen ready for the next order.

### Test6: adding to an order and then posting this to transactions.

- Expected:   That an order can be created by adding items to the order and then viewed in the 'Order' tab of the navbar. That the paid option button displays and shows
              the correct order total in the correct format and moves the order to transactions.               
- Testing:    The app was launched with run.py. The PostgreSQL database was monitored using SQL shell in Windows 11. An order was created and then the 'paid' option clicked.
              The PostgreSQL database was checked to verify that the correct actions had happened as expected.
- Result:     Issues with passing of variables to identify which menu/submenu/item needed editing/deleting. Some styling issues when presenting Bootstrap cards.           
- Fix:        Routing issues were fixed by passing the relevant identifiers into the necessary app routes in routes.py file. A global variable used in calculating the total
              order price was removed by making the total price calculation a function. PostgreSQL was confirmed to have updated correctly. Bootstrap classes adjusted to improve consistency of look across different screens. Test passed.

The final part of the build was to add in the ability to email a.csv file containing the days transactions to a nominated email address.

### Test7: email a .csv file to an email address.

- Expected:   That when selected an email address could be input and a .csv file containing data about the day's sales could be sent to the email address. That the
              transactions list would clear after the email was sent.                        
- Testing:    The app was launched with run.py. The PostgreSQL database was monitored using SQL shell in Windows 11. An order was created and then the 'paid' option clicked. The PostgreSQL database was checked to verify that the correct actions had happened as expected. Then from the 'Sales' screen the 'send email; option was selected. An email address was input and 'send' selected.
- Result:     Email address defaulted to 'gavin.brown@4uxdesign.com' which was a placeholder address needed for the routing. The input email address was ignored.
- Fix:        The issue was identified as a form issue. When inputting an email address the form value had been set to the placeholder email address. Once this was removed  
              the email correctly sent.

With the basic design and functionality now in place testing could begin for browser, device and Google Lighthouse.

### Browser Tests: the browsers used.

The app was tested on Google Chrome Version 122.0.6261.112 (Official Build) (64-bit), Mozilla Firefox 123.0.1 (64-bit), Microsoft Edge Version 122.0.2365.80 (Official build) (64-bit), Safari, mobile Safari on Apple iPhone 14 running iOS 17.4 and Safari on Apple iPad running iOS 17.4. Google Chrome developer tools were also used to try various different devices/screen resolutions. The app proved to be responsive, scaling correctly across different resolutions with no apparent display issues. All functionality was maintained and the testing was considered successful.

[Back to the top of testing](#testing)

[Back to the top](#expresso)

### Validation

The code was structured for HTML using the [VScode](https://code.visualstudio.com/) 'HTML language features' function, and for Python the [CI Python Linter](https://pep8ci.herokuapp.com/) was used. There were two issues left unresolved both with the Python code. The lines 115 and 245 are reported as too long but they have been left as is to improve readability. The official [Pep8](https://peps.python.org/pep-0008/) guidelines say that readability is key.

For validation the site was checked using [W3C HTML Validation Service](https://validator.w3.org/). The page checked was the 'base.html' page as this is the template for the site. There was an error raised for the double curly braces used by the template engine Jinja2 however this is to be expected as it is not HTML. In this instance the error can be safely disregarded.

![W3C Validation Screenshot](static/img/w3c_html_validation.png)

The site was built using the Bootstrap5 library and therefore no validation testing for CSS or Javascript was possible.

The next test was to put the app through [Google Lighthouse](https://developer.chrome.com/docs/lighthouse/overview). The results were a very impressive 100 in the four categories tested, Performance, Accessibilty, Best Practices and SEO. This confirms that the site performs well and is accessible and search engine optimised.

![Google Lighthouse Report](static/img/lighthouse_report.png)

## Bugs And Fixes

With the code in its finished form the app was subjected to a rigorous hands on testing regime as I looked to uncover any bugs or design changes that would only become apparent through hands on use. Documented here are the major bugs/issues that were found and resolved. 

- The price of items, total price of the order and the transactions prices didn't display correctly. Added templating format to number presentation to get the correct GBP
  £00.00 format.

- The submenu and item pages were missing navbar options preventing navigating away from these pages. The correct templating was added to the navbar to correct this.

- An error crept into the routing preventing the edit functions from working. this was traced to an incorrect variable and therefore value being passed causing a SQLalchemy
  error and the app to crash when confirming an edit. The variable was changed and the error corrected.

- There was no confirmation when creating new menus, submenus or items. A dismissable alert was created for this to notify the user.

- The submenu name was missing from item card. The variable {{ submenus.submenus_name }} was missing. Adding the variable in corrected this issue.

- The order that items and submenus were displayed in varied meaning if you had a large number of these you could easily lose track of where they were.
  This was found to be a missing .order_by() when creating lists of items and submenus in routes.py. Once added the cards displayed consistently.

- The code had been using a string as 'True' rather than a boolean value as there was a problem evaluating the boolean as True. This turned out to be because Jinja2 
  evaluates a boolean and reports the result as a string, so True is evaluated as 'True' not True. The code was adjusted and boolean values used.

- After some minor styling changes the app stopped working completely on Heroku and after a lengthy investigation I discovered that something in the previous four commits
  had broken the code. Rolled back the code using git hard rest and git force push and the app started working again. This can be seen in the commit record on Github. The commit ref is efd5f9a.

- A 'back to top' was added to the footer on mainscreen, view_submenus, and view_items screen to enable an easy option to go back to the top of the displayed cards.

- Added an alert when trying to delete a menu that has submenu or when deleting a submenu that has items preventing a SQLalchemy error and the app crashing.

- Added an alert when trying to delete an item that is in the currentorder preventing a SQLalchemy error and the app crashing.

- Changed the route in transactions from a return to a redirect preventing a SQLalchemy error and the app crashing.

- Added a 'reset app' feature that allows the user to delete the whole database and start from scratch removing the need for the user to do this manually.

- Removed unnecessary code from reset app function as deletion of a menu cascades through submenus and items so no need to delete submenus and items separately.

- Decision was taken due to time pressures to remove the custom 404 handling as it wasn't working.

- After feedback from my tutor another bug was found. If a non number is entered either for item price or cost price a SQL error is generated and the app crashes. This was found to be an incorrect type attribute in the input fields. The type should have been number but instead was text. With the addition of the step attribute set to '0.01' this prevents non numbers from being added and prevents a SQL error and app crash.

- Whilst fixing the previous bug another issue was found. If the name hit the char limit it overspills on the order page making it difficult to read. The fix was to add the Bootstrap classes text-wrap and text-break which prevents the overspill.

[Back to the top of validation](#validation)

[Back to the top](#expresso)

## Unfixed Bugs

There two main issues that remain unresolved..

 - Firstly the custom 404 page did not work. Several fixes were tried but none resolved the issue so the decision to remove the page and rely on the default 404 error page was taken.
 - Secondly the favicon icon is missing. Again several fixes were tried but none worked. The favicon remains in the code but does not present on page load.

## Deployment

This project was deployed from VS Code to Heroku and the PostgreSQL database to ElephantSQL

- Navigate to [ElephantSQL](https://www.elephantsql.com/)
- Select 'Create New Instance'
- Enter a name and select 'Tiny Turtle (Free) then select 'Select Region'
- Select 'EU-West-1 (Ireland) as the data center then select 'Review'
- Select 'Create Instance'.
- Return to the main screen and select your newly created instance.
- from 'details' copy the URL.
- In the terminal of your IDE launch python with 'python + return' enter the command 'pip3 freeze > requirements.txt', and a file with all the app requirements will be created.
- Add a 'Procfile' to the root of your project. In the Procfile add 'web: python run.py'
- Push these changes to Github.

-  Setting up Heroku
  - Go to the Heroku website [here](https://www.heroku.com/).
  - Login to Heroku and choose 'Create App'.
  - Click 'New' and 'Create a new app'
  - Choose a name and select your location
  - Go to the 'Settings' tab. In 'Config Vars' 'Reveal Config Vars' and add the keys DATABASE_URL from ElephantSQL, DEBUG, EMAIL, IP, PORT and SECRET_KEY from the env.py file.
  - Select 'More' then 'Run Console' and when the console opens type
      - python then 'return'
      - from pointofsale import db
      - db.create_all()
      - exit()
  - Navigate to the 'Deploy' tab
  - Click on 'Connect to Github' and search for the repository
  - Enable automatic deploys
  - In 'Manual Deploy' make sure the main branch is selected and click 'Deploy Branch'
  - When the app build has completed click 'Open App' to launch.

  ## Credits

  - [Bootstrap Docs](https://getbootstrap.com/docs/5.3/getting-started/introduction/) for help with Bootstrap.
  - [Jinja Docs](https://jinja.palletsprojects.com/en/3.0.x/templates/) for help with templates.
  - [Stackoverflow](https://stackoverflow.com/) for some great suggestions to fix issues.
  - [Github - akshay-sri123](https://gist.github.com/akshay-sri123/9b49cba8e179fc1bedd73655d9327bf5) for a partial solution to sending an email.
  - [This thread from Stackoverflow](https://stackoverflow.com/questions/51644454/how-to-attach-an-existing-csv-file-to-an-email) for the rest of the solution to sending emails.

## Acknowledgements

- [Code Institute](https://codeinstitute.net/) for inspiring me to try something new.
- My tutor Ashley Oliver for help, support and timely advice.

[Back to the top](#expresso)

# CITS3403-Project
A web application to chat with AI.

## Description
- This is a chatting application that allows its user to chat with an AI supported by OpenAI`s CHATGPT 3.5 API. 
- User can chat with the AI about basically anything.
- Every chatting message can be traced and found by user.

### CSS Design
- using same backgound
- using same font
- all corners are filleted 
- minimalism sytle
- user friendly, all elements and buttons are clear, all functions are easy to use, giving hints in different places
###  View Structure Design
- four views
- user starts with login page with context explains below
- user can jump between login page and register page
- after validation, user auto jump into chat page
- there is a nevigation bar in chat page and search page to help user switch between these two views
- user can logout using nevigation bar, and will be jump back to login page
- in chat page there is a chat window for user to interact with chatbot
- in search page, there is a search bar for user to search chatting history with keywords or getting all chatting history at once
- in search page, search result will shown below the search bar
###  Project Structure Design
- well-documented. html, css, js, data... different types of files are stored in different folder, and folders are placed by their usage
- use base.html, build all views from same base, and functions like nevigation bar is defined in reuseable files, so that there is no redundant codes


### Development

- This application was developed by Jesse Yang (23307563) and Qichong Huang (23311085). Jesse handled the back-end development, while Qichong took care of the front-end development.
- We generated the initial concept through discussions and devised a plan to initiate the development process.
- Employing an agile development approach, we divided the development into several distinct phases.
  - During the first sprint, we created a prototype of the application, established the foundational server router, and developed basic web pages. Jesse focused on familiarizing himself with the OpenAI API for the subsequent sprint.
  - In the second sprint, we implemented a chatbot and integrated search functionality for the chat history.
  - In the final sprint, we conducted comprehensive testing of the application, resolved various bugs, and completed the documentation.
## How to install
First, clone the repository into a folder

### Windows
1. Ensure you have Python installed.
2. Run `setup.bat`.
   
### Unix-based systems (Linux/Mac)
1. Ensure you have Python 3 installed.
2. Run `setup.sh`.

## How to run
1. Ensure you are in the .venv virtual environment. If not, re-enter by running the `setup` script again.
2. In the terminal, Run `flask run`.
3. Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser of choice.

## How to test
- Replace `app/config.py` with `test_config.py` in the `tests` folder, then rename it to `config.py`.
### Unit test
1. Duplicate the `prototype.db` in the folder `app/data`, rename the new copy as `test.db`.
2. In the command line, go to the `tests` folder.
3. Run `python test_routes.py`.
4. Delete `test.db`.
### Selenium test
1. Duplicate the `prototype.db` in the folder `app/data`, rename the new copy as `test.db`.
2. Run the application.
3. In the command line, go to the `tests` folder.
4. Run `python selenium_test`.  
5. Delete `test.db`.
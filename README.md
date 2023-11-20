# AgriViz

"AgriViz: Integrated Agricultural Yield Monitoring and Visualization System," portrays a solution for modern agricultural data management and analysis. The main idea behind this project involves the creation of a SQL relational database on Amazon RDS, together with a structured data processing pipeline. Raw agricultural yield data is systematically collected, organized, and made available for further analysis.

The front end is a user-friendly web application which is created by Python Flask and MySQL, that helps in accessibility for various users. The application includes a secure login and registration system. The home page consists of field, dates, and year selection options for various fields. The center of this project lies in the integration of Amazon QuickSight, a data visualization tool. Users can quickly transition to QuickSight, where they gain access to raw yield data that they selected on the home page. This empowers them to explore, analyze, and visualize the data in various ways, from heat maps to geographical plots, and can also apply filters for customized insights on the raw data.

# Directory Overview

* Web_application - Contains all the files to create the web application
  * app.py - Python file that has the main web application structure
  * static
    * style.css - CSS file used to add styling to the web application
  * templates
    * home.html - HTML file to design the home page
    * index.html - HTML file to design the login page
    * layout.html - HTML file to design the home page
    * profile.html - HTML file to design the profile page
    * register.html - HTML file to design the register page
* Query_harvestDB - MYSQL queries to create the harvest database
* Query_processedDB - MYSQL queries to create the processed database
* Query_pythonlogin - MYSQL queries to create the login database (Stores user information)
* as
* awa

# Front-end

* Download and install Python. Make sure to check the Add Python to PATH option on the installation setup screen.
* Download and install MySQL Community Server and MySQL Workbench.
* Open the command line and Install Python Flask with the command: **pip install flask**      
* Install Flask-MySQLdb with the command: **pip install flask-mysqldb**
* Once you have all the files under **Web_application** folder locally follow the following steps:
  * Make sure your MYSQL server is up and running. Also, make sure MYSQL is running on port 3306 otherwise it will face connection errors
  * Open the Command Prompt and navigate to your project directory
  * Run command: **set FLASK_APP=app.py**
  * Run command: **set FLASK_DEBUG=1**
  * Run command: **flask run**

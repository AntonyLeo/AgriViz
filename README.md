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
* fields_to_DB.py - Python file to upload field data into the field table in the harvest database
* picker_to_DB.py - Python file to upload picker data into the picker table in the harvest database
* carts_to_DB.py - Python file to upload cart data into the cart table in the harvest database
* raw_data_to_DB.py - Python file to upload raw data into the raw_data table in the harvest database
* select_inputs.py - Python code to select the appropriate inputs needed to run the yield map generation code
* processed_data.py - Python code to upload the generated yield map into the proce table in the processed database
* field.xlsx - Raw data file for field 
* Carts_2022.xlsx - Raw data file for 2022 carts - salinas
* Spence_picker_2022.xlsx - Raw data file 2022 pickers - salinas
* yield data - csv files with yield generation of each day.
* Harvest 2022 - Files with raw data for the 2022 harvest 

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

These steps should get the front-end up and running 

# Back-end

* Once you have all the raw data (field.xlsx, carts_2022.xlsx, Spence_picker_2022.xlsx, Harvest 2022)
* Run Query_harvest_DB and Query_processed_DB in MYSQL Workbench to create the Harvest and Processed databases.
* Once you have the databases created, run field_to_DB.py with field.xlsx file to update field table, run picker_to_DB.py with Spence_Picker_2022.xlsx file to update picker table, run carts_to_DB.py with Carts_2022.xlsx file to update cart table, and finally run raw_data_to_DB.py with Harvest 2022 file to update raw_data table. This is to update the Harvest database.
* Once the database is all set and populated, run select_inputs.py python file to select the appropriate inputs needed to run the yield map generation code
* Once the yield maps are generated, run processed_data.py python file to upload the generated yield map into the proces table in the processed database and also to create a table locally.

These steps should get the back-end up and running

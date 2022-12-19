# CHUNK_FILE (TEAM FROGPP)
## Introduction.
Chunk_Files is an online platform that allows individuals to upload large CSV or JSON files and splits the dataset in the uploaded CSV or JSON file into multiple files as specified by the user making use of available option such as size of each new file.
## Objectives
+ Allow users split large files.
+ Users should have the ability to save the files for later and download.
+ Users should be able to see history of previous file operations performed.
## Solution
+ A tool for splitting CSV and JSON files as well as other file formats.
+ Easy download, import and save of CSV and JSON files.
+ Ability to perform split operations according to various parameters like size and number of rows.
+ Ability to view history of files chunked.
## Structure of the Webapp 
+ Home page.
+ Landing page.
+ Contact us page
+ Sign in and sign up page.
+ Tools page containing; csv and json splitter and other file converters.
+ Terms of service page.
+ Privacy policy page

## Technologies Used
+ Frontend: HTML, CSS and JavaScript.
+ Backend: Python
+ Design: Figma
## Features of the Webapp
+ The platform has many features which are accessible to both registered/authenticated  and unauthenticated users.
+ They can only view the documentation
+ They can register or login to make use of the platform.
+ They can see answers to FAQs
+ They can view an example of how the webapp is used
+ The following features are only available to authenticated user.
+ Auth. Users have full access to the Platform.
+ Auth. Users can upload a CSV or a JSON file.
+ Auth. Users can specify the sizes of each new file.
+ Auth. Users can download the chunked files in a zip file or separately.
+ Auth. Users can save the file and download later.
+ Auth. Users can view history of files chunked.
## Why use chunk_file?
+ Data analysis depends on the ability to find insight from data sets, however, some datasets can sometimes be voluminous to feed into data algorithms which will hinder the completion time of such algorithms, hence the need to feed data algorithms with small sets of data for learning. 
+ A society or a school record with a high number of data needs to be split into separate files for different analyses and classification.
+ Chunk_file allows you to specify the type of data format you want to receive (presently we have only CSV and JSON formats.).
## How to use chunk_file
+ Drag and drop your CSV or JSON file into the allocated space or Select upload file and choose a file from your directory 
+ Select the sizes of the chunked files [for unequal sizes seperste sizes by comma e g (2Mb, 3Mb, 1.4Mb etc)].
+ Select the output file format (CSV or JSON).
+ Select either to doe load zip or seperate files.
+ Click on chunk file to chunk your files 
+ Select Download to download the zip or seperate files.
## FAQs
+ What is CSV? A CSV file is information seperated using commas, It’s a way to exchange structured information, like the contents of a spreadsheet. Due to its simplicity, CSV can be used by virtually anyone who examines data in spreadsheets and tables. We offer splitting and conversion of CSV files. This tool allows you to split large CSV files into smaller files based on your specicification.
+ What is JSON? JSON is an open standard file format for sharing Data that uses human-readable text to store and transmit data. It is a general data format used with different applications, including web applications. It is a lightweight format for storing and transporting data. Web Developers use JSON to transmit data from the server to the web browser and from the web browser back to the server.
+ Why do I need to split CSV? Some systems are limited in terms of the size of data they can process. In this case, it is then necessary to split the CSV/JSON files so that they are processed. In other cases, the limitation is at the level of the sending of the data (although a compressed CSV normally takes up little space, the text being easily compressed).
+ How do I split my CSV files? To split your CSV file, follow these simple steps: Sign in to your dashboard (if you don’t have an account, create one and Sign in) Upload the CSV file(s) to our servers for splitting Download or save your chunked files
+ How do I split my JSON files? To split your JSON file, follow these simple steps: Sign in to your dashboard (if you don’t have an account, create one and Sign in) Upload the JSON file(s) to our servers for splitting Download or save your chunked files
+ Are my files stored on the site? Every user is given the option to have their chunked files stored on our servers. The storage of chunked files is not automatic and is at the choice of each user. Files not saved will be kept in the drafts on the dashboard for a very limited amount of time.
+ How long are files stored on the site? Draft files are stored for 24 hours only.
+ Are my stored files secure? YES. Every action happens on your local system. it doesnt go to our Database.
+ What is the maximum file upload size? The maximum upload size is 5Gb, pending updates to the server.
+ Can i change the output file format? Yes, you can specify the output format to either JSON or CSV, other file formats will be available on server updates.


### To visit the website click the link below
https://chunk-it-1.herokuapp.com/
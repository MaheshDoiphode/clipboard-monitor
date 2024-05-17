# Clipboard Monitor

This project is a utility that monitors your clipboard and stores the copied data in a MongoDB database. It's especially useful for tasks that involve a lot of copying and pasting, as it allows you to easily retrieve any data that was previously on your clipboard.

## How it Works

The utility uses a Python script to monitor the clipboard. Whenever the `ctrl+c` key combination is pressed, the script retrieves the current clipboard data and sends it to a Spring Boot application. The Spring Boot application then stores the clipboard data in a MongoDB database along with a timestamp.

## Prerequisites

To run this utility, you'll need:

- Python 3.6 or later
- The `pyperclip` and `keyboard` Python libraries
- Java 8 or later
- Spring Boot
- A MongoDB database

## Setup

1. Install the required Python libraries by running `pip install pyperclip keyboard` in your terminal.
2. Set up your Spring Boot application and MongoDB database.
3. Update the Python script with the URL of your Spring Boot application.
4. Run the Python script as an administrator.

## Usage

Once the Python script is running, it will monitor your clipboard and store the copied data in the MongoDB database whenever you press `ctrl+c`. You can then use your Spring Boot application to retrieve and view the stored clipboard data.

## Note

Not necessarily but can follow if not working - The `keyboard` library requires elevated privileges to function, so you'll need to run your Python script as an administrator. Also, the `keyboard` library can be resource-intensive as it's constantly monitoring all key presses. This can lead to high CPU usage, especially if there are other processes also running on your computer.




## Long Description
```
Sure, here's a detailed technical description of the Clipboard Monitor project:

The Clipboard Monitor is a utility designed to persistently store and track data that a user copies to their clipboard. This is achieved through a combination of Python scripting for clipboard monitoring and a Spring Boot application for data handling and storage in a MongoDB database.

The Python script is the primary driver of the clipboard monitoring functionality. It utilizes the `pyperclip` and `keyboard` libraries to detect when a user copies something to their clipboard. The `keyboard` library is used to register a callback function that is triggered whenever the `ctrl+c` key combination is pressed. This callback function then uses the `pyperclip` library to retrieve the current clipboard data.

Once the clipboard data is retrieved, the Python script sends this data to a Spring Boot application. This is done through a HTTP request, with the clipboard data included in the request body.

The Spring Boot application is responsible for handling the received clipboard data and storing it in a MongoDB database. It exposes an endpoint that the Python script can send requests to, and includes a service layer that handles the data storage. When the Spring Boot application receives a request from the Python script, it extracts the clipboard data from the request body and stores it in the MongoDB database along with a timestamp.

This setup allows the Clipboard Monitor to continuously track and store clipboard data, providing a persistent clipboard history that can be easily accessed and searched. This can be particularly useful for tasks that involve a lot of copying and pasting, as it allows the user to retrieve any data that was previously on their clipboard.

In terms of prerequisites, the Clipboard Monitor requires Python 3.6 or later for the Python script, Java 8 or later for the Spring Boot application, and a MongoDB database for data storage. The `pyperclip` and `keyboard` Python libraries are also required for the clipboard monitoring functionality.
```

## Short Description
```

```
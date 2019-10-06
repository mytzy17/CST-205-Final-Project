# Image to Text Translator

# Description 
The main idea of the project is to be able to upload an image with unknown text and translate it to a desired one. The user will be able to upload an image (with text) from any location in their machine and have it translated to any one of over 104 languages supported by Google's Translator API. 

# Prerequisites
Clone the repository: 
```bash
git clone https://github.com/dignacio0815/CST-205-Final-Project.git
cd CST-205-Final-Project
```

Please install the following dependencies listed below in your terminal: <br />
```bash
brew update
pip install --upgrade pip
pip install -r requirements.txt
```

# Installing
Getting the application running: 

1. Follow link to get credentials for API Key authentication by following Google Translate API documentation:
``` bash
[Google Translator API Documentation](https://cloud.google.com/translate/docs/reference/libraries)
```
2. Set up your enviornment variables by running: <br /> 
MacOS:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="[PATH TO YOUR API KEY.json]"
```
Windows Powershell:
```bash
$env:GOOGLE_APPLICATION_CREDENTIALS="[PATH TO YOUR API KEY.json]"
set GOOGLE_APPLICATION_CREDENTIALS=[PATH]
```
3. Run the program
```bash
python main.py
```
# Running Tests
Use images in __Images__ folder provided in repo and upload them to GUI and translate

# Usage
![Alt Text](http://g.recordit.co/rqF2EHBTAU.gif)

# Authors
* Denize Ignacio
* Mytzy Escalante
* Ankit Gulekar
* Roober Cruz

# Support 
Helpful Links: <br />
[Google Translator API Documentation](https://cloud.google.com/translate/docs/reference/libraries)

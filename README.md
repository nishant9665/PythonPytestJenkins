Jenkins JOB
Build -> Deploy -> Test -> Release

Build<Notification Feedback> Deploy<Notification>


How to set build pipeline:
1. download jenkins.war file
https://www.jenkins.io/download/

2.Check the java version.
C:\Users\user>java -version

Facing the java issue then set the java version in environment variable.
Check the location of java and set the path accordingly in environment

C:\Users\Mikel>where java

C:\Users\user>java -version
java version "23.0.1" 2024-10-15

Run the Jenkins war file by using the below command.

Java - jar <path of war file> like below.
C:\Users\user>java -jar C:\Nishant_Study\Software\jenkins.war

get this message at the end -
2024-12-06 08:03:07.219+0000 [id=35]    INFO    hudson.lifecycle.Lifecycle#onReady: Jenkins is fully up and running

Jenkins open -

use this below command -

Execute Windows batch command:

cd C:\Users\user\Desktop\Nishant\Python-Selenium\API-E2E Testing
cd TestCases
python Test3.py

Below are field need to complete the build.
New Item : entry any name
Select an item type : free style project

Install all dependency while facing the issue for executions-
pip install
pip install selenium
pip install pytest
pip install allure-pytest

Then run the command like :
pytest -v test_Login.py

-----------------------
This site can’t be reached

Means local host is not up and running so for that please apply below command.
this message only required- hudson.lifecycle.Lifecycle#onReady: Jenkins is fully up and running

Then open the local host :
<http://localhost:8080/login?from=%2F>
Userid : xxx
Password :xxxx

jenkins cmd run-->


cd C:\Nishant_Study\PythonJenkinsPytest\operations
pytest -v -s test_Login.py
-----------------------

or create a new repository on the command line
echo "# PythonPytestJenkins" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/nishant9665/PythonPytestJenkins.git
git push -u origin master

-----------------------------------

…or push an existing repository from the command line
git remote add origin https://github.com/nishant9665/PythonPytestJenkins.git
git branch -M main
git push -u origin main
-------------------------------------------



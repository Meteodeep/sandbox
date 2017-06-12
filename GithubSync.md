Part 1: Setting it up first time:
-Install git        (Bits you need to type are colour in red. Don’t include “ ”)
sudo apt-get install git  (it may already be installed)
git config --global user.name "username"
git config --global user.email "your_email@example.com"


-Make a folder that will sync up with github. Maybe name it after your group.
mkdir “name of folder”
   eg. mkdir gitalpha


-Open that folder (change the directory “cd” to the new folder)
cd “name of that folder you just made”
  eg. cd gitalpha

-Add invisible git files to the folder so that GitHub can link to it
git init
-Tell your Pi where where to find your group’s repository online. Find the address of the git by opening it on github and clicking “Clone or download”. In yellow.
git remote add origin https://github.com/”username”/”repo name”.git
   eg. git remote add origin https://github.com/STJRush/rpi.git
Part 2: Everyday use (pushing and pulling)
How to move files from Github->Pi
-Pull down the latest copy of the your files from Github onto your Raspberry Pi:
git pull origin master

How to move files from Pi->Github
-Add files to prepare a commit (a save)
git add .


-Commit changes with a -message. Do include the “” marks.
git commit -m "my message to explain the change"
eg. git commit -m "fixed a bug with elif, else"

-Push your changes up to the master branch on Github.
git push origin master
-You’ll be asked for your username and password to be sure that you have access to change the online repository.
-BONUS: You don’t have to use the master branch. All of the above can be done with your own branches. 

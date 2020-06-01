# Pickling and Stuctured Error Handling
## Introduction
In this assignment, we are asked to create a script that demonstrates how pickling and structured error handling are implemented in Python. In the first part of the script, I will explain how pickling can be used to store data on a .dat file in binary format and then loaded from a .dat file and converted into its original readable format. In the second part of the script, I will explain how structured error handling can be used to trap errors in the program and relay them back to the user. 
## Pickling
Pickling is a technique that allows us to preserve data in binary format as opposed to storing it as “plain text”. Python.org defines pickling as “implementing binary protocols for serializing and de-serializing a Python object structure.” The main benefits of pickling are the ability to store more complex data (relative to text files) with a single line of code and reducing its storage size. Figure 1 below shows the code in the data and processing layers of the script:

Figure 1

![Figure 1]( https://github.com/shpy086/IntroToProg-Python-Mod07/blob/master/Figure1.png)

In the data layer, I declare the two variables that we will be using: the first is the .dat file and the second is the list object that will be stored in the file. In the processing layer of the code, we have created two functions that that will be used to manipulate the user’s data. The first function will write the data to a .dat file in binary code. The second function will read binary code from the .dat file and convert it back to readable format. 

In the third and final layer of the script, the presentation layer, the user is prompted to enter data which establishes two more variables: “sport” and “team”. Once the user inputs both pieces of data, the program calls the “save data to file” function store the data as a list object in the .dat file. Then, the program calls the “read data from file” function to read data from the .dat file and print its result. Figure 2 below shows the presentation code:

Figure 2

![Figure 2](https://github.com/shpy086/IntroToProg-Python-Mod07/blob/master/Figure2.png)

When running the script in PyCharm, it executes the script successfully. In this case, when the user is prompted to enter a sport, they input “football” and when prompted to enter a team, they input “Giants”. When the two are combined, they form a list object. The sport is the category of the list object and the team is one of the teams within that category. Figure 3 below shows the script running in PyCharm:

Figure 3

![Figure 3]( https://github.com/shpy086/IntroToProg-Python-Mod07/blob/master/Figure3.png) 

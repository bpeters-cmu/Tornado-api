# Tornado-api
## Instructions for running tic-tac-toe api
Save Dockerfile and docker-compose.yml in the same directory and run using **_docker-compose up_**

API documentation can be found here: https://tictactoe11.docs.apiary.io/#

or here: https://github.com/bpeters-cmu/Tornado-api/blob/master/apiary.apib

Tornado is configured to listen on port 80

This application is also currently running on AWS and can be accessed at <ip> 
  
## Gameplay
The tic-tac-toe board is represented by a list data structure, with 1 representing X and 0 representing O

The positional layout of the board is as follows:

                                            0 | 1 | 2

                                            3 | 4 | 5

                                            6 | 7 | 8

Players are automatically assigned X or O and take turns based on the "nextTurn" field returned in the "Get Game By ID" api

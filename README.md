Project Summary/Overview

A simple API endpoint expecting a user to enter a string. Re-orders the string into an array of characters. And returns the transformed string as JSON.
This was completed by Edward Mawela as a job application to the IT/Tech company, 'One Eleven'

Live Demo at this URL : 
https:\\word-transformer-one-eleven.up.railway.app

API Endpoint:
https:\\word-transformer-one-eleven.up.railway.app/transform
API Usage:
POST /transform

Request body example:
{"data": "example"}
Response:
{"word": ["a", "e", "e", "l", "m", "p", "x"] } 

Note/Edge-Cases:
- 
-Input is processed literally as a string.
-Control characters are escaped according to JSON specification.
-Intended input is a simple word of alphabetical characters.
-The Transformation uses the Python function 'sorted()'...so expect behaviour in alignment with ASCII modeling.

Deployment
Deployed on Railway using FastAPI .

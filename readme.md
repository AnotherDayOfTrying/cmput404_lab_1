# CMPUT 404 - LAB 1

## Question 1: What is your GitHub URL?

https://github.com/AnotherDayOfTrying

## Question 2: What version is the requests library installed on the system?

2.31.0

## Question 3: What version is the requests library installed in the virtualenv?

2.31.0

## Question 4: What is the difference between the virtual environment and the not virtual environment python?

No difference. Both the virtual env and local env have the same version b/c the latest were installed in both. If a different version was installed in the virtual env then the virtual env, if activated, would have a different version of the requests package. A virtual environment allows packages to be project-specific.

## Question 5: What status code is returned for http://google.com ? What URL must you visit to get a 200 status code?

Status Code: 301
You must visit the URL `http://www.google.com/` to get a 200 status code. The URL is found from looking at the location header.

## Question 6: What status code is returned for http://google.com/teapot? Is it the one returned by curl -i or curl -iL? What happens when you curl http://www.google.com/teapot?

Status Code http://google.com/teapot: 301 -> `-i` -> 301 -> `-iL` -> 418
`-i` includes the headers in the response
`-iL` includes the headers and performs the redirection

Status Code http://www.google.com/teapot: 418
Note: this is the same response given from the command curl -iL http://google.com/teapot as http://www.google.com/teapot is the location that curl redirects towards when using `-iL`

## Question 7: What changed in the output of https://webdocs.cs.ualberta.ca/~hindle1/1.py when you used -X POST? What is this method useful for?

Populated form fields with the provided payload (X=Y). Included new headers `CONTENT_LENGTH`, `CONTENT_TYPE`. Shell Environment `REMOTE_PORT` (57012 -> 57048), `REQUEST_METHOD` ('GET' -> 'POST')
Useful for analyzing any requests coming towards the endpoint.

## Question 8: What is the raw URL to your Python script on GitHub?

https://raw.githubusercontent.com/AnotherDayOfTrying/cmput404_lab_1/main/lab_1.py

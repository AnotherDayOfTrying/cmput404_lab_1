Question 1: What is your GitHub URL?

https://github.com/AnotherDayOfTrying

Question 2: What version is the requests library installed on the system?

2.31.0

Question 3: What version is the requests library installed in the virtualenv?

2.31.0

Question 4: What is the difference between the virtual environment and the not virtual environment python?

No difference. Both the virtual env and local env have the same version b/c the latest were installed in both. If a different version was installed in the virtual env then the virtual env, if activated, would have a different version of the requests package.

Question 5: What status code is returned for http://google.com ? What URL must you visit to get a 200 status code?

Status Code: 301
http://www.google.com/ from location header

Question 6: What status code is returned for http://google.com/teapot? Is it the one returned by curl -i or curl -iL? What happens when you curl http://www.google.com/teapot?

Status Code http://google.com/teapot: 301 -> `-i` -> 301 -> `-iL` -> 418

Status Code http://www.google.com/teapot: 301

Question 7: What changed in the output of https://webdocs.cs.ualberta.ca/~hindle1/1.py when you used -X POST? What is this method useful for?

Populated form fields. Useful for analyzing any requests.

Question 8: What is the raw URL to your Python script on GitHub?



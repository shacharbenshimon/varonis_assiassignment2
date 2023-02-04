API testing-

Dependencies-
Make sure you have installed all the requirements
(which are in the requirements.txt file).

In 'tests' directory there are the API's tests.
The last 2 tests fails because of the following reasons-
1- GET method to /api/poly/<object_id> - returns the entire object list and not just the specific
 requested object.
2- DELETE method to /api/poly/<object_id> -returns that delete method is not allowed in /api/poly
 and does not return 204 as an answer as expected.
3- POST method to /api/poly	-
 the params - {"data": [{"key": "key1", "val": "val1", "valType": "int"}]} return 200 OK although "val1" isn't int.

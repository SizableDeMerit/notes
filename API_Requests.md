#api query examples
1. Query Parameters:
   GET https://api.example.com/data?key1=value1&key2=value2

2. Request Body (JSON for a POST request):
   POST https://api.example.com/users
   Body:
   {
       "username": "example_user",
       "email": "user@example.com"
   }

3. HTTP Headers (Authorization example):
   GET https://api.example.com/sensitive-data
   Headers:
   Authorization: Bearer <token>

4. URL Path Parameters:
   GET https://api.example.com/users/{userID}

5. HTTP Methods (Verbs):
   DELETE https://api.example.com/users/123

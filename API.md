# Documentation for API Call

- URL
    /api/v1/predict
- Method: POST
- Data Params
    - message=[str]
- Success Response
    Code: 200
    Content: `"ham\n"`
- Sample Call
    `curl -X POST -d "message=I'm on the way home, be there in fifteen." http://127.0.0.1:5000/api/v1/predict`
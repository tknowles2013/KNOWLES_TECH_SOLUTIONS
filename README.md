# KNOWLES_TECH_SOLUTIONS
KNOWLES_TECH_SOLUTIONS


Challenge 1

Leverage the Random User Generator API (https://randomuser.me) to create user data which you will sort and store into separate files.

 

Specifications

    Please commit your answer to a GitHub repository.
    Retrieve data for 100 random users from only the United States and Germany, and the United Kingdom. Your code should retrieve this data from a single API request. The response format should be in JSON.
    Output the response into a file that should be committed with the rest of your code.
    Using January 1, 1990 as a midpoint, divide and sort the 100 responses into two csv files based on the users’ birthdates.
    Create one CSV file that contains all American males born after January 1, 1980.
    The output csv files should have descriptive file names and contain column headers.

 

 

Challenge 2

Collect unstructured data from www.motionpoint.com, analyze the data and store it in a file.

 

Specifications

    Please commit you answer to a GitHub repository.
    The results should be stored in a CSV file with a unique file name and column headers.
    Starting at www.motionpoint.com, Extract and store content from the following HTML elements:
        <title></title>
        <meta name="description">
    In addition to the above elements, you should also store the URL where this information was retrieved.
    Create and store meta data that measures the length of the extracted contact.
    Leveraging HREFs found on the starting URL, collect the same information from 4 additional URLs without collecting information from the same URL multiple times.

Limitations

There should be a 5 second delay between each page request.

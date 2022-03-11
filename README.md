# arabic-dialect
## This project to calssify 17 arabic dialect.
________________________
I have data that include 2 columns (ids and dialect) and [API](https://recruitment.aimtechnologies.co/ai-tasks) to downlaod texts from it.
I worked in four steps we will see it.
### 1) [Data fetching from API](https://github.com/AntoniosMalak/arabic-dialect/blob/main/data_fetching.ipynb)
- First condition: The request body must be a JSON as a list of strings, and the size of the list must NOT
exceed 1000
- Second condition: The API will return a dictionary where the keys are the ids, and the values are the text, here
is a request and response.
Because of these conditions we have data with 458197 rows so we worked in these steps........
  - Collect ids astype string in a list.
  - Split ids into two lists.
    - list_1000 => this is a list with length 485 of lists every list on it with length 1000 here we collect (485000).
    - list_197  => this is a single list with length 197.
    at last, we make 2 lists contain all ids.
  - Make a request for 2 lists to fetch all texts.
  - Collect ids and texts into DataFrame.
  - See if we have missing data we don't fetch.
  - Save data as `Data/collected_data.csv`

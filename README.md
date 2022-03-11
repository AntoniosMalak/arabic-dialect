# arabic-dialect
## This project to calssify 17 arabic dialect.
________________________
I have `collected_data.csv` that include 2 columns (ids and dialect) and [API](https://recruitment.aimtechnologies.co/ai-tasks) to downlaod texts from it.
I worked in four steps we will see it.<br>
### 1) [Data fetching notebook from API](https://github.com/AntoniosMalak/arabic-dialect/blob/main/data_fetching.ipynb)
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

### [Data pre-processing notebook](https://github.com/AntoniosMalak/arabic-dialect/blob/main/data_pre-processing.ipynb)
- I worked in the same way as mention in [`Aim Technologies blog`](https://aimtechnologies.co/arabic-sentiment-analysis-blog.html?fbclid=IwAR0hlfhCOqd2xpJ3sGUb8yJbN0MzMq4dPPe6swuXwtdbCx1Mrn2I2wei3AM) to prepossing Arabic texts. 
    1 - `Normalizing similar characters` for example: (أ,إ,ا) should all be (ا).
    2 - `Removing tashkeel` for example (“وَصيَّة”) should be (“وصية”).
    3 - `Normalizing mentions and links to a standard form` for example: (@vodafone سعر الباقة كام؟) should be (XmentionX سعر الباقة كام؟).
    4 - `Removing unnecessary or repeated punctuation or characters` for example: (!!! جداااااا) should be (! جدا).
- Collect preprocessing texts in processed_text column in data.
- Save data as `processed_data.csv`

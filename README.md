# arabic-dialect
## This project to calssify 17 arabic dialect.
________________________
I have `dialect_dataset.csv` that include 2 columns (ids and dialect) and [API](https://recruitment.aimtechnologies.co/ai-tasks) to downlaod texts from it.
There are 4 steps as mentioned below.<br>
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

### 2) [Data pre-processing notebook](https://github.com/AntoniosMalak/arabic-dialect/blob/main/data_pre-processing.ipynb)
- I worked in the same way as mentioned in [`Aim Technologies blog`](https://aimtechnologies.co/arabic-sentiment-analysis-blog.html?fbclid=IwAR0hlfhCOqd2xpJ3sGUb8yJbN0MzMq4dPPe6swuXwtdbCx1Mrn2I2wei3AM) to prepossessing Arabic texts and add some prepossessing. <br>
    1 - `Normalizing similar characters` for example: (أ,إ,ا) should all be (ا). <br>
    2 - `Removing tashkeel` for example (“وَصيَّة”) should be (“وصية”). <br>
    3 - `Normalizing mentions and links to a standard form` for example: (@vodafone سعر الباقة كام؟) should be (XmentionX سعر الباقة كام؟).<br>
    4 - `Removing unnecessary or repeated punctuation or characters` for example: (!!! جداااااا) should be (! جدا).<br>
    5 - `Removing English words and numerical` for example: my name is انطونيوس ملاك 55457 should be (انطونيوس ملاك). <br>
- Collect prepossessing texts in processed_text column in new data include columns (ids, text, dialect, processed_text)
- Save data as `processed_data.csv`

### [Model Training notebook](https://github.com/AntoniosMalak/arabic-dialect/blob/main/model_training.ipynb)
Here we built classification models and Deep learning model.
- classification models:
  - Load data and split it and build methods that can help.
    - **text_fit_predict_without_imbalanced** method to predict more than techniques with original data.
    - **text_fit_predict_with_imbalanced** method to predict more than techniques with resample techniques because dialect column are different, the biggest one is EG with 57636 rows and the lowest one is TN with 9246 rows.

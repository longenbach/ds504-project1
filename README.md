# ds504-project1

crawler.py is used for get the details of a product through Walmart open API.

Pre-requirement:
requests

## Usage for collecting "ground truth"
Edit "collectdata.py" script:
1. Add your own Walmart API key
2. Change START and END to be your own range of exhaustive search (Min=1, Max=100000)
  (You are also able to change COMPANY_UPC which is the manufacturer UPC (Default=885306))
3. Run collectdata.py.

## Usage of sampling with prefix digits
Edit "sampling_app.py" script:
1. Add two or three Walmart API keys
2. Change COMPANY_UPC if you want to query another manufacturer
3. Run sampling_app.py

#### The result file name will have a timestamp, so that you won't overwrite the same file. 

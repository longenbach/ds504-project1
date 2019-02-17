# ds504-project1

crawler.py is used for get the details of a product through Walmart open API.

Pre-requirement:
requests

## Usage
#### Please make sure you have installed requests
Edit "collectdata.py" script:
1. Add your own Walmart API key
2. Change START and END to be your own range of exhaustive search (Min=1, Max=1000000)
  (You are also able to change COMPANY_UPC which is the manufacturer UPC (Default=885306))
4. Run collectdata.py.

#### The result file name will have a timestamp, so that you won't overwrite the same file. 

#### Please pay attention to the number of queries allowed by API per day and per second

#### This code is used for collect "ground truth". You can change the code in genupc.py to perform our sampling method.

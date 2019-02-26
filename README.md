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
#### The result file name will have a timestamp, so that you won't overwrite the same file

## Usage of sampling with prefix digits (This part is not used anymore)
Edit "sampling_app.py" script:
1. Add two or three Walmart API keys
2. Change COMPANY_UPC if you want to query another manufacturer
3. Run sampling_app.py

## Usage of estimating valid products
Edit "sampling.py" script
1. Change the parameters of "sampling()" function at 60th line (in the main part)
(Parameters are number of iteration, total number of intervals, number of sampled intervals and number of fixed digits respectively)
2. Run sampling.py

#### Each time you run "sampling.py", the parameters and results are added into the file "test_param_result.json".
(I have run the code several times and results are in the "test_param_result.json" file)

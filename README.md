# dsp-service
DSP unit hosted in the cloud, powered by AWS Lambda. 

## AWS Lambda
The entirety of the DSP code is powered by a single Lambda function. 

## DSP Suites
The application will support custom DSP suites (i.e. choosing x, y, z DSP transforms to be applies sequentially). The DSP suite will be sent to AWS Lambda as a [list?] which will be parsed by the handler to construct the sequence of DSP transforms.

## Storage [tbd]
Raw and all subsequent signal stages will be stored in dynamoDB tables (or maybe something else)
Could also save suites 

## Auto mode [tbd]
Perhaps incorporate an "auto-mode" which would automatically choose a 

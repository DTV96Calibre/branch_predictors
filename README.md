# Introduction
This collection emulates branch predictors you'd find in a processor.
Predictions are represented as either `True`, as in the branch was or is
taken, or `False`, the branch wasn't or isn't taken. Where applicable, 
history is defined as an array of booleans representing branch outcomes
ordered such that the oldest value has the smallest index and the most
recent outcome has the largest index.


## Global
The global branch predictor attempts to memorize patterns of branch outcomes which it uses to make predictions. 

### Usage
First initialize the Branch Prediction Table (BPT) using 
`initializeBPT(historySize, initialValue=True)`. All values in the BPT are
set to `initialValue` upon initialization. Use `getPrediction(history)`
and `setPrediction(prediction, history)` to access the BPT and make
predictions or set branch outcomes.

`getIndex(history)` can be used to see where a given history is being
mapped to. `getBPT()` returns the BPT array.


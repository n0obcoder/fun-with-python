# MOOD_TAG Classification of Songs

## Training
Training script can be easily run by using the train.py file and passing in the  training.csv file in the command-line llke the way it is shown below.
```
python train.py training.csv
```

## Testing
Testing script can be run by using the eval.py file and passing in the evaluation.py file and the model path (lgbm.pkl by default) in the command-line.
```
python eval.py evaluation.csv lgbm.pkl
```
Once this script is run succcessfully, it will automatically generate evaluation_classified.csv woth a 'MOOD_TAG' columns containing all the predictions in it.

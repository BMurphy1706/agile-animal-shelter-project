# Data reformatting library

## Removal

- As seen in the remove.py file, code is present for dropping columns in both the intakes and outcomes tables
- I have also included the dataset again as a means of testing

## Adding

- Although not necessarily adding new data, a library named add has been created as a means of adding the two rows for the animals gender and if they have been neutered/spayed
- These have been separated as one can infer if it has been "neutered" or "spayed" depending on the animals gender and those who cannot be identified can be assumed as having been intact

## Main file

- Adding a main output file, showing the process by which the csv files are parsed into a pandas dataframe and the library code is applied onto them until they are fully reformatted

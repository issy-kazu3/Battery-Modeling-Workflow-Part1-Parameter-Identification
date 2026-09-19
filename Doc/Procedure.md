## 1) Data Trimming

The raw test data contain SOC adjustment periods and other sections that are not suitable for parameter identification.
 
Since manually removing these data is tedious and error-prone, a Python script was developed to automatically extract only the relevant regions required for parameter identification.
![raw](https://github.com/issy-kazu3/Battery-Modeling-Workflow-Part1-Parameter-Identification/blob/main/images/pulsed_data.png)
![trimmed](https://github.com/issy-kazu3/Battery-Modeling-Workflow-Part1-Parameter-Identification/blob/main/images/extracted_pulsed.png)

 
As a preprocessing step, the initial SOC adjustment section was removed, and the OCV value for each SOC condition was added manually.
 
## 2) Parameter Identification (Ri, Rp, C)


Using the processed data, another Python program was developed to identify the equivalent circuit model parameters (Ri, Rp, and C) for each SOC condition.
 
The resulting parameter set is shown below.
 
RMSE was used as an error metric. Data sets with exceptionally large RMSE values were considered outliers and excluded from further analysis.
 
## 3) Cell Characteristic Map Generation
 
Finally, the identified parameters were organized into tables according to SOC and charge/discharge operating mode.
 
This process produced the cell characteristic map shown below.
 
In the next article, the extracted parameters will be used to perform battery simulation and compare the results with measured data.
``

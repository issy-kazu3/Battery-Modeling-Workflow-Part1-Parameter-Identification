#20260727 from 10sec pulse charge discharge CSV data,extract pulse part data.
import pandas as pd

csv_path=r"D:\Userarea\J0125789\Documents\Python_code\battery"
input_file=csv_path+r"\10_sec_pulse_test_raw_data_60degC.csv"
output_file=csv_path+r"\result.csv"
df=pd.read_csv(input_file,encoding="shift_jis")

mask=((df["status"]==r"CC charge") | (df["status"]==r"CC discharge")) & (df["Current [A]"].abs()>8)    #Extract condition

df_step=df[mask].copy()

if df_step.empty:
    print("No data which exceed 8A")

df_out=df_step[["Total Time","Step Time","Voltage [V]","Current [A]","Battery Temperature [°C]","Chamber Temperature [°C]"]]
df_out.to_csv(output_file,index=False,encoding="shift_jis")
print("Extraction finished:",output_file)



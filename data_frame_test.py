import pandas as pd
import numpy as np
import re

d = {'_id': [1, 2, 3, 4, 5, 6, 7],
'column1': ['FullName', 'custfullnm', 'nm123', 'sitenm', 'full12', 'suplnm', 'countryfull'],
'column2': ['', '', '', '', '', '', '']}
df = pd.DataFrame(data=d)

key_words = ["full", "nm", "name", "txt", "[0-9]"]
check = f"{'|'.join(key_words)}"
mand_key = "full"

df["column2"] = np.where(
    df.column1.str.contains(mand_key, flags=re.IGNORECASE)
    & df.column1.str.match(check, flags=re.IGNORECASE),"Full Name","",)

print(df)


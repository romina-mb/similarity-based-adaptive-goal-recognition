##_______________________________ code 2 _______________________________##

import pandas as pd
import glob
import os

##------------------------------gradual drift------------------------------------##
parent_folder = 'final results/sys evaluation_grd_ol' 
output_file = 'final results/merged_summary_grd.csv'

##------------------------------re-occurring drift------------------------------------##
# parent_folder = 'final results/sys evaluation_oc_ol' 
# output_file = 'final results/merged_summary_oc.csv'

##------------------------------sudden drift------------------------------------##
# parent_folder = 'final results/sys evaluation_sud_ol' 
# output_file = 'final results/merged_summary_sud.csv'


target_filename = 'compare.csv'


# Find all files with matching names
all_summary_files = glob.glob(os.path.join(parent_folder, '**', target_filename), recursive=True)

# Collection and combination
df_list = []
for file in all_summary_files:
    df = pd.read_csv(file)
    
    # df['SourceFile'] = os.path.basename(file)
    df['DomainFolder'] = os.path.basename(os.path.dirname(file))  # Registers the parent folder as a domain.
    df_list.append(df)

merged_df = pd.concat(df_list, ignore_index=True)
merged_df.to_csv(output_file, index=False)

print(f"All summaries were saved in the file '{output_file}' successfully.")

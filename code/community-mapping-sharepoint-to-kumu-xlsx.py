
# This script reads in an xlsx file of stakeholder metadata and prepares a file for kumu mapping.
# Adapted from https://github.com/rcmcooperative/community-mapping/blob/main/code/sharepoint-to-kumu-xlsx.py
# Gould van Praag, C. (2025). RCM Cooperative Community Mapping Workflow. Zenodo. https://doi.org/10.5281/zenodo.15320348

# # Set-up in terminal
# Adapted from [TTW local build step-by-step guide](https://the-turing-way.netlify.app/community-handbook/local-build.html?highlight=conda%20env) to use a conda environment
# 1. [install miniconda](https://docs.conda.io/projects/miniconda/en/latest/)
# 2. `conda init`
# 3. `curl https://github.com/rcmcooperative/community-mapping/blob/main/DO-NOT-USE/kumu-env.yml` > kumu-env.yml
# 4. `conda env create -f kumu-env.yml`
# 5. `conda activate kumu_env`
# 6. in vs code, set python interpreter to kumu_env before running debugging (see [guide here](https://code.visualstudio.com/docs/python/environments#_using-the-create-environment-command))




# library of functions for checking, makeing, renaming files etc.
import os as os
import subprocess
# subprocess.run('source activate the-turing-way', shell=True)
# subprocess.run('pwd', shell=True)
# subprocess.run('pip install -r requirements.txt',shell=True)
# library for handelling data read in from the xlsx file
import pandas as pd
import numpy as np
import csv
from anonymizedf.anonymizedf import anonymize
import time
import json

# where all our data is
dataRoot = '/Users/cassandragouldvanpraag/Library/Mobile Documents/com~apple~CloudDocs/repos/rcmcooperative/partner-TOSI/private/community-map-data/'

sharepoint_date = '20251112'
filename_prefix = 'Community-List-'
filename_extension = '.csv'

filename_read_affiliations = filename_prefix+'Affiliations-'+sharepoint_date+filename_extension
filename_read_tools = filename_prefix+'Tools-'+sharepoint_date+filename_extension
filename_read_people = filename_prefix+'People-'+sharepoint_date+filename_extension
# For the purposes of mapping, we don't actually need to have the initiatives and interactions as elements, only as metadata for the people
# filename_read_interactions = filename_prefix+'Interactions-'+sharepoint_date+filename_extension
# filename_read_initiatives = filename_prefix+'Initiatives-'+sharepoint_date+filename_extension

timestr = time.strftime("-%Y%m%d-%H%M%S")

filename_write_internal = 'kumu-data-TOSI-processed-internal-'+sharepoint_date+timestr+'.xlsx'
path_write_internal = os.path.join(dataRoot,'kumu',filename_write_internal)

filename_write_public = 'kumu-data-es-processed-public-'+sharepoint_date+timestr+'.xlsx'
path_write_public = os.path.join(dataRoot,'kumu',filename_write_public)


path_read_affiliations = os.path.join(dataRoot,'sharepoint-list-downloads',filename_read_affiliations)
path_read_tools = os.path.join(dataRoot,'sharepoint-list-downloads',filename_read_tools)
path_read_people = os.path.join(dataRoot,'sharepoint-list-downloads',filename_read_people)
# path_read_interactions = os.path.join(dataRoot,filename_read_interactions) # Not working with interactions yet. Will need to incorporate this data into 'people' metadata


# csv file containing our index of scan IDs
# data_people = pd.read_excel(path_read,sheet_name='people')
data_people = pd.read_csv(path_read_people)
data_affiliations = pd.read_csv(path_read_affiliations)
data_tools = pd.read_csv(path_read_tools)
# data_interactions = pd.read_csv(path_read_interactions)

data_elements = pd.DataFrame()
data_connections = pd.DataFrame()

print(data_people)
print(data_affiliations)
print(data_tools)


# First column in each table is the entry name in sharepoint.
# Rename this "name-" column to "label", which is what kumu needs to call its elements

data_people = data_people.rename(columns={'name-person': 'label'})
data_affiliations = data_affiliations.rename(columns={'name-affiliation': 'label'})
data_tools = data_tools.rename(columns={'name-tool': 'label'})
                                                
print(data_people)
print(data_affiliations)
print(data_tools)

# Column names are different across the lists. Need to merge them together so all data types have the same metadata fields.
# You need to merge on all the common columns and use outer join (https://stackoverflow.com/questions/42940507/merging-dataframes-keeping-all-items-pandas)
# pd.merge(df1, df2, on = ['Name', 'Parent', 'Parent_Addr'], how = 'outer')
# find unique column headers over all dfs


# (https://stackoverflow.com/questions/59940311/retrieve-unique-column-names-over-multiple-dataframes-and-append-all-to-a-list)
alldf = [data_people, data_affiliations, data_tools]
desiredlist = []
for index, dataframe in enumerate(alldf):
    a = dataframe.columns.values.tolist()
    for column_name in a:
        if not column_name in desiredlist:
            desiredlist.append(column_name)

# combine data for "elements" tab
data_elements = pd.merge(data_people,data_affiliations, on = 'label', how = 'outer')
data_elements = pd.merge(data_elements,data_tools, on = 'label', how = 'outer')

data_elements.columns = data_elements.columns.str.rstrip('_x')  # strip suffix at the right end only.
data_elements.columns = data_elements.columns.str.rstrip('_y')  # strip suffix at the right end only.

def sjoin(x): return ';'.join(x[x.notnull()].astype(str))
data_elements = data_elements.groupby(level=0, axis=1).apply(lambda x: x.apply(sjoin, axis=1))

# move 'label' to first column
# (https://stackoverflow.com/questions/25122099/move-column-by-name-to-front-of-table-in-pandas)
cols = list(data_elements)
# move the column to head of list using index, pop and insert
cols.insert(0, cols.pop(cols.index('label')))
# use ix to reorder
data_elements = data_elements.loc[:, cols]


# Kumu: If you want to store multiple values inside of one cell (for example, tags or keywords), 
# just separate each value with the pipe character |. 

data_elements['affiliation'] = data_elements['affiliation'].str.replace(',','|')
data_elements['tool-developer'] = data_elements['tool-developer'].str.replace(',','|')
data_elements['initiative-leadership'] = data_elements['initiative-leadership'].str.replace(',','|')
data_elements['initiative-participant'] = data_elements['initiative-participant'].str.replace(',','|')
data_elements['interaction-leadership'] = data_elements['interaction-leadership'].str.replace(',','|')
data_elements['interaction-participant'] = data_elements['interaction-participant'].str.replace(',','|')
data_elements['interaction-speaker'] = data_elements['interaction-speaker'].str.replace(',','|')
data_elements['funding-recipient'] = data_elements['funding-recipient'].str.replace(',','|')
data_elements['funding-applicant'] = data_elements['funding-applicant'].str.replace(',','|')

# Count the number of engagements
cols_engagement = ['initiative-leadership', 'initiative-participant','interaction-leadership','interaction-participant','interaction-speaker','funding-recipient','funding-applicant']

count_engagement = pd.DataFrame()
for col in cols_engagement:
    # Condition 1: Check for standard nulls (None, NaN)
    is_null = data_elements[col].isnull()
    # Condition 2: Check for empty strings, whitespace, or the specific string "[]"
    as_string = data_elements[col].astype(str)
    # Check for empty strings or strings composed only of whitespace
    is_effectively_blank = as_string.str.strip().eq('') 
    # Check for the specific excluded string "[]"
    is_excluded_string = (as_string == '[]')
    
    # The FINAL combined exclusion:
    is_excluded = is_null | is_effectively_blank | is_excluded_string
    
    # Condition 2 (Pipes): True if the string contains one or more pipes
    contains_pipe = data_elements[col].astype(str).str.contains('\|', na=False)
    
    # The value to use if pipes are found (N+1 logic)
    pipe_count_plus_one = data_elements[col].str.count('\|') + 1

    # --- Step B: Apply Nested Conditional Logic ---
    
    count_engagement[f'{col}_Item_Count'] = np.where(
        # PRIORITY 1: Check for Exclusions
        is_excluded,
        0, 
        # If not excluded, move to the next check:
        np.where(
            # PRIORITY 2: Check for Pipes
            contains_pipe,
            pipe_count_plus_one, # If pipes, use N+1 count
            # PRIORITY 3: Must be a non-excluded, single item
            1 
        )
    )

# 2. Sum the row-wise item counts to get the final total
data_elements['engagement-count-total'] = count_engagement.sum(axis=1)


# create a new column "type-what" as a copy of "type" for kumu filtering (kumu doesn't seemto like to work with "type" alone for colour etc. )
# data_elements['type-what'] = data_elements.loc[:, 'type']
# think this is now fixed by labeling the column "kumu-type"

# # reorder columns so they are logical in kumu
# def swap_columns(df, col1, col2):
#     col_list = list(df.columns)
#     x, y = col_list.index(col1), col_list.index(col2)
#     col_list[y], col_list[x] = col_list[x], col_list[y]
#     df = df[col_list]
#     return df

# col_order = pd.Series(data_elements.columns)
# print(col_order)

# fix_cols = input("do you need to update the colomn order? (enter 0 or col number to by updated):")
# while int(fix_cols) > 0:
#     i = int(fix_cols)
#     # ask which column you want in position i
#     inputq = "what do you want in col" + str(i) + "? (type current index number):"
#     x = int(input(inputq))
#     # get the name of the col in position i
#     col_new = col_order.iloc[x]
#     # get the name of the column cirrently in position i
#     col_old = col_order.iloc[i]
#     # swap _old with _new
#     data_elements = swap_columns(data_elements, col_old, col_new)
#     col_order = pd.Series(data_elements.columns)
#     print(col_order)
#     fix_cols = input("do you need to update the colomn order? (enter 0 or col number to by updated):")
# kumu actually puts them up in any old order, so this never worked


# create a new column "type-what" as a copy of "type" for kumu filtering
# data_elements['type-what'] = data_elements.loc[:, 'type']

# Check if there is a column 'ID' and remove it if there is, as kumu creates a column called ID and it get's upset! 
if 'ID' in data_elements.columns:
    data_elements = data_elements.drop('ID', axis=1)
else:
    print("Column 'ID' does not exist.")



####################

# Now handel the connections!!!

data_people['affiliation'] = data_people['affiliation'].str.replace(',','|')
# data_people['tool-user'] = data_people['tool-user'].str.replace(',','|')
data_people['tool-developer'] = data_people['tool-developer'].str.replace(',','|')

# data_people['workstreams'] = data_people['workstreams'].str.replace(',','|')
# data_people['workstreams'] = data_people['workstreams'].str.replace('"','')
# data_people['workstreams'] = data_people['workstreams'].str.replace('[','')
# data_people['workstreams'] = data_people['workstreams'].str.replace(']','')

# print(data_people[['affiliations']].to_string(index=False)) 
# print(data_people[['affiliations-turing']].to_string(index=False)) 
# print(data_people[['projects']].to_string(index=False)) 
# print(data_people[['workstreams']].to_string(index=False)) 

# Kumu: If you put multiple elements in the "To" cell of a connection, separating each element with the pipe character |, 
# Kumu will draw a connection from the "From" element to each separate element in the "To" cell. (https://docs.kumu.io/guides/import/import)

# concatenate the affiliations and projects if not empty
# data_people['to'] = data_people[['affiliations', 'affiliations-turing', 'projects']].apply(lambda x: ','.join(x.dropna()), axis=1)
# data_people['to'] = data_people[['affiliation', 'tool-user', 'tool-developer']].apply(lambda x: ','.join(x.dropna()), axis=1)
data_people['to'] = data_people[['affiliation', 'tool-developer']].apply(lambda x: ','.join(x.dropna()), axis=1)

# replace ',' in 'to' with |
data_people['to'] = data_people['to'].str.replace(',[]','')
data_people['to'] = data_people['to'].str.replace(',','|')
data_people['to'] = data_people['to'].str.replace('[]|','')

# rename 'label' to 'from'
data_people = data_people.rename(columns={'label': 'from'})
# keep only 'from' and 'to'
data_people = data_people[['from', 'to']]
# add 'direction' column ("undirected")
data_people['direction'] = 'undirected'


# DO IT ALL AGAIN FOR CONNECTIONS FOR AFFILIATIONS AND TOOLS

# 1. Merge affiliations
data_affiliations['affiliation'] = data_affiliations['affiliation'].str.replace(',','|')
data_tools['affiliation'] = data_tools['affiliation'].str.replace(',','|')

# 2. rename 'label' to 'from'
data_affiliations = data_affiliations.rename(columns={'label': 'from'})
data_tools = data_tools.rename(columns={'label': 'from'})

# 3. rename 'affiliation' to 'to'
data_affiliations = data_affiliations.rename(columns={'affiliation': 'to'})
data_tools = data_tools.rename(columns={'affiliation': 'to'})

# 4. keep only 'from' and 'to'
data_affiliations = data_affiliations[['from', 'to']]
data_tools = data_tools[['from', 'to']]

# 5. add 'undirected'
data_affiliations['direction'] = 'undirected'
data_tools['direction'] = 'undirected'

# COMBINE ALL THE CONNECTIONS

frames = [data_people, data_affiliations, data_tools]
data_connections = pd.concat(frames)
data_connections = data_connections.reset_index(drop=True)

# replace NaN in 'to' with '[]'
data_connections['to'] = data_connections['to'].fillna('[]')

#fix some column names
data_elements.rename(columns={'Created': 'created-date'}, inplace=True)
data_elements.rename(columns={'Created B': 'created-by'}, inplace=True)
data_elements.rename(columns={'Modified': 'modified-last-date'}, inplace=True)
data_elements.rename(columns={'Modified B': 'modified-last-by'}, inplace=True)
# data_elements.rename(columns={'countr': 'country'}, inplace=True)

# fix the sizes
# data_elements.loc[data_elements['type-what'] == 'Person', 'size'] = 1
# data_elements.loc[data_elements['type-what'] == 'Research insitute', 'size'] = 100
# data_elements.loc[data_elements['type-what'] == 'Public sector / Government body', 'size'] = 20
# data_elements.loc[data_elements['type-what'] == 'Private industry', 'size'] = 20
# data_elements.loc[data_elements['type-what'] == 'Non-profit', 'size'] = 20
# data_elements.loc[data_elements['type-what'] == 'Consortium', 'size'] = 35
# data_elements.loc[data_elements['type-what'] == 'Turing programme', 'size'] = 20
# data_elements.loc[data_elements['type-what'] == 'Project', 'size'] = 50
# This now all done in sharepoint





print('writing data to:' + path_write_internal)
with pd.ExcelWriter(path_write_internal) as writer:
    # use to_excel function and specify the sheet_name and index 
    # to store the dataframe in specified sheet
    data_elements.to_excel(writer, sheet_name="elements", index=False)
    data_connections.to_excel(writer, sheet_name="connections", index=False)
print('writing xlsx data for internal map - complete')    


####################
# Do anonymisation
####################

an = anonymize(data_elements)
an.fake_ids("label")

data_elements_anon = data_elements

data_elements_anon.rename(columns={'Fake_label': 'label-anon'}, inplace=True)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# if kumu-type not = "person" set kumu-consent to "consent-public"
data_elements_anon.loc[data_elements_anon['kumu-type'] != 'person', 'kumu-consent'] = 'consent-public-identifiable'

# if kumu-type == "person" and kumu-consent == []; kumu-consent = "consent-none"
data_elements_anon.loc[(data_elements_anon['kumu-type'] == 'person') & (data_elements_anon['kumu-consent'] == ''), 'kumu-consent'] = 'consent-none'

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# # Select the specified columns and assign them to a new DataFrame
elements_consent_lookup = data_elements_anon[['label', 'kumu-consent', 'label-anon','kumu-type']].copy()


data_connections_anon = data_connections[['from', 'to', 'direction']].copy()
data_connections_anon['label-public'] = np.nan


df1 = data_connections_anon
df2 = elements_consent_lookup


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# # Loop through df1 and find matching values in df2
for index, row in df1.iterrows():
    print(index)
    print(df1.iloc[index]) #df1.at[index, 'label-public']
    if index == 835:
        print(df1.iloc[835])
    id_value = row['from']
    matching_row = df2[df2['label'] == id_value]
    if not matching_row.empty:
        if matching_row['kumu-consent'].values[0] == 'consent-none':
            print("Matching value in df2 for id", id_value, ":", "Consent is none")
            # Add the 'Fake-label' value to df1
            df1.at[index, 'label-public'] = matching_row['label-anon'].values[0]
        elif matching_row['kumu-consent'].values[0] == 'consent-public':
            print("Matching value in df2 for id", id_value, ":", "Consent is public")
            df1.at[index, 'label-public'] = matching_row['label'].values[0]
        elif matching_row['kumu-consent'].values[0] == 'consent-public-pseudonymised':
            print("Matching value in df2 for id", id_value, ":", "Consent is pseudonymised")
            df1.at[index, 'label-public'] = matching_row['label-anon'].values[0]
        else:
            print("Matching value in df2 for id", id_value, ":", "Consent is: ",matching_row['kumu-consent'].values[0])
    else:
        print("No matching value found in df2 for id", id_value)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

data_connections_anon = df1

# redact identifiable information from data_elements_anon where no consent
columns_identifiable = ['email', 'github', 'position', 'pronouns', 'url']
data_elements_anon.loc[data_elements['kumu-consent'] == 'consent-none', columns_identifiable] = np.nan

# delete opinion columns for everyone %**
columns_opinions = ['how-to-engage','influence-over-programme','interest-in-programme','moe-level','notes']
# **Decided to keep the initiatives and interactions for now as I'm not going to publish a public version, and these might actually be useful for the public filtering

data_elements_anon = data_elements_anon.drop(columns_opinions,axis=1)

# get rid of boring columns %**
columns_boring = ['created-date', 'created-by', 'modified-last-date', 'modified-last-by', 'url']
data_elements_anon = data_elements_anon.drop(columns_boring,axis=1)



# replace labels with label_anon where consent == none
data_elements_anon.loc[data_elements_anon['kumu-consent'] == 'consent-public-identifiable', 'label-anon'] = data_elements_anon['label']

# rename
data_elements_anon.rename(columns={'label-anon': 'label-public'}, inplace=True)

# delete the old "label" and "from", replace with the anonymised values
data_elements_anon = data_elements_anon.drop('label',axis=1)
data_elements_anon.rename(columns={'label-public': 'label'}, inplace=True)

data_connections_anon = data_connections_anon.drop('from',axis=1)
data_connections_anon.rename(columns={'label-public': 'from'}, inplace=True)

# and move the new ones to the first column (for kumu)
cols = list(data_elements_anon.columns)
cols.insert(0, cols.pop(cols.index('label')))
data_elements_anon = data_elements_anon[cols]

cols = list(data_connections_anon.columns)
cols.insert(0, cols.pop(cols.index('from')))
data_connections_anon = data_connections_anon[cols]

# write out
print('writing anonymised data to:' + path_write_public)
with pd.ExcelWriter(path_write_public) as writer:
    # use to_excel function and specify the sheet_name and index 
    # to store the dataframe in specified sheet
    data_elements_anon.to_excel(writer, sheet_name="elements", index=False)
    data_connections_anon.to_excel(writer, sheet_name="connections", index=False)
print('writing xlsx data for public map - complete')


# #################



# # %%%%%%%%%%%%%%%%%%%%%%%%%%%




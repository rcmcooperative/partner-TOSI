
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
dataRoot = '/Users/cgouldvanpraag/Library/CloudStorage/OneDrive-TheAlanTuringInstitute/E&S Grand Challenge - Documents/WS1 Ecosystem/stakeholder-mapping/data-sources/'

sharepoint_date = '20240228'
filename_prefix = 'stakeholder-list-E&S-'
filename_extension = '.csv'

filename_read_companies = filename_prefix+'companies-'+sharepoint_date+filename_extension
filename_read_projects = filename_prefix+'projects-'+sharepoint_date+filename_extension
filename_read_people = filename_prefix+'people-'+sharepoint_date+filename_extension
filename_read_interactions = filename_prefix+'interactions-'+sharepoint_date+filename_extension

timestr = time.strftime("-%Y%m%d-%H%M%S")

filename_write_internal = 'kumu-data-es-processed-internal-'+sharepoint_date+timestr+'.xlsx'
path_write_internal = os.path.join(dataRoot,'kumu',filename_write_internal)

filename_write_public = 'kumu-data-es-processed-public-'+sharepoint_date+timestr+'.xlsx'
path_write_public = os.path.join(dataRoot,'kumu',filename_write_public)


path_read_companies = os.path.join(dataRoot,'sharepoint-list-downloads',filename_read_companies)
path_read_projects = os.path.join(dataRoot,'sharepoint-list-downloads',filename_read_projects)
path_read_people = os.path.join(dataRoot,'sharepoint-list-downloads',filename_read_people)
# path_read_interactions = os.path.join(dataRoot,filename_read_interactions) # Not working with interactions yet. Will need to incorporate this data into 'people' metadata


# csv file containing our index of scan IDs
# data_people = pd.read_excel(path_read,sheet_name='people')
data_people = pd.read_csv(path_read_people)
data_companies = pd.read_csv(path_read_companies)
data_projects = pd.read_csv(path_read_projects)
# data_interactions = pd.read_csv(path_read_interactions)

data_elements = pd.DataFrame()
data_connections = pd.DataFrame()

print(data_people)
print(data_companies)
print(data_projects)


# First column in each table is the entry name in sharepoint.
# Rename to "label" for kumu

data_people = data_people.rename(columns={'name-person': 'label'})
data_companies = data_companies.rename(columns={'name-company': 'label'})
data_projects = data_projects.rename(columns={'name-project': 'label'})
                                                
print(data_people)
print(data_companies)
print(data_projects)

# Column names are different across the lists. Need to merge them together so all data types have the same metadata fields.
# You need to merge on all the common columns and use outer join (https://stackoverflow.com/questions/42940507/merging-dataframes-keeping-all-items-pandas)
# pd.merge(df1, df2, on = ['Name', 'Parent', 'Parent_Addr'], how = 'outer')
# find unique column headers over all dfs


# (https://stackoverflow.com/questions/59940311/retrieve-unique-column-names-over-multiple-dataframes-and-append-all-to-a-list)
alldf = [data_people, data_companies, data_projects]
desiredlist = []
for index, dataframe in enumerate(alldf):
    a = dataframe.columns.values.tolist()
    for column_name in a:
        if not column_name in desiredlist:
            desiredlist.append(column_name)

# combine data for "elements" tab
data_elements = pd.merge(data_people,data_companies, on = 'label', how = 'outer')
data_elements = pd.merge(data_elements,data_projects, on = 'label', how = 'outer')

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

data_elements['affiliations'] = data_elements['affiliations'].str.replace(',','|')
data_elements['affiliations-turing'] = data_elements['affiliations-turing'].str.replace(',','|')
data_elements['projects'] = data_elements['projects'].str.replace(',','|')
data_elements['interaction-participant-all'] = data_elements['interaction-participant-all'].str.replace(',','|')
data_elements['interaction-participant-active'] = data_elements['interaction-participant-active'].str.replace(',','|')
data_elements['interaction-participant-presenter'] = data_elements['interaction-participant-presenter'].str.replace(',','|')
data_elements['interaction-participant-leadership'] = data_elements['interaction-participant-leadership'].str.replace(',','|')

# data_elements['workstreams'] = data_elements['workstreams'].str.replace(',','|')
# data_elements['workstreams'] = data_elements['workstreams'].str.replace('"','')
# data_elements['workstreams'] = data_elements['workstreams'].str.replace('[','')
# data_elements['workstreams'] = data_elements['workstreams'].str.replace(']','')

# create a new column "type-what" as a copy of "type" for kumu filtering (kumu doesn't seemto like to work with "type" alone for colour etc. )
data_elements['type-what'] = data_elements.loc[:, 'type']

# reorder columns so they are logical in kumu
def swap_columns(df, col1, col2):
    col_list = list(df.columns)
    x, y = col_list.index(col1), col_list.index(col2)
    col_list[y], col_list[x] = col_list[x], col_list[y]
    df = df[col_list]
    return df

col_order = pd.Series(data_elements.columns)
print(col_order)

fix_cols = input("do you need to update the colomn order? (enter 0 or col number to by updated):")
while int(fix_cols) > 0:
    i = int(fix_cols)
    # ask which column you want in position i
    inputq = "what do you want in col" + str(i) + "? (type current index number):"
    x = int(input(inputq))
    # get the name of the col in position i
    col_new = col_order.iloc[x]
    # get the name of the column cirrently in position i
    col_old = col_order.iloc[i]
    # swap _old with _new
    data_elements = swap_columns(data_elements, col_old, col_new)
    col_order = pd.Series(data_elements.columns)
    print(col_order)
    fix_cols = input("do you need to update the colomn order? (enter 0 or col number to by updated):")


# create a new column "type-what" as a copy of "type" for kumu filtering
data_elements['type-what'] = data_elements.loc[:, 'type']

# drop the column 'ID' as kumu wan't to create that value itself.
data_elements = data_elements.drop('ID', axis=1)

####################

# Now handel the connections!!!

data_people['affiliations'] = data_people['affiliations'].str.replace(',','|')
data_people['affiliations-turing'] = data_people['affiliations-turing'].str.replace(',','|')
data_people['projects'] = data_people['projects'].str.replace(',','|')

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
data_people['to'] = data_people[['affiliations', 'affiliations-turing', 'projects']].apply(lambda x: ','.join(x.dropna()), axis=1)

# replace ',' in 'to' with |
data_people['to'] = data_people['to'].str.replace(',[]','')
data_people['to'] = data_people['to'].str.replace(',','|')
# replace 'Alan Turing Institute|Turing-' with 'Turing-'
# This was to make Turing affiliated people connected to their programme only. Think it's better to keep the direct Turing affiliation, for discoverability.
# data_people['to'] = data_people['to'].str.replace('Alan Turing Institute|Turing-','Turing-')

# rename 'label' to 'from'
data_people = data_people.rename(columns={'label': 'from'})
# keep only 'from' and 'to'
data_people = data_people[['from', 'to']]
# add 'direction' column ("undriected")
data_people['direction'] = 'undirected'


# DO IT ALL AGAIN FOR CONNECTIONS FOR COMPANIES AND PROJECTS

# 1. Merge affiliations
data_companies['affiliations'] = data_companies['affiliations'].str.replace(',','|')
data_projects['affiliations'] = data_projects['affiliations'].str.replace(',','|')

# 2. rename 'label' to 'from'
data_companies = data_companies.rename(columns={'label': 'from'})
data_projects = data_projects.rename(columns={'label': 'from'})

# 3. rename 'affiliations' to 'to'
data_companies = data_companies.rename(columns={'affiliations': 'to'})
data_projects = data_projects.rename(columns={'affiliations': 'to'})

# 4. keep only 'from' and 'to'
data_companies = data_companies[['from', 'to']]
data_projects = data_projects[['from', 'to']]

# 5. add 'undirected'
data_companies['direction'] = 'undirected'
data_projects['direction'] = 'undirected'

# COMBINE ALL THE CONNECTIONS

frames = [data_people, data_companies, data_projects]
data_connections = pd.concat(frames)
data_connections = data_connections.reset_index(drop=True)

# replace NaN in 'to' with '[]'
data_connections['to'] = data_connections['to'].fillna('[]')

#fix some column names
data_elements.rename(columns={'Created': 'created-date'}, inplace=True)
data_elements.rename(columns={'Created B': 'created-by'}, inplace=True)
data_elements.rename(columns={'Modified': 'modified-last-date'}, inplace=True)
data_elements.rename(columns={'Modified B': 'modified-last-by'}, inplace=True)
data_elements.rename(columns={'countr': 'country'}, inplace=True)

# fix the sizes
data_elements.loc[data_elements['type-what'] == 'Person', 'size'] = 1
data_elements.loc[data_elements['type-what'] == 'Research insitute', 'size'] = 100
data_elements.loc[data_elements['type-what'] == 'Public sector / Government body', 'size'] = 20
data_elements.loc[data_elements['type-what'] == 'Private industry', 'size'] = 20
data_elements.loc[data_elements['type-what'] == 'Non-profit', 'size'] = 20
data_elements.loc[data_elements['type-what'] == 'Consortium', 'size'] = 35
data_elements.loc[data_elements['type-what'] == 'Turing programme', 'size'] = 20
data_elements.loc[data_elements['type-what'] == 'Project', 'size'] = 50





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

# if type-what not = "person" set consent-kumu to "consent-public"
data_elements_anon.loc[data_elements_anon['type-what'] != 'Person', 'consent-kumu'] = 'consent-public'

# if type-what == "person" and consent-kumu == []; consent-kumu = "consent-none"
data_elements_anon.loc[(data_elements_anon['type-what'] == 'Person') & (data_elements_anon['consent-kumu'] == ''), 'consent-kumu'] = 'consent-none'

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# # Select the specified columns and assign them to a new DataFrame
elements_consent_lookup = data_elements_anon[['label', 'consent-kumu', 'label-anon','type-what']].copy()


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
        if matching_row['consent-kumu'].values[0] == 'consent-none':
            print("Matching value in df2 for id", id_value, ":", "Consent is none")
            # Add the 'Fake-label' value to df1
            df1.at[index, 'label-public'] = matching_row['label-anon'].values[0]
        elif matching_row['consent-kumu'].values[0] == 'consent-public':
            print("Matching value in df2 for id", id_value, ":", "Consent is public")
            df1.at[index, 'label-public'] = matching_row['label'].values[0]
        elif matching_row['consent-kumu'].values[0] == 'consent-pseudonymised':
            print("Matching value in df2 for id", id_value, ":", "Consent is pseudonymised")
            df1.at[index, 'label-public'] = matching_row['label-anon'].values[0]
        else:
            print("Matching value in df2 for id", id_value, ":", "Consent is: ",matching_row['consent-kumu'].values[0])
    else:
        print("No matching value found in df2 for id", id_value)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

data_connections_anon = df1

# redact identifable information from data_elements_anon where no consent
columns_identifiable = ['email', 'github', 'position', 'pronouns', 'url']
data_elements_anon.loc[data_elements['consent-kumu'] == 'consent-none', columns_identifiable] = np.nan

# delete opinion columns for everyone %**
columns_opinions = ['how-to-engage','influence-over-programme','interaction-participant-active','interaction-participant-all','interaction-participant-leadership','interaction-participant-presenter','interactions-count','interest-in-programme','moe-level','notes']
data_elements_anon = data_elements_anon.drop(columns_opinions,axis=1)

# get rid of boring columns %**
columns_boring = ['created-date', 'created-by', 'modified-last-date', 'modified-last-by', 'url']
data_elements_anon = data_elements_anon.drop(columns_boring,axis=1)



# replace labels with label_anon where consent == none
data_elements_anon.loc[data_elements_anon['consent-kumu'] == 'consent-public', 'label-anon'] = data_elements_anon['label']

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




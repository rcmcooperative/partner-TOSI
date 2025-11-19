<mark>**This project is being developed in the open, with ongoing work made publicly accessible and transparent from the start. 
Accordingly this material may be incomplete, under review, or liable to change.
We welcome your thoughts and contributions to this material following the routes described in the [CONTRIBUTING guide](../../../CONTRIBUTING.md).**</mark>

# Community mapping
Mapping the community is an essential stage of work to understand who your community are. 
Understanding who they are allows you to understand their perspectives and priorities, and anticipate their needs. 

A community map is also an essential tool for community managers to track engagement, identify opportunities for growth, manage pathways to leadership, and connect individuals or groups with shared interests. 
This work is often done implicitly or informally, and suffers from a lack of reproducibility when there are changes in leadership. 

We advocate for a transparent and reproducible mapping workflow, to optimize the management of large communities. 
Public share of a community map is also a valuable tool for community members to identify themselves and locate others with shared interests. 

## Notebook of activity (oldest to newest)
*This file is being used as a lab note book, to keep track of activities associated with this task. A formal write up will be prepared at the end of this project*


### 2025-09-29

This phase of work has been brought forward from [the proposal](../../proposal-OSRP-RCMCoop.md) so it can be used to manage contacts for invitation to interview. The structure and settings are broadly being followed as per our [previously developed structure](http://github.com/rcmcooperative/community-mapping). Additional lists have been generated where noted below. 

**Notes these lists contain identifiable information and are accessible only to immediate project members. Sharing is currently managed by [Luisa Pimentel](../../../README.md#team-members)**

- **[Community-list-People](https://mcgill-my.sharepoint.com/:l:/r/personal/luisa_pimentel_mcgill_ca/Lists/CommunityListPeople)**
    - List of people with contact information. Cross linked to with affiliations, initiatives they lead or participate in, tools they develop or use, and interactions they have attended where this information is available.  
- **[Community-List-Affiliations](https://mcgill-my.sharepoint.com/:l:/r/personal/luisa_pimentel_mcgill_ca/Lists/CommunityListAffiliations)** 
    - List of organizational units people can be attached to, e.g. Universities, Departments, Labs etc. 
- **[Community-List-Initiatives](https://mcgill-my.sharepoint.com/:l:/r/personal/luisa_pimentel_mcgill_ca/Lists/CommunityListInitiatives)** 
    - List of initiatives delivered by TOSI or their affiliates. Use to identify which individuals are leaders/participants in a given initiative, or recipients of awards. 
- **[Community-List-Interactions](https://mcgill-my.sharepoint.com/:l:/r/personal/luisa_pimentel_mcgill_ca/Lists/CommunityListInteractions)**
    - Used to track interactions (for example seminars) delivered by TOSI or their affiliates, to monitor engagement. 
- **[Community-List-Tools](https://mcgill-my.sharepoint.com/:l:/r/personal/luisa_pimentel_mcgill_ca/Lists/CommunityListTools)** 
    - To identify open science tool developers and users, as infrastructure development is a mission area for TOSI. 

The intention is to set this infrastructure up now for use in this project, and to build it out a space for ongoing use by TOSI and initiative leadership to record engagement going forward. A further extension would be self-service submissions to the map by participants/developers/users.

Ongoing training is being provided to Luisa, and further documentation on usage will be developed.

The sharepoint lists have been shared with [Cass' RCM Cooperative email](../../../project-management/communications/channels.md#email)). 

### 2025-10-02

Sharepoint list work shared at TOSI team meeting. Annabell approves continued development and review of Initiatives and Tools list by Luisa for completeness.

### 2025-10-07

The sharepoint lists have been shared with [Cass' McGill email](../../../project-management/communications/channels.md#email)) now this is available. This has been necessary as Cass was previously unable to to make or edit the look-up columns which are essential for linking elements.

Luisa has reviewed the Initiative list and made amendments. Luisa is also supporting data entry for email addresses, initiative leadership and tool contacts.

### 2025-10-15

Double checked permissions to access the lists before this repo is made public. 
Links above have been updated and all previous links deleted. (this document has not yet been pushed, so no links have been published in previous versions before this verification step).
Note the links are all in Luisa's private Sharepoint area.
Suggest this is moved to a TOSI group area for improved long-term fidelity of access.

Luisa is continuing to add email addresses. 
Cass will do a big push on this so interview invites can be sent ASAP. 

### 2025-10-20

Added previous awardees and PIs of labs with team members who'd received awards (2023, 2024). 

Added Cooper Prize recipients (from the Neuro)

Added Open Science in Action Seminar speakers and Chairs
- This should really be refactored as an element on the "interactions" list. 
- Leaving it as an "initiative" for now as that is enough to show who has engaged across multiple activities.

Need to get lists of:
- Previous GRC members
- Previous Cooper Prize reviewers

### 2025-10-22

Transferred Open Science in Action form "initiative" to "interaction" and linked people as "interaction-speakers"

Thinking about what data is available to track engagement. 
For most interactions TOSI have summary data e.g. "200 people attended", but this is not the right resolution for understanding where initiatives are reaching nor the pathways of people into leadership. 
Where possible for the events which are being organized currently, I'll be asking the team to collect names of participants and noting their participation on the people list.
We will also brainstorm in the team meeting tomorrow about what data they do currently hold at a fine enough level, e.g. applicants for awards (currently I only have recipients/runners up) and applicants for APC offset. 

I'm going to work on adding labs to the "affiliations" list, to see where they have clusters of interest, or more importantly where they don't.
This information is implicit to their operations at the moment, but i suggest to demonstrate it effectively will require more centralized data collection. 
I'd also like to be able to clearly show the value of working closely to build engagement with targetted groups/individuals. 

Going to push on tidying the data and running through the code for visualisation in kumu, to grow engagement about collecting this data. 
There will be quite a a few areas of the [existing code](https://github.com/rcmcooperative/community-mapping/blob/main/code/sharepoint-to-kumu-xlsx.py) which need adapting. 

I've taken the TOSI Leaders Group off the list for now, as I keep having to work around them (e.g. in missing emails).
I think they are distant enough to exclude for this exercise, and will be easy to re-add at a later date.

Remember in all of this that what you measure is what is (or becomes) important (or rather you should think about what you value when you set your measures). If we value diversity of engagement (e.g. getting people from different labs), then we should be recording this.

### 2025-11-01
- Added lab elements for all labs in all [research groups](https://www.mcgill.ca/neuro/research)
- Considering adding all people from all labs, then we could see who we have engaged showcase filter). Unfortunately this data is incomplete from an external transparency perspective as it relies on each lab having an up to date lab page. The information will probably exist in HR records, but unlikely to be able to access that in an appropriate time frame for this project. Could be updated later.
- Currently will show where we have touch through the presence of lab members on the map.

### 2025-11-03
- Added OS Helpers (dm from Luisa)
- Luisa also shared applicants to internal awards. Not sure I've correctly understood or grouped awards, so will review with the team.
- Will also review the broad categorisation I've created for "initiative types" (initially based on the TOSI teams grouping), and think about how this will be usefully visualized. For example, awards and the OS dashboard are both included as "incentives", but in filtering the data it would be useful to see award recipients seperately form contributors to the dashboard (although we don't yet have any contributors to the dashboard except Gabriel). Will look to see if any others need cleaning.

### 2025-11-04
- List of presenters of Open Science Lab Tours received. 
- Recategorised Lab tours from an "initiative" to interaction, and added the above list as speakers
- Spent some time with Luisa unpacking areas I felt there was confusion about and setting up the activities for 2025-11-05

#### Grants vs awards
- Grants are project applications
- Awards are track record of accompliments
    - Except Launchpad (UG)
        - Track record not reviewed
        - Comes from different budget envelopes
        - So listed in the "awards" page, but is actually more of a grant 
- Redid the initiative types to make the above practical distinctions clear
    - previous category types based on TOSI's miro (the link for this is in [Luisa's notes](https://mcgill.sharepoint.com/:w:/r/sites/TOSI_Group/Shared%20Documents/Community%20Officer%20Initiatives/Open%20Scientist%20in%20Residence%20Program/2025/OSRP%20meeting%20notes_2025%20edition.docx?d=w87f3a01b43be4468990788f03f0c00d4&csf=1&web=1&e=L7NTxK), which I can't seem to access now... )
    - New category types:
        - committee
        - training-education
        - support-infrastructure
        - incentives
        - metrics-impact
        - outreach-community
        - contribution-recognition
        - funding-projects
        - funding-open-access
- Added the history obtained from Luisa about who has applied for these programms
    - ==Still to add details from here: https://mcgill.sharepoint.com/:x:/s/TOSI_Group/ETN2_lmOKi1Gnuh9sIQiRHQBHfUYP77nl7LEUx7Gph_9PQ==
    - Note that the current data structure is not identifying who was successful in awards, and what year they applied. 
    This would need restructuring, which we don't have resource for at the moment.
- Requesting a list of who has applied for APC funding from Gabriel - received and added.
    - Lots of labs have only engaged via APC Offset programme. This suggests this is a valuable gateway to build engagement.

#### TOSI Trainee Council vs The Neuro Trainee Committee vs OSHO
- TOSI Trainee Council is McGill wide, hence includes Douglas folks
    - Now confirmed who is leadership on this committee and updated others to -initiative-participant
- OSHO is separate from TOSI Trainee Council, but has overlap via Navid


### 2025-11-05

#### Add Best practice guides 
- https://www.mcgill.ca/neuro/open-science/open-science-best-practices
- Contributors well listed on the two guides currently available
    - Adding these has added lots of new people and connections.
    - It would be interesting to understand if/how this was conducted differently or engagement activated

#### Core facilities
- https://www.mcgill.ca/neuro/research
- These now all added as "core-facilities" in affiliations list
- Azrieli Centre = "Centre" not "core facility"
- core facilities are all Neuro affiliated
- Spiralled out to generate connections with Ludmer Centre
    
#### Partnerships
- https://www.mcgill.ca/neuro/research/partnerships
- not adding for now as it is not clear what value these will add the the map in the first instance, and not clear how these are defined

#### OSHO resources
- https://openscienceofficehours.github.io/osoh_website/FEATURED-open-science-resources/
- Not adding these for now, as many are non-Neuro and will take a lot of resource to review
- Happy that we've captured a good bunch in our exiting tool set, and present with ambition for self services. 

#### Open Science in Action Symposium 
- For some years had a organisers tab, but not all. These people have been added to "leadership" for that year
- 2023 also had named people at Networking, but not consistently on the program

#### Data wrangling for kumu
- pulled the [code](~./code/community-mapping-sharepoint-to-kumu-xlsx.py) and [env.yml]((~./code/kumu-env.yml) to convert to kumu from rcmcoop repo
- Tested the env and having a read through to refamiliarise! 
- On the actual visualization, for proof of concept it will be sufficient to have people, affiliations and tools as elements, with initiatives and interactions as metadata. 
- For initiatives, collapse the name to also include initiative type, so then can filter/showcase by e.g. "funding-project-x, y, z".
- Also add a initiative-engagement-count, so you can see who has been a repeat organiser
- For interactions lets keep the name as it is (they are unique enough and there are not too many), but also add a "count" 

### 2025-11-06
- Reviewing (and implementing) column validation rules (e.g. [no spaces in emails](https://github.com/rcmcooperative/community-mapping/blob/main/docs/how-we-map-sharepoint-lists.md#email))
    - Remember to put filed names in [] in validation formulae
        - Only seems to work if you enter the validation via the whole list settings page, not via column>edit
    - Decided to put "no commas" warning on every free text time and pick lists, to make it easier to create links later on (commas are interpreted as new cells in my code)
- Need to remember to add something in usage not to change the column headers, otherwise valuation will break
- Aiming to remove as much processing as possible from the script, so the data available in the lists matches what is in kumu
- Added a consent option "consent-not-invited" and set this to default for new items in the people list.
Updated all people entries to "consent-not-invited" 
- Setting element sizes by type:
    - University = 100
    - Faculty = 80
    - Department = 70
    - Institute = 60
    - Research group = 50
    - Centre = 40
    - Core facility = 30
    - Lab = 20
    - Tool = 10
    - People = 1
- Using calculated value
    - Tried with formula `=SWITCH([kumu-size],"university",100,"faculty",80,"department",70,"institute",60,"research group",50,"centre",40,"core-facility",30,"lab",20,"")` but switch is not available in sharepoint lists. Have to use nested if instead
    - `=IF([kumu-type]="university",100,IF([kumu-type]="faculty",80,IF([kumu-type]="department",70,IF([kumu-type]="institute",60,IF([kumu-type]="research group",50,IF([kumu-type]="centre",40,IF([kumu-type]="core-facility",30,IF([kumu-type]="lab",20,""))))))))`
    - Had to create a new column of the type "calculate" rather than a choice with numbers
- Tried to create a calculation based on how many initiatives-participant per row, but sharepoint can't do calculations on look-up columns or multiple choice columns
- changed name-initiative to enforce unique values
- Not completed all validation settings on tools list
- Updated size calculation to make The Neuro biggest and easier to find on the map:
    - `=IF([name-affiliation]="The Neuro",100,IF([kumu-type]="university",100,IF([kumu-type]="faculty",80,IF([kumu-type]="department",70,IF([kumu-type]="institute",60,IF([kumu-type]="research group",50,IF([kumu-type]="centre",40,IF([kumu-type]="core-facility",30,IF([kumu-type]="lab",20,"")))))))))`

### 2025-11-10
- Had to add anonymizedf (via pip) to the [conda env](~./code/kumu-env.yml)! Updated the yml
- Debugging [code](~./code/community-mapping-sharepoint-to-kumu-xlsx.py)

### 2025-11-11
- Debugging code (now running)
- Setting up [kumu display settings](../../../code/kumu-settings/kumu-display-settings-internal)
- Map shows lots of affiliations missing - fulled in where I can
- Thinking about how we manage the award/grant data, I had previously grouped recipients and applicants together as "participants". This was a mistake, as they show different things. 
- Now I've created an initiative item per year, and lookups in the people list for "funding-recipient" and "funding-applicant". 
- Aim is to put all financial incentives together in these lookups
- Not moved to these lookups yet:
    - APC offset (split into years)
    - Cooper prize recipients (if any were Neuro)
    - Badges (they do come with $100)
- Now wondering if the GRC and TC committees should be split up by year, so you can see who is on there currently and who is passed... Probably should be...
- This might leave only commitees in the initative-participant etc. lookups, so it would make sense to rename this, and make it easier to showcase them all together
- Also added the affiliation type name, (e.g. Poline => Poline Lab), to make it a bit easier to read in the map. Added other missing affiliation types
- Also had to delete the "tool-user" lookup to make the "funding-recipient" etc. lookups, as sharepoint had reached the max number of lookups...
- Although Hatrock has a first and runner up prize, I've decided to group these together and note as runner up in the notes, so we have some space for more lookups later. Hatrock was the only one which had an explicit "runner up", so doesn't add much value to have it as a separate field (which would require a separate showcase in kumu).
- Vis is looking good! Changing the of items so The Neuro is the biggest (currently Universities are the biggest).
- Making sure all PIs are affiliated with their labs only, then labs are affiliated with centres etc. 
- When uploading data to kumu, there is a box tick option to override existing data. I'm ticking this, but not sure it's all being cleared (remembered this from previous projects too). I'm going to upload a completely blank list of elements and connections, to wipe the slate.
- Just found this useful [list of units at BIC](https://www.mcgill.ca/bic/about-us-1/staff). I've changed labs who I had as affiliated with BIC to the units given her. Remember that we're not plotting everyone, just the ones we have touch on (and The Neuro specific labs), so there are other PIs at BIC who we're aren't collecting. 
- Made a thing to count the total number of engagements per element, to showcase single vs repeat engagers (note however that we're not yet recording everything that should be recorded to really understand who is most engaged! e.g. attendance at events)

### 2025-11-12
- Got access to the unsuccessful applications internal awards. Now added affiliations.
- Got access to Helpers programme placements. Now added.
- Note I've not added the data of who I've spoken with in these interviews, to keep them anonymous.

### 2025-11-13
- Map shared with TOSI team. 
- Available at https://kumu.io/cassgvp/tosi-internal (private kumu project)
- Note the code is also generating a deidentified dataset for kumu, but I've not reviewed or tested this. 

### 2025-11-18
- User `gabrielp` (Gabriel Pelletier) has been added to the kumu map as a contributor.
- Either Gabriel or myself will need to have a paid account to add him as a manager on the map.
- Now have access to [grant applications](https://mcgill.sharepoint.com/sites/TOSI_Group/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FTOSI%5FGroup%2FShared%20Documents%2Fprizes%5Fawards%5Ffunding%2Fneuro%5Fopen%5Fscience%5Fgrants&viewid=f986b468%2D5c06%2D4f4b%2D96dc%2Decdb8bad5804) to review who has applied and their affiliations - now added, inc 2025 applicants
- So much effort is going into preparing these applications, but so few are funded. While this is valuable exercise for trainees, it is a shame that the capacity for experimentation an innovation is being limited. Would love to explore what can be done with no or minimal funding. 
- 8 new contacts added in this years grant applications (where applications were not open to labs which had previously received funding). While this looks promising, it is not a self sustaining method for growing reach. Also not able to disentangle whether this came from lab tours widening awareness or specific exclusion criteria.








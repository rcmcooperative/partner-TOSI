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

This phase of work has been brought forward from [the proposal](../../proposal-OSRP-RCMCoop.md) so it can be used to manage contacts for invitation to interview. The structure and settings are broadly being followed as per our [previously developed structure](http://github.com/rcmcooperative/community-mapping). Additional lists have been generated where notes below. 

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
- Spent some time with Luisa unpacking areas I felt there was confusion about:

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
- Requesting a list of who has applied for APC funding from Gabriel

#### TOSI Trainee Council vs The Neuro Trainee Committee vs OSHO
- TOSI Trainee Council is McGill wide, hence includes Douglas folks
    - Now confirmed who is leadership on this committee and updated others to -initiative-participant
- OSHO is separate from TOSI Trainee Council, but has overlap via Navid

#### Add Best practive guides 
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



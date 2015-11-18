KPCC's Officer Involved
=======================

In This Guide
=============

* [How We Did It](#how-we-did-it)
* [What Is Here](#what-is-here)
* [Data Dictionary](#data-dictionary)
* [Authors and Contributors](#authors-and-contributors)

[How We Did It](http://projects.scpr.org/officer-involved/stories/how-we-did-it/)
=================================================================================

As KPCC set out to analyze [how often on-duty police officers and sheriff's deputies in Los Angeles County shot another person](http://projects.scpr.org/officer-involved/), one thing became clear:  This isn't data you can simply look up.

Most data on police shootings is scattered, focused on fatal shootings when it’s available at all and even then rarely contains the level of detail we were looking for: How often do police shoot people who are unarmed? How often do shootings occur after pursuits? Why did officers feel they had to use deadly force?

The only agency privy to the details of every shooting in Los Angeles county is the [Los Angeles County District Attorney’s Office](http://da.co.la.ca.us/). When an officer shoots someone, prosecutors review evidence to determine whether it was legally justified.

If prosecutors decide not to file charges, the district attorney sends a [letter](http://projects.scpr.org/officer-involved/explore/documents.html) to the head of the law enforcement agency summarizing the facts of the case and spelling out the reasons a criminal case won't be pursued.

KPCC requested letters for all shootings that occurred on or after Jan. 1, 2010. All but two shootings in 2015 were still pending as of Nov. 10, 2015, so we ended our period of analysis at Dec. 31, 2014. The district attorney released [359 letters](http://projects.scpr.org/officer-involved/explore/documents.html) that KPCC determined were on-duty officer-involved shootings. These documents show 375 people were hurt or killed in those cases. We did not review shootings that involved off-duty officers or district attorney reviews of suspects who died in custody from causes other than shooting. As of Nov. 10, 2015, the district attorney had not rendered a decision on at least 29 on-duty shootings that occurred during the five-year period we reviewed.

[Read more about how we did it](http://projects.scpr.org/officer-involved/stories/how-we-did-it/)

What Is Here
============

Of the data KPCC compiled we've made [select fields available](http://projects.scpr.org/officer-involved/explore/) in a [csv](kpcc-officer-involved-data.csv) and [json](kpcc-officer-involved-data.json) formats. As we continue to report about this issue, additional fields will be made available.

Data Dictionary
===============

**NOTE**: All determinations were made using language from the District Attorney narratives and Medical Examiner's data on fatalities.

* **id** (primary key):
    * Unique ID of the record

* **district_attorney_county** (string):
    * County of District Attorney's office that reviewed the letter.

* **district_attorney_file_number** (string):
    * File number used by the district attorney's office. In the case of the [Los Angeles District Attorney's Justice System Integrity Division](http://da.lacounty.gov/contact/office-directory/justice-system-integrity-division) the first two numbers indicate the year in which the shooting took place.

* **incident_url** (string):
    * Link to the District Attorney summary letter on [DocumentCloud](https://www.documentcloud.org/home).

* **person_name** (string):
    * Name of person shot

* **person_ethnicity** (string):
    * Race/ethnicity of person shot and killed pulled from [Los Angeles County Medical Examiner](http://mec.lacounty.gov/wps/portal/mec) data for shootings during the five-year period of review in which there were "law enforcement-related circumstances."

* **person_gender** (string):
    * Gender based on district attorney records or [Los Angeles County Medical Examiner](http://mec.lacounty.gov/wps/portal/mec) data.

* **person_age** (string):
    * Age of the person shot and killed at time of death, pulled from [Los Angeles County Medical Examiner](http://mec.lacounty.gov/wps/portal/mec) data for shootings during the five-year period of review in which there were "law enforcement-related circumstances."

* **district_attorney_date_of_letter** (string):
    * Day, month and year of district attorney letter declining to prosecute.

* **type_of_incident** (string):
    * Comma-separated list of "types of force" used by officers in an incident, ordered by occurrence. For instance, a value of ```Pepper Spray, Bean Bag Weapon, Shooting``` indicates less-than-lethal force consisting of pepper spray and a bean bag weapon were used prior to deadly force.

* **date_of_incident** (string):
    * Day, month and year of the shooting.

* **person_killed** (boolean):
    * FALSE: Person was shot but did not die
    * TRUE: Person was shot and died

* **person_armed** (boolean, null OK):
    * FALSE: If a person did not possess a weapon at the time of the shooting we deemed them to be unarmed, even if an officer feared the person was trying to use a vehicle to injure or kill the officer, or attempting to take an officer's weapon.
    * TRUE: Person had any type of weapon at the time of shooting, including a firearm, airsoft pistol, BB gun, knife or other weapon
    * NULL: Person was a bystander and not involved in the shooting, or carrying a non functional, toy or replica firearm.

* **armed_with_firearm** (boolean):
    * FALSE: Person did not possess a firearm.
    * TRUE: Person possessed a firearm.

* **armed_with_weapon** (string):
    * FALSE: Person did not possess a weapon other than a firearm.
    * TRUE: Person possessed a weapon other than a firearm.

* **used_vehicle_as_weapon** (boolean):
    * FALSE: Person did not try to use a vehicle as a weapon during incident.
    * TRUE: Officer said person tried to use a vehicle as a weapon during incident.

* **person_ignored_officer_commands** (boolean):
    * FALSE: Person did not ignore or disobey officer commands.
    * TRUE: Person ignored, disobeyed or did not hear officer commands.

* **person_hid_hands_from_officer** (boolean):
    * FALSE: Person was not hiding hands during incident.
    * TRUE: Person concealed hands or made furtive movements during incident.

* **person_reached_for_waistband** (boolean):
    * FALSE: Person did not reach for, tug or move hands around waistband or pants.
    * TRUE: Person reached for, tugged or moved hands around waistband or pants.

* **person_fled_by_foot_or_vehicle** (boolean):
    * FALSE: Person did not flee during incident.
    * TRUE: Person fled during incident by foot or car.

* **person_grabbed_for_officers_weapon_holster** (boolean):
    * FALSE: Person did not grab for officer's weapon during incident.
    * TRUE: Person grabbed for officer's weapon during incident.

* **person_signs_of_mental_illness** (boolean):
    * FALSE: No signs of mental illness.
    * TRUE: Person had history of mental illness, relatives and/or friends told police person had history of mental illness or toxicology tests showed presence of therapeutic drugs in the system.

* **person_signs_of_impairment** (boolean):
    * FALSE: Person's toxicology did not show signs of impairment or drug use, person did not admit to alcohol or drug use, or information about impairment comes from a third party.
    * TRUE: Person's toxicology showed signs of drug or alcohol use, or person admitted to drug use.

* **officer_self_defense** (boolean):
    * FALSE: Officer not defending him or herself in shooting, according to district attorney summary letters.
    * TRUE: Officer was defending him or herself in shooting, according to district attorney summary letters.

* **officer_defense_of_civillians** (boolean):
    * FALSE: Officer not defending a civilian in shooting, according to district attorney summary letters.
    * TRUE: Officer was defending a civilian or civilians in shooting, according to district attorney summary letters.

* **officer_defense_of_officers** (boolean):
    * FALSE: Officer not defending a law enforcement officer in shooting, according to district attorney summary letters.
    * TRUE: Officer was defending another law enforcement officer or officers in shooting, according to district attorney summary letters.

Authors and Contributors
========================

* [Chris Keller](http://www.scpr.org/about/people/staff/chris-keller)
* [Aaron Mendelson](http://www.scpr.org/about/people/staff/aaron-mendelson)
* [Annie Gilbertson](http://www.scpr.org/about/people/staff/annie-gilbertson)

KPCC's Officer Involved
=======================

In This Guide
=============

* [How We Did It](#how-we-did-it)
* [What Is Here](#what-is-here)
* [Data Dictionary](#data-dictionary)
* [Authors and Contributors](#authors-and-contributors)

[How We Did It](http://projects.scpr.org/officer-involved-sb/stories/how-we-did-it/)
=================================================================================

How many people do police shoot in San Bernardino? Who is shot by law enforcement? What circumstances lead to shootings?

These are questions that government data can’t answer.

That’s why KPCC and The San Bernardino Sun built a database tracking police shootings in San Bernardino County from 2010 through 2015, [providing an unprecedented examination of police shootings in the county](http://projects.scpr.org/officer-involved-sb/).

To construct our database and find answers to our questions, we combed through letters written by the San Bernardino County District Attorney. The D.A. investigates every shooting in which an officer’s gunfire strikes a person, to determine if criminal charges are warranted. Since it has been more than a decade since an on-duty officer has been charged in connection with a shooting in San Bernardino County, these letters represent a comprehensive record of shootings in the county in which investigations are closed. Some cases from the review period remain open.

To turn hundreds pages of memos into a database, reporters at KPCC and The Sun reviewed each letter and entered data on dozens of fields relating to suspects, officers and circumstances in shootings. A second journalist double-checked every one of the 102 entries.

[Read more about how we did it](http://projects.scpr.org/officer-involved-sb/stories/how-we-did-it/)

What's Here
============

Of the data KPCC compiled we've made select fields available in a [csv](kpcc-officer-involved-data-sb.csv) and [json](kpcc-officer-involved-data-sb.json) formats.

Data Dictionary
===============

**NOTE**: Each row represents a person struck by police gunfire in San Bernardino County. In one case, two people we injured in the same shooting incident. All determinations in the data were made using language from the District Attorney narratives and Medical Examiner's data on fatalities.

* **id** (primary key):
    * Unique ID of the record

* **district_attorney_county** (string):
    * County of District Attorney's office that reviewed the letter.

* **district_attorney_file_number** (string):
    * File number used by the district attorney's office.

* **incident_url** (string):
    * Link to the District Attorney summary letter on [DocumentCloud](https://www.documentcloud.org/home).

* **person_name** (string):
    * Name of person shot

* **person_ethnicity** (string):
    * Race/ethnicity of person shot and killed pulled from San Bernardino County Sheriff's Department, Coroner Division data for shootings during the five-year period of review in which there were "law enforcement-related circumstances."

* **person_gender** (string):
    * Gender based on district attorney records or coroner data.

* **person_age** (string):
    * Age of the person shot and killed at time of death, pulled from coroner data for shootings and District Attorney reports. Not always available.

* **district_attorney_date_of_letter** (date):
    * Day, month and year of district attorney letter declining to prosecute.

* **type_of_incident** (string):
    * Comma-separated list of "types of force" used by officers in an incident, ordered by occurrence. For instance, a value of ```pepper spray, bean bag weapon, shooting``` indicates less-than-lethal force consisting of pepper spray and a bean bag weapon were used prior to deadly force.

* **date_of_incident** (date/time):
    * Day, month, year and approximate time of the shooting. The csv file contains this data as local date and time (PST or PDT). The json contains this data as UTC.

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

* **moving_car** (boolean):
    * FALSE: Officer did not shoot at a moving vehicle during the encounter.
    * TRUE: Officer did shoot at a moving vehicle during the encounter.
   

Related: Los Angeles County Shooting Data
========================
Previously, KPCC reviewed hundreds of shootings in Los Angeles County spanning 2010 - 2014. That project was [published here](http://projects.scpr.org/officer-involved) and the data is [available on Github](https://github.com/SCPR/kpcc-data-team/tree/master/data/kpcc-officer-involved).

Authors and Contributors
========================

* [Aaron Mendelson](http://www.scpr.org/about/people/staff/aaron-mendelson)
* [Annie Gilbertson](http://www.scpr.org/about/people/staff/annie-gilbertson)
* [Chris Keller](https://github.com/chrislkeller)

##Officer-Involved project data dictionary
All determinations were made using language from the District Attorney narratives and Medical Examiner's data on fatalities.

* armed_with_firearm: Boolean
    * 0: Person did not have a firearm
    * 1: Person had firearm

* armed_with_weapon: [TK--different from person_armed and person_unarmed?]

* car_stop: Boolean
    * 0: Not a traffic stop
    * 1: Was traffic stop

* date_of_incident: Day, month and year of incident

* district_attorney_county: County of District Attorney's office that reviewed the letter

* district_attorney_date_of_letter: Day, month and year of letter declining to prosecute

* district_attorney_file_number: File number of the Los Angeles District Attorney's Justice System Integrity Division. The first two numbers indicate the year in which the shooting took place

* id: Unique ID of the incident/person [TK--which?] in KPCC data

* incident_url: Link to the District Attorney letter on DocumentCloud

* officer_defense_of_civillians: Boolean
    * 0: Officer not defending a civilian in shooting
    * 1: Officer was defending a civilian or civilians in shooting

* officer_defense_of_officers
    * 0: Officer not defending a law enforcement officer in shooting
    * 1: Officer was defending another law enforcement officer or officers in shooting

* officer_self_defense
    * 0: Officer not defending him or herself in shooting
    * 1: Officer was defending him or herself in shooting

* person_age: Age of the person at time of death, as given by Medical Examiner in case of fatal shootings

* person_armed: Boolean
    * 0: Person was not armed with a weapon at the time of shooting. This includes people who officers said were using a vehicle as a weapon, or who attempted to get their firearm [TK correct? where are replica guns?]
    * 1: Person had any type of weapon at the time of shooting, including a firearm, knife or other weapon

* person_ethnicity: Race/ethnicity as given by Medical Examiner in case of fatal shootings

* person_fled_by_foot_or_vehicle: Boolean
    * 0: Person did not flee during incident
    * 1: Person fled during incident by foot or car

* person_gender: Gender as given by Medical Examiner in case of fatal shootings

* person_grabbed_for_officers_weapon_holster: Boolean
    * 0: Person did not grab for officer's weapon during incident
    * 1: Person grabbed for officer's weapon during incident

* person_hid_hands_from_officer: Boolean
    * 0: Person was not hiding hands during incident
    * 1: Person concealed hands or made furtive movements [TK--wording] during incident

* person_ignored_officer_commands: Boolean
    * 0: Person did not ignore or disobey officer commands
    * 1: Person ignored, disobeyed or did not hear officer commands

* person_killed: Boolean
    * 0: Person was non-fatally shot [TK--will data include Judd Vear or similar?]
    * 1: Person was fatally shot

* person_name: Name of person

* person_reached_for_waistband: Boolean
    * 0: Person did not reach for, tug or move hands around waistband
    * 1: Person reached for, tugged or moved hands around waistband

* person_signs_of_impairment: Boolean
    * 0: Person's toxicology did not show signs of impairment or drug use, person did not admit to alcohol or drug use, or information about impairment comes from a third party
    * 1: Person's toxicology showed signs of drug or alcohol use, or person him or herself admitted to drug use

* person_signs_of_mental_illness: Boolean
    * 0: No signs of mental illness
    * 1: Person had history of mental illness or relatives and/or friends told police person had history of mental illness

* person_unarmed: [TK--how differs from person_armed or armed_with_weapon]

* person_weapon: Type of weapon carried by person

* person_wounded: [TK--range of values]

* type_of_incident: [TK--range of values]

* used_vehicle_as_weapon: Boolean
    * 0: Person did not use a vehicle as a weapon during incident
    * 1: Person used a vehicle as a weapon during incident

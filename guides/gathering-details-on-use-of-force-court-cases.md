LA County Use of Force
======================
This is going to be an attempt to chronicle how the KPCC Data Team tracked down the details of different criminal cases involving police officers in LA County. It will also hopefully serve as an illustrative example for others that want to wrangle information out of the court system. It can be difficult to track down the details of cases that involved police officers, and sometimes the charge sheet doesn't give enough information for a news story, so more leg-work is involved. 

####What we were looking for 
While working on a project involving police oversight in LA County, the Data Team encountered a problem. We had a list of police officers in LA County that had been charged with excessive use of force, but we didn't have any information about what the officers did to be charged. 

The goal of looking through officer use-of-force cases was to find the narrative details of the incident because we needed to know what the officers did that led the DA to charge them. Specifically, we wanted to see cases where officers had been charged of using excessive force only while on-duty.

####What we were given 
In the cource  of the OIS project, we had two sets of information relating to officers and use of force in LA County. The first is a large number of declination memos, and the second is a spreadsheet of cases where the DA filed charges. 

The spreadsheet of officers who were charged was given to us by the DA after we submitted a CPRA request for "names, badge numbers, and case numbers" relating to filed on duty and off-duty use of force cases filed with the DA's office. The spreadsheet the DA provided only has case number, case name, and the charges. The DA doesn't make a distinction between on-duty and off-duty incidents, so it included both on-duty officers, sheriffs deputies in charge of county jails, and off-duty officers. 

####Cleaning the data
Since the info the DA gave us had officers whose charges fell outside the scope of our project, we had to seperate the relevant cases from the rest. We had case number, officer names, and the charges. 

First we had to figure out what each officer on the list was charged with. The [LA Superior Court](http://www.lacourt.org/) has an online database of cases filed in LA County. Not all the cases are free to view, but the website does have summaries of criminal cases, which provide basically the same information that the DA provided us, plus some other information like dates and dispositions. 

We went through and verified all the information that the DA provided us, checking against the criminal case summary online. It became apparent while doing this that the info the DA gave us was slightly inaccurate. Sometimes the charges online didn't match the charges the DA gave us, or the case number didn't match the name provided. Our spreadsheet, titled LA County Use of Force Reports, has a column for marking differences in the spreadsheet provided and the online database.

Once the info was verified, we had to figure out what the officers were charged with. [The California Legislative Info website](http://leginfo.legislature.ca.gov/faces/codes.xhtml) has the complete law, searchable by number. Our spreadsheet has the charges that the officers faced and a brief description. After cataloging every charge and disposition, we labeled the whether the case involved excessive force on duty and whether it was relevant. 

In addition to adding information on the charges, we also cataloged the officer's pleas and the disposition. Pleas were either guilty, innocent, or no contest (nolo contendre in the online database) and the dispositions were either guilty/convicted, dismissed, or dismissed per 1203.4 P.C. (which means convicted and later expunged).

After cataloging all of the charges, there were 24 cases that fit our criteria. Relevant here means that the case involved a potentially on-duty officer that had unlawfully used force against a person, weeding out cases of domestic abuse and sexual assault. 

####Finding Narrative Information 
The information provided by the DA and the LA Court database isn't enough to find out what exactly happened in the cases. We needed to narrow down much further. 

There are a few problems with only looking at the court's online database and charge sheet. Primarily LA County jails are run by the sheriff's department, which means that that the list of officers the DA gave us also included sheriff deputies that had been accused of mistreating inmates. While an important issue, such cases fell outside of the purview of our project. We need to know whether the case involved an officer, on duty and routine patrol, used excessive force, and the court's online database didn't have that info. 

The next step we took was to go to the courthouse and look up the cases. Criminal cases are public records and open to viewing. The case does not always have the information you might be looking for, but its the first place to look. Clerks at the different courthouses have the right to go through the files and pull things that they believe to not be subject to public records. How much they are allowed to pull/redact is unclear, so fight back when they may be pulling way too much. 

On that note, find people who can advocate for you. They will be your friend. Reach out to public information officers in different parts of the civic structure.They can help you when the courts get apprehensive about following public information laws. 

There are many different places that the criminal case might be:

* Archives and halls of records. In Los Angeles, its the Hall of Records located at 320 W. Temple St. Ideally, all the cases would be at the hall of records, but in LA, files are on about a 7 year delay in being moved from various courthouse offices to the hall of records. You can request files all day, but they will only give you three at a time to view. 

* Courthouses where the cases were filed. The Clara Shortridge Foltz Criminal Justice Center at 210 W. Temple St. had a majority of the files I needed to see. The clerks at the Justice Center said that the public was only allowed to view 3 files a day. They havedifferent excuses for why, and said that it came down to there being a very small staff handling all requests for cases. KPCC had 19 cases and waiting that long wasn't reasonable so we worked with Mary Hearn, the Public Information Officer for the Superior Court of LA to get the files faster.

* City Attorney's Office. Not all the cases were filed with the District Attorney's Office. The public information officer there, Frank Mateljan, tracked down some information that we needed. 

* Newspapers. For some of the cases, the only narrative information we could find came from the LA Times in articles published during trials.  

Many of the files were missing narrative details related to the crime. We were able to find out that Officer X violated Penal Code ### when he assaulted Victim A, but not the circumstances under which the assault occurred. The amount of information in each file was wildly different case to case. In one instance, the clerks only left three pages in the file, and in others, the case contained the entire testimony. 


####Conversation with Dave Maas 
In conversation with journalist/Electronic Frontier Foundation activist [Dave Maas](http://maassive.com/), he gave a number of suggestions on the best ways to go about finding details on court cases. Here is a short list of all the things he suggested we try.

* [District Attorney's Office](http://da.co.la.ca.us/)

The two best documents we can get from the DAs office are the charge evaluation worksheet and the declination memorandum. The charge evaluation worksheet details what the defendant was charged with, so a list of the penal/vehicle/health etc. code violations, but won't have a lot of details. 

The declination memo will have lots of narrative information but is only available when the DA chooses not to prosecute. It has a complete story of what led up to a potential crime, but is only available some cases. A declination memo literally means a memo detailing why the DA is declining to prosecute. 

* Police Oversight Board

The Police Oversight Board tracks complaints about officers. You can track down the complaints leveled against the officers, but the letters may not have the officer's names included. Each police department has their own oversight board. 

* [Civil Service Commission](http://civilservice.lacounty.gov/)

They conduct their own mini-trials when it comes to the civil cases filed against police. You may be able to find the reports on those hearings, but like other documents, it may have the officer's name removed/redcated. 

* [Civil Suits](https://www.lacourt.org/paonlineservices/civilimages/publicmain.aspx?)

Investigate the civil case repository of the LA Superior Court to see if the officers have had civil cases filed against them related to their use of force. The County charges for viewing civil cases.  

* Lawyers

There tends to be a small number of lawyers that go after bad cops in any given city. Dave said that they tend to keep their own list of crooked cops and suggested that I call some lawyers and talk to them to see what they would be willing to share

* [Justia.com](https://dockets.justia.com/)

Look through dockets.justia.com to find more filings against the officers or the police department. Filter by civil rights cases to narrow down the field. This is a difficult avenue to follow successfully because you need the plaintiff's name.


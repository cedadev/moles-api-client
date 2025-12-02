#!/usr/bin/env python

"""
faam_record_creator.py
======================

Ulimately, what we're aiming to do here is to create an Observation per FAAM flight
which will need us to gather all the necessary pieces of information together into a dictionary
which we'll then use to create the new Observation by this type of call:
 
# create instance of model
faam_obby = Observation(**faam_flight_dict)
# don't forget to save to database!
faam_obby.save()


Written by: G A Parton

Creation: 14th August 2015

Version 1.0: initial scripting



"""
# first let's call in the standard libraries we need...

import unicodecsv as csv
import os
import sys
#import urllib2
import getopt
import glob
import re
import calendar
import json
import datetime
import codecs
import collections
import logging
import collections

# and set the environment so we can interact with MOLES.
    
os.environ["DJANGO_SETTINGS_MODULE"] = "cedamoles_site.settings"
import django
django.setup()

# and call in the MOLES library


from cedamoles_app.models import *
from cedamoles_app.code_lists import * # gives me the all the codelist in my local context.


sys.path.append("/home/badc/software/catalogue_content_scripts")
#sys.path.append("/home/badc/software/catalogue_content_scripts/routine_maintanence")
#from routine_maintenance import permissions_object_setting as pos
import moles_basic_tools as mbt
#from moles_basic_tools import *
from ceda_elasticsearch_tools.elasticsearch import CEDAElasticsearchClient


# we can then call up the value with things like: CEDA_RoleValue.author to ensure that we're using the correct value from the code list!


# now to start making the functions we need



# ==================================================

# acquisiton related functions

# ==================================================


def get_acquisition_link():

    """
    takes in some basic details and then tries to:
        1) find existing acquisition(s) if it/they exists
        2) if more than one, then tries to merge them to one acquisition
        3) if none, then creates an acquisitions
        4) return the id to the acquisiton record
    """
    acquisition_id = None

    return acquisition_id


# ==================================================

# Generic moles record tools

# ==================================================


def poppy_organisation_mappings(name):

    name = name.upper()
    
    poppy_org_dict = {'FAAM': 15
                     , 'BAE SYSTEMS': 1531
                     , 'LEEDS': 16
                     , 'LEICESTER': 399
                     , 'READING': 80
                     , 'NERC': 11
                     , 'MET OFFICE': 5
                     , 'EUMETSAT': 234
                     , 'EUFAR': 154
                     , 'CEH EDINBURGH': 409
                     , 'UNIVERSITY OF MANCHESTER': 65
                     , 'LAQUILLE': 1532
                     , 'MANCHESTER': 65
                     , 'UEA': 340
                     , 'YORK': 249
                     , 'BADC': 1
                     , 'CEDA': 3134 }
    
    if name in poppy_org_dict:
        
    
        try:
            return Party.objects.get(ob_id = poppy_org_dict[name])
        except:
            log.error('NOT FOUND! > %r %r' , name, poppy_org_dict[name] ) 
    
    
    else:
        return None

def party_check_create_faam(party):
    
    party_last = party[0].strip()
    if len(party) == 2:
        party_first = party[1].strip()
    else:
        party_first = ''

    # will need to do the following:
    # check party first defined or not
    # if yes, then individual, otherwise organisation
    
    #first check to see if it is an organisation and if so, on Poppys_org_dict
    
    if not party_first:
        log.info( 'checking for org in org list.... %r', party_last)

        party_ob = poppy_organisation_mappings(party_last)
    
    else:
    
        if Party.objects.filter(lastName__exact=party_last).filter(firstName__exact=party_first):
           party_ob = Party.objects.filter(lastName__exact=party_last).filter(firstName__exact=party_first)[0]

        elif Party.objects.filter(lastName__exact=party_last).filter(firstName__startswith=party_first[0]):
           party_ob = Party.objects.filter(lastName__exact=party_last).filter(firstName__startswith=party_first[0])[0]

        else:
            log.error("")

            party_ob = mbt.party_maker(party_first,party_last)

    
    return party_ob

mbt.party_check_create = party_check_create_faam

# ==================================================

# functions to do with the Projects

# ==================================================


def get_faam_project(project_abbrev_upper):
    """
    function to make new FAAM Project record and note list of new ones made to later population
    
    note - it first checks that isn't already a MOLES Project record using the abbreviation
     
    """

    new_proj_record = None
    
    # first, lets see if we can track one down by project abbreviation only...
    
    proj_by_id_matcher = Project.objects.filter(identifier__url__iexact=project_abbrev_upper)
    
    if proj_by_id_matcher:
        if len(proj_by_id_matcher) == 1:
            new_proj_record = proj_by_id_matcher[0]
        
        else:
            raise "too many matches!!! for %s"% project_abbrev_upper
    
    else:
    
        with open('new_proj_list', 'a') as new_proj_file:
        
            new_proj_details = {'abstract': 'The %s project utilised the FAAM aircraft. Further details to follow.'% project_abbrev_upper
                               #,'imageDetails': None # imageDetails - if funder is NERC then choose NERC logo
                               ,'keywords': ' %s, FAAM, Met Office'% project_abbrev_upper 
                               ,'publicationState': u'working'# set to working
                               ,'status': u'completed'  # set to completed.. remember this is a controlled list, with mapping between the value and user wording!
                               ,'title': '%s FAAM Aircraft Project'% project_abbrev_upper
                               }




            new_proj_record = Project.objects.create(**new_proj_details)

            proj_party_dict  = {}
         
            proj_party_dict['ceda_officer'] = [('Garland','Wendy')]

            # having determined our parties, throw this into the add_parties function to add the related parties 

            mbt.add_parties(proj_party_dict, new_proj_record)

            id_details = {'relatedTo': new_proj_record
                         ,'identifierType': 'ceda_abbreviation'
                         ,'url': project_abbrev_upper.strip()
                         }
            id_added = Identifier.objects.create(**id_details)

            
            new_proj_file.write('%s|http://catalogue.ceda.ac.uk/uuid/%s\n'% (project_abbrev_upper, new_proj_record.uuid) )
            log.info('New project record created > %r http://catalogue.ceda.ac.uk/uuid/%r', new_proj_record.title, new_proj_record.uuid)
    
    
    
    
    return new_proj_record

    
def proj_maker(project_abbrev,project_details):

    """
    call is made with some outline details and then creates new project record as needed
    
    Available info is:
        {'title' : title_string
        , 'abstract' : abstract_string
        , 'faam_site_url' : row[2]
        , 'moles_project_record_url' : moles_proj_uuid
        , 'pi_last' : row[4]
        , 'pi_first' : row[5]
        , 'funder' : row[6]
        , 'other' : row[7:] 
        'moles_ob_id': proj_ob_id                                   
        }


    once created we wimply need to return the Project object ID 
        
    """
    log.info("CREATING NEW PROJECT")
    
    project_id = None
    
    if project_details['title'] == None:
        project_details['title'] = 'FAAM PROJECT TITLE NEEDED - %(date)s-%(time)s'  # insert date-time ?
    
    #project_details
    
    
    
    project_details_dict = {'abstract': project_details['abstract']# Get this from the Project record
              #,'imageDetails': None # imageDetails - if funder is NERC then choose NERC logo
              ,'keywords': ' %s, FAAM, Met Office'% project_abbrev 
              ,'publicationState': u'working'# set to working
              ,'status': u'completed'  # set to completed.. remember this is a controlled list, with mapping between the value and user wording!
              ,'title':  project_details['title']
              }
    
    # now create the record and return the project_id so that it can be linked to the record.
    
    faam_proj = Project(**project_details_dict)
    
    # don't forget to save to database!
    faam_proj.save()

    if project_details['parent_project'] != '':
        faam_proj.parentProject = project_details['parent_project']
        faam_proj.save()
        
    project_id = faam_proj
    project_uuid = faam_proj.uuid
    
    # now we have the project record created
    # and its id we can add the links to other things
    
    
    # put in code to determine funder, and if one of a stanard set then we can use this determine which logo
    # to add    
    
    
    proj_ref_obj = Referenceable.objects.get(uuid=project_uuid)
    
    
    # to add    
    # ceda_abbreviation  = proj_abbrev
    
    party_dict = {}
    
    if 'ceda_officer' not in party_dict :
        party_dict['ceda_officer'] = [('Garland','Wendy')]
    
    
    
    #make up other party_dict entries where these are supplied...
    
    if project_details['pi_last']:
        last_name_list = project_details['pi_last'].split('\n')
        first_name_list = project_details['pi_first'].split('\n')
        pi_list = []
        for i, last_name in enumerate(last_name_list):
            if i <= len(first_name_list):
                first_name = first_name_list[i]
            else:
                first_name = ''
            pi_list.append((last_name, first_name))
            
        party_dict['principal_investigator'] = pi_list

    if project_details['coi_last']:
        last_name_list = project_details['coi_last'].split('\n')
        first_name_list = project_details['coi_first'].split('\n')
        coi_list = []
        
        for i, last_name in enumerate(last_name_list):
            if i <= len(first_name_list):
                first_name = first_name_list[i]
            else:
                first_name = ''
            coi_list.append((last_name, first_name))
            
        party_dict['co_investigator'] = pi_list

    if project_details['funder']:
        last_name_list = project_details['funder'].split('\n')
        first_name = ''
        funder_list = []
        for last_name in last_name_list:
           funder_list.append((last_name, first_name))
            
        party_dict['funder'] = funder_list
    
    # having determined our parties, throw this into the add_parties function to add the related parties 
    mbt.add_parties(party_dict,faam_proj)
            
    return project_id
    
    
def proj_updater(project_details):
    """
        attempt to use details that Poppy has gathered to provide a more detailed project description
    """
    
    
def faam_projects():
    
    """
        function to read in the project details file and create look-up dictionary
    """
    
    import csv
    import os
    import sys
    #import urllib2
    import getopt


    faam_proj_list_in = '/home/users/gparton/catalogue_scripts/faam_project_list.csv'
    
    proj_lines = {}
    parent_project_dict = {'EUFAR': Project.objects.get(uuid__exact='a0aebebc95412cadd236706b90419153')
                          ,u'Met Office FAAM Campaigns': Project.objects.get(uuid__exact='ae9d95078716251c53c396cf5b24941e')
                          ,u'Met Office Flights': Project.objects.get(uuid__exact='ae9d95078716251c53c396cf5b24941e') }
            
    with open(faam_proj_list_in, 'rb') as csvfile:
        proj_stuff = csv.reader(csvfile)
        
        for row in proj_stuff:
            log.debug(row )   
            if row[0] == 'Abbreviated title':
                continue
            elif row == '':
                continue
            
            #Project name,
            #Info,
            #URL on FAAM website ,
            #URL of MOLES project record,
            # parent entry ***** NEW
            #PI surname,
            #PI first name,
            #Funder,
            #Other (eg. dataset record),
            #Comments

            title_string = ''
            abstract_string = ''      
            moles_proj_uuid = None
            proj_ob = None
            
            
            #if existing Project record has been given, taken those details
            try:
            
                if row[4] != '':

                    # get stuff from existing record
                    # first just strip out the uuid:
                    log.debug(row[4])
                    if "http" in row[4]:
                        uuid_from_url = row[4].replace('http://catalogue.ceda.ac.uk/uuid/','')

                    else:
                        uuid_from_url = row[4]
                    log.debug('uuid is', uuid_from_url)
                    proj_ob = Project.objects.get(uuid__exact=uuid_from_url)    


                else:

                    #stuff from file

                    if row[1].strip() != '':
                        title_string = row[1].decode('cp1252').encode('utf-8')

                    else:
                        title_string = row[0] + ' Project Details'

                    abstract_string  = row[2].decode('cp1252').encode('utf-8')#unicode(row[2], "utf-8")

                    if abstract_string == '' :
                        abstract_string = 'Project details needed. Please contact CEDA for additional information.'



                    if row[5].strip() != '':
                        try: 
                            parent_project = parent_project_dict[row[5].strip()]
                        except:
                            if "http" in row[5]:
                                parent_uuid = row[4].replace('http://catalogue.ceda.ac.uk/uuid/','')

                            else:
                                parent_uuid = row[5]
                            parent_project = Project.objects.get(uuid__exact=row[5].strip())
                    else:
                        parent_project = None

                    if not abstract_string:
                        abstract_string = 'Need to write an abstract'




                    proj_details =  {'title' : title_string
                                    , 'abstract' : abstract_string
                                    , 'faam_site_url' : row[3]
                                    , 'moles_project_record_url' : moles_proj_uuid
                                    , 'parent_project' : parent_project
                                    , 'pi_last' : row[6]
                                    , 'pi_first' : row[7]
                                    , 'funder' : row[8]
                                    , 'coi_last': row[9]
                                    , 'coi_first': row[10]
                                    , 'poc_last' : row[11]
                                    , 'poc_first' : row[12]
                                    , 'location_name': row[13]
                                    , 'moles_ob_id': proj_ob                                  
                                       }

                    proj_ob = proj_maker(row[0],proj_details)

                proj_lines[row[0].strip()] = proj_ob

    
            except:
                continue     
            
    #make the output list we'll wrire alphabetical using collections.OrderedDict()
    proj_lines_ordered = collections.OrderedDict(sorted(proj_lines.items(), key=lambda t: t[0]))
            
    update_proj_file(proj_lines_ordered)
    
    os.rename('/home/users/gparton/catalogue_scripts/faam_project_list.csv.updated', '/home/users/gparton/catalogue_scripts/faam_project_list.csv')
        
    return proj_lines
    
    

def update_proj_file(proj_details):

    """
    Function to output the updated project details into a file that replaces the one read in.
    This should then ensure that we're re-using projects and not creating a whole new bunch.
    
    """
    
    faam_proj_list_out = '/home/users/gparton/catalogue_scripts/faam_project_list.csv.updated'
    
    
    
    with open(faam_proj_list_out,'wb') as proj_csv_out:
        spamwriter = csv.writer(proj_csv_out)
        headerLine = ['Abbreviated title', 'full title', 'abstract', 'faam_site_url', 'moles_project_record_url', 'parent_project' ,'pi_last', 'pi_first', 'funder','coi_last','coi_first','poc_last','poc_first','location']
        spamwriter.writerow(headerLine)
        
        
        for key, value in proj_details.items():
            
            parent_uuid = None
            
            if value.parentProject:
                parent_uuid = value.parentProject.uuid    
            else:
                parent_uuid = None            
          
            spamwriter.writerow([key
                                ,value.title
                                ,'now in MOLES'
                                ,'now in MOLES'
                                ,'http://catalogue.ceda.ac.uk/uuid/%s'% value.uuid
                                ,parent_uuid
                                ,'now in MOLES'
                                ,'now in MOLES'
                                ,'now in MOLES'
                                ,'now in MOLES'
                                ,'now in MOLES'
                                ,'now in MOLES'
                                ,'now in MOLES'
                                ,'now in MOLES'
                                ]
                                )



        
# ================================== 
    
# Now the functions to get stuff from the flight
# folders in the archive

# ===================================    
    
    
def get_aircraft_platform_id(path):

    """
    function to take the path, find the aircraft set up for eventual use with EUFAR data too!)
    and then look up in a dictionary to get the platform ob_id and a preferred name to use in
    the title of subsequent records
    
    """
    aircraft_dir_name = 'undefined'
    
    if not re.search(r'faam',path):
        aircraft_dir_name = re.search(r'/badc/eufar/data/aircraft/(?P<aircraft>[a-z0-9\-]*)',path).groups()
    else:
        aircraft_dir_name = 'faam'    
    aircraft_dict = {'undefined': [None,None]
                    ,'faam': [Platform.objects.get(ob_id=51),'BAE-146', ImageDetails.objects.filter(ob_id__exact=8)]
    #               ,'awi-polar5':
    #               ,'dlr-do228-101':
    #               ,'dlr-do228-dcffu':
    #               ,'dlr-g550-halo':
    #               ,'enviscope-learjet':
    #               ,'enviscope-partenavia':
    #               ,'faam-bae146':
    #               ,'fub-ask16':
    #               ,'fub-c207':
    #               ,'fzk-enduro':
    #               ,'gtk-3in1twinotter':
    #               ,'ibimet-skyarrow':
    #               ,'inta-casa212-ar':
    #               ,'inta-casa212-rs':
    #               ,'kit-enduro':
    #               ,'nerc-do228':
    #               ,'nlr-citation':
    #               ,'nlr-metro2':
    #               ,'safire-atr42':
    #               ,'safire-fa20':
    #               ,'safire-piper-aztec':
    #               ,'seneca':
    #               ,'uniman-seaes-c182j':
                    }
    
    return aircraft_dict[aircraft_dir_name]



def read_flight_log(start_path):
    """
        script to try and pull out start and end times for the flight from the 
        the flight log
        
        need to also work out if times are in GMT or local time, if local.. yikes....
        
    """
    
    flight_details = {'start_time': None
                     ,'end_time': None
                      }
    flight_log_file_path = os.path.join(start_path,'flight-sum_faam_20130301_r0_b756.txt')
    
    if os.path.isfile(flight_log_file_path):
        flight_log_file = open(flight_log_file_path,'r')

        flight_log = flight_log_file.readlines()

        if len(flight_log) > 9:
            flight_details['start_time'] = flight_log[9].split(' ')[0]
            flight_details['end_time'] = flight_log[-1].split(' ' )[0]

    return flight_details
    
    
def flight_project_abbrev(start_path):
    """
        function to pull out the flight's project ID from the 00README file
    """


    read_me_file = open(os.path.join(start_path,'00README'))
    first_line = read_me_file.readline()
    proj_abbrev_bits = (' - ').join(first_line.split(' - ')[1:]).strip()
    
    
#    (' - ').join(read_me_file.readline().split(' - ')[1:]).strip()
    
    project_abbrev = []
    project_special_flight = None
    project_flight_number = None
    project_flight_extra = None
    
    
        
        
    proj_regex = re.compile(r'^(?P<project_abbrev>[a-zA-Z0-9\- \/]*?) ?(?P<special>Transit|Test|Pilot)? *Flight(s)? *(?P<project_flight_number>[a-zA-Z0-9\-\_\/]{1,})?(\s\((?P<project_flight_extra>[a-zA-Z0-9\-\_ \,\.\/\!\"\']*)\))*')
    
    
    
    
    if re.match(proj_regex,proj_abbrev_bits):
       
        read_me_project_lines_parts = re.search(proj_regex,proj_abbrev_bits).groupdict()
    
        project_abbrev_string = read_me_project_lines_parts['project_abbrev']
        
                
        project_abbrev = project_abbrev_string.strip().split('/')

        if 'special' in read_me_project_lines_parts:
            project_special_flight = read_me_project_lines_parts['special']#re.compile('(?P<special>Transit|Test|Pilot)')
        
        if 'project_flight_number' in read_me_project_lines_parts:
            project_flight_number = read_me_project_lines_parts['project_flight_number']

        if  'project_flight_extra' in read_me_project_lines_parts:
            project_flight_extra =  read_me_project_lines_parts['project_flight_extra']

    else:

        
        project_abbrevs = proj_abbrev_bits.split(' ')[0].strip()   
        if '/' in project_abbrevs:
            project_abbrev = sorted(project_abbrevs.split('/'))
        elif project_abbrevs == 'flight':
            pass
        else:
            project_abbrev.append(project_abbrev) 
           
    return project_abbrev, project_flight_number, project_flight_extra, project_special_flight

def find_instrument_groups(start_path):
    """
        function to determine the different sub-folders and thus the different instrumentation groups used on the flight
        and then to pull out the different instrument names from the NASA-Ames file names
    """
    
    instrument_details = {'groups':None
                         ,'instruments': None
                         }
    
    instrument_groups = glob.glob(os.path.join(start_path,'*/'))
    
    instrument_list = []
    group_list = []
    for group in instrument_groups:
        file_lists = glob.glob(group + '*.n[a|c]')
        for instrument_file in file_lists:
            instrument_list.append(os.path.basename(instrument_file).split("_")[0])
          
        group_list.append(os.path.basename(os.path.normpath(group)))
        
    instrument_details['groups'] = list(set(group_list))
    instrument_details['instruments'] = list(set(instrument_list))
    
    
    return instrument_details
    

def get_result_ob(internal_path):
    
    
    result_details = {'dataPath':internal_path
                     ,'fileFormat': 'Data are netCDF and NASA-Ames formatted. Ancillary files may be plain ASCII or PDF formatted. Image files may be PNG formatted.'
                     ,'curationCategory': CEDA_CurationValue.A
                     ,'numberOfFiles': 0
                     ,'volume': 0
                     ,'storageLocation': 'internal'
                     ,'storageStatus': 'online'
                     }
    
    result_ob = Result(**result_details)
    result_ob.save()
    
    
    return result_ob
    

def get_info_from_dir_paths(year_list=[], flight_num=None):
    """
     big controlling function to scrape info from the directories and to 
     create a big uber, master dictionary that will form the core of info 
     for the observation generation
     
    """
    starting_dir = ('/badc/faam/data/')

    dir_list = []
    
    if year_list:
    
        files_depth_2  = glob.glob(os.path.join(starting_dir,'[1-2]*/[bc]*'))  
        
        for last_year_to_scan in year_list:

            for directory in files_depth_2:
                if int(re.search(os.path.join(starting_dir,'([0-9]{4})'),directory).groups()[0]) == int(last_year_to_scan):

                    dir_list.append(directory)
    else:
        
        dir_list  = glob.glob(os.path.join(starting_dir,'*/%s*' % flight_num))   
        

                
    info_from_dir_paths = collections.OrderedDict()
    month_list = [x.lower() for x in list(calendar.month_abbr)]
        
    for flight_dir_path in dir_list:
        parent_dir, flight_number_date = os.path.split(flight_dir_path)
        flight_year = os.path.basename(parent_dir)
        flight_number,flight_month_char,flight_day = flight_number_date.split('-')
        
        flight_month = str(month_list.index(flight_month_char))
        
        if len(flight_month) < 2 :
            flight_month = '0' + flight_month
        if len(flight_day) < 2: 
            flight_day = '0' + flight_day
        
        aircraft_ob, aircraft_name, aircraft_logo = get_aircraft_platform_id(flight_dir_path)
        
        
        project_abbrev, project_flight_number, project_flight_extra, project_special_flight = flight_project_abbrev(flight_dir_path)
        
        instrument_details = find_instrument_groups(flight_dir_path)
        
        flight_log = read_flight_log(flight_dir_path)
                
        if not flight_log['start_time']:
            start_time = '000000'
        
        else:
            start_time = flight_log['start_time']
            
        if not flight_log['end_time']:
            end_time = '235959'
        else:
            end_time = flight_log['end_time']
        
        
        archive_start_date = datetime.datetime.strptime(flight_year+flight_month+flight_day+start_time,'%Y%m%d%H%M%S')
        archive_end_date = datetime.datetime.strptime(flight_year+flight_month+flight_day+end_time,'%Y%m%d%H%M%S')
         
        
        first_creation_time = datetime.datetime.fromtimestamp(os.stat(flight_dir_path).st_ctime)
        
        
        info_from_dir_paths[flight_number] = {'aircraft_name': aircraft_name
                                             ,'aircraft_ob': aircraft_ob
                                             ,'aircraft_logo': aircraft_logo
                                             ,'internal_path' : flight_dir_path
                                             ,'flight_number' : flight_number
                                             ,'flight_proj_abbrev' : project_abbrev
                                             ,'archive_flight_date' : {'startTime':archive_start_date,'endTime': archive_end_date}
                                             ,'project_flight_number': project_flight_number
                                             ,'project_flight_extra' : project_flight_extra
                                             ,'projet_special_flight': project_special_flight
                                             ,'instrument_groups': instrument_details['groups']
                                             ,'instrument_list': instrument_details['instruments']
                                             ,'creation_date' : first_creation_time
                                             }
    
    
    return info_from_dir_paths
    
    
    
    
def instrument_suite_text(groups):
    """
        the text that is to be used will depend on the sub-directories given in the archive
        possible directories are: 
     
            core_cloud_physics
            core_processed
            core_raw
            mo-non-core
            non-core
            non-core_processed

     
    """
    
    # first order the groups by name, then work out what we have
    plural = ''
    
    groups = '|'.join(sorted(groups)).strip()
    core = 0
    non_core = 0
    
    if re.search(r'core_',groups):
        core = 1
    if  re.search(r'non-core',groups):
        non_core = 1
    
        
    if core and non_core:
        instrument_combination = 'core and non-core'
        plural = 's'
    elif core:
        instrument_combination = 'core'
    elif non_core:
        instrument_combination = 'non-core'
            
    else :
        instrument_combination = 'various'
        plural = 's'
    
                
    return 'Airborne atmospheric measurements from %s instrument suite%s'% (instrument_combination, plural)

def get_result(internal_path):

    """
        checks to see if the result already exists and if so, throws a wobbly
        else it creates a new result based on the internal path and 
        then returns that object 
            
    """
    
    result_object = None
    
    return result_object
    
    
    
def poll_elastic_search_for_faam_details(flight_no):
    """
        function to take the flight number, construct a URL and then to poll the 
        elastic search info to get aggregated geographic and temporal extent info back
        
    """
    
    
    #elastic_search_url = "https://jasmin-es1.ceda.ac.uk:/faam/_search?pretty=true&&size=1&_source=misc.flight_info.flight_num,spatial.geometries.search.coordinates,temporal&q=misc.flight_info.flight_num:%s"% flight_no
    
    elastic_search_url = "https://jasmin-es1.ceda.ac.uk:/stac-finder-items/_search?pretty=true&&size=1&_source=properties.flight_num,geometry.search.coordinates,temporal&q=properties.flight_num:%s"% flight_no
    
   

    geo_spatial_info = None
    temporal_info = None
    
    es = CEDAElasticsearchClient()


#    query = {"_source": ["spatial.geometries","temporal"],
#                 "query": {
#                        "match_phrase_prefix": {
#                            "misc.flight_info.flight_num": flight_no
#                                                }
#                          }
#                }
    query = {"_source": ["geometry","properties"],
                 "query": {
                        "match_phrase_prefix": {
                            "properties.flight_num": flight_no
                                                }
                          }
                }
        
    try:
            
            #flight_info = es.search(index="faam", body=query, request_timeout=60)
            flight_info = es.search(index="stac-finder-items", body=query, request_timeout=60)
            
            point = {'lat':[], 'lon':[]}
            geo_types = set([])
            
            for hit in flight_info['hits']['hits']:
                


                if not geo_spatial_info or 'envelope' not in geo_types:

                    try:
                          #if 'search' in hit['_source']['spatial']['geometries']:
                        if 'search' in hit['_source']['geometry']:


                            if hit['_source']['spatial']['geometries']['search']['type'] == 'Point':
                                geo_spatial_return = flight_info['hits']['hits']['_source']['spatial']['geometries']['search']['coordinates']
                                geo_spatial_info = {'eastBoundLongitude': geo_spatial_return[0]
                                                   ,'westBoundLongitude': geo_spatial_return[0]
                                                   ,'northBoundLatitude': geo_spatial_return[1]
                                                   ,'southBoundLatitude': geo_spatial_return[1]
                                                   }
                                geo_types.add('point')

                            else:
                               # geo_spatial_return = hit['_source']['spatial']['geometries']['search']['coordinates']
                                geo_spatial_return = hit['_source']['geometry']['search']['coordinates']
                                geo_spatial_info = {'eastBoundLongitude': geo_spatial_return[1][0]
                                                   ,'westBoundLongitude': geo_spatial_return[0][0]
                                                   ,'northBoundLatitude': geo_spatial_return[0][1]
                                                   ,'southBoundLatitude': geo_spatial_return[1][1]
                                                   }
                                geo_types.add('envelope')

                        elif 'display' in hit['_source']['spatial']['geometries']:

                            if hit['_source']['spatial']['geometries']['display']['type'] == 'Point':
                                geo_spatial_return = flight_info['hits']['hits']['_source']['spatial']['geometries']['display']['coordinates']
                                geo_spatial_info = {'eastBoundLongitude': geo_spatial_return[0]
                                                   ,'westBoundLongitude': geo_spatial_return[0]
                                                   ,'northBoundLatitude': geo_spatial_return[1]
                                                   ,'southBoundLatitude': geo_spatial_return[1]
                                                   }
                                geo_types.add('point')


                            else:
                                geo_spatial_return = hit['_source']['spatial']['geometries']['display']['coordinates']
                                geo_spatial_info = {'eastBoundLongitude': geo_spatial_return[1][0]
                                                   ,'westBoundLongitude': geo_spatial_return[0][0]
                                                   ,'northBoundLatitude': geo_spatial_return[0][1]
                                                   ,'southBoundLatitude': geo_spatial_return[1][1]
                                                   }

                                geo_types.add('envelope')





                    except:
                        pass

                    


            if not temporal_info :

                try:

                    temporal_return = (flight_info['hits']['hits'][0]['_source']['properties']['start_datetime'],flight_info['hits']['hits'][0]['_source']['properties']['end_datetime'])
                    #print("start_time=",temporal_return[0])
                    if re.match(u'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{1,6}',temporal_return[0]):
                        temporal_info = {'startTime': datetime.datetime.strptime(temporal_return[0], '%Y-%m-%dT%H:%M:%S.%f')
                                ,'endTime': datetime.datetime.strptime(temporal_return[1],'%Y-%m-%dT%H:%M:%S.%f')
                                }
                    else:
                    
                        temporal_info = {'startTime': datetime.datetime.strptime(temporal_return[0], '%Y-%m-%dT%H:%M:%S')
                                ,'endTime': datetime.datetime.strptime(temporal_return[1],'%Y-%m-%dT%H:%M:%S')
                                }
                                
                                
                                
                    
                except:
                    pass
    except:
            pass

    
    
    return geo_spatial_info, temporal_info

    
def flight_observation_creator(flight_no, flight_details, proj_obs):
    
    """
        this is the script to start take things in construct all the required items in turn
        
    """
    
    proj_title = 'unnamed project'
    proj_abbrev = ''
    
    



    if flight_details['projet_special_flight']:
        project_special_flight_text = '%s '% flight_details['projet_special_flight']    
    else:
        project_special_flight_text = ''
        
    if len(proj_obs) >= 1:
        proj_title = 'for %s'% proj_obs[0].title
        if proj_title[-1] == '.':
            proj_title = proj_title[:-1]
        if not flight_details['flight_proj_abbrev'][0] in proj_title:
            proj_title = proj_title + " (%s)"% flight_details['flight_proj_abbrev'][0]
       
        
        if len(proj_obs) > 2:
            for counter, mid_proj in enumerate(proj_obs[1:-1]):
                proj_title = proj_title + ', %s'% mid_proj.title
                if proj_title[-1] == '.':
                    proj_title = proj_title[:-1]

                if not flight_details['flight_proj_abbrev'][0] in proj_title:
                    proj_title = proj_title + " (%s)"% flight_details['flight_proj_abbrev'][counter]


        if len(proj_obs) >= 2:
            proj_title = proj_title + ' and %s'% proj_obs[-1].title
            if proj_title[-1] == '.':
                proj_title = proj_title[:-1]

            if not flight_details['flight_proj_abbrev'][0] in proj_title:
                proj_title = proj_title + " (%s)"% flight_details['flight_proj_abbrev'][-1]

        # just in case the abbreviation isn't already in the long title we'll check and add if needed 
        
       
       
       
    if "project" not in proj_title or "Project" not in proj_title or "projects" not in proj_title or "Projects" not in proj_title:
        if len(proj_obs) == 1:
            proj_title = proj_title + ' project'
        else:
            proj_title = proj_title + ' projects'
            
    if len(proj_obs) > 1 and proj_title[-7:] == 'project':
        proj_title = proj_title + 's'

    if proj_title[-1] == '.':
            proj_title = proj_title[:-1]
       
    if len(flight_details['flight_proj_abbrev']) >= 1:
        proj_abbrev = flight_details['flight_proj_abbrev'][0]
        
        if len(flight_details['flight_proj_abbrev']) > 2:
        
            for mid_abbrev in flight_details['flight_proj_abbrev'][1:-1]:
                proj_abbrev = proj_abbrev + ', ' + mid_abbrev
        
        if len(flight_details['flight_proj_abbrev']) >= 2:
                proj_abbrev = proj_abbrev + ' and ' + flight_details['flight_proj_abbrev'][-1]
                
    
                            
    title_items = {'aircraft': flight_details['aircraft_name']
                      , 'flight_no': flight_no.upper()
                      , 'flight_proj_abbrev' : proj_abbrev
                      , 'project_flight_number' : flight_details['project_flight_number']
                      , 'instrument_suite' : instrument_suite_text(flight_details['instrument_groups'])
                      , 'proj_long_title' : proj_title
                      , 'special_flight' : project_special_flight_text 
                      } 
    
 
    #Abstract needs to be constructed to bring together:
    
    #Flight date-time
    #Flight number (bXXX)
    #Flight number in series if avaible (e.g. flight 1 for SAMBAA)
    #Project acronym
    #Project long name
    #(PI, Funder)
    #Instrument suite and list of non-core instruments (if available)
    #?location_name?
 
    
    
    
  
    if not flight_details['project_flight_number'] :

           
        title = "FAAM %(flight_no)s %(flight_proj_abbrev)s %(special_flight)sflight: %(instrument_suite)s on board the %(aircraft)s aircraft" % title_items
        abstract_text = '%(instrument_suite)s data on board the FAAM %(aircraft)s aircraft collected %(proj_long_title)s.'% title_items        

    elif re.match(r'[0-9]{1,2}',flight_details['project_flight_number'].strip()):
        
    
        title = "FAAM %(flight_no)s %(flight_proj_abbrev)s %(special_flight)sflight, number %(project_flight_number)s: %(instrument_suite)s on board the %(aircraft)s aircraft" % title_items 
        abstract_text = '%(instrument_suite)s data on board the FAAM %(aircraft)s aircraft during flight %(project_flight_number)s %(proj_long_title)s.'% title_items
    else : 
    
        title = "FAAM %(flight_no)s %(flight_proj_abbrev)s %(special_flight)sflight, %(project_flight_number)s: %(instrument_suite)s on board the %(aircraft)s aircraft" % title_items 
        abstract_text = '%(instrument_suite)s data on board the FAAM %(aircraft)s aircraft, %(project_flight_number)s flight %(proj_long_title)s.'% title_items
    
  
    
    # now to get geo-temporal details from elastic search response
    
    geog_extent_dict, temporal_extent_dict = poll_elastic_search_for_faam_details(flight_no.lower()) 
    
    # and to link up with unique geographic and temporalExtents if we have this info..
    
        
    if geog_extent_dict:
        geo_extent_ob = GeographicBoundingBox(**geog_extent_dict)
        geo_extent_ob.save()
        flight_details['geog_extent_dict'] = geog_extent_dict
        
    else:
        geo_extent_ob = None
    
    flight_details['geog_extent_ob'] = geo_extent_ob
    
    if temporal_extent_dict:
        temporal_extent_ob = TimePeriod(**temporal_extent_dict)
        temporal_extent_ob.save()
        flight_details['temportal_extent_dict'] = temporal_extent_dict

    elif flight_details['archive_flight_date']:
        temporal_extent_ob = TimePeriod(**flight_details['archive_flight_date'])
        temporal_extent_ob.save()
    
    else:
        temporal_extent_ob = None

    flight_details['temportal_extent_ob'] = temporal_extent_ob


    key_words_list = []
    
    key_words_list.extend(flight_details['flight_proj_abbrev'])
    key_words = ', '.join(key_words_list)
    flight_details['key_words'] = key_words + ', FAAM, airborne, atmospheric measurments'
    
    # Need to make sure we link this up to the FAAM Observation Collection:
    faam_collection_ob = ObservationCollection.objects.filter(uuid__contains='affe775e8d8890a4556aec5bc4e0b45c')[0]
    
    
    if proj_obs:
        for proj_ob in proj_obs:
        
            try:
                proj_onlineresources = proj_ob.onlineresource
            except:
                proj_onlineresources = None
    else:
        proj_onlineresources = None
    
    
    up_freq = MD_MaintenanceFrequencyCode.asNeeded
    if int(flight_details['internal_path'].split('/')[4]) > 2010:
        up_freq = MD_MaintenanceFrequencyCode.notPlanned
        
    
    faam_observation_details = {'abstract': abstract_text
                ,'dataLineage' : 'Data were collected by instrument scientists during the flight before preparation and delivery for archiving at the Centre for Environmental Data Analysis (CEDA).'
                ,'dataPublishedTime': flight_details['creation_date']
                ,'geographicExtent' : geo_extent_ob 
                ,'keywords' : flight_details['key_words']
                ,'language' : 'English'
                ,'publicationState' : MO_PublicationStateValue.published
                ,'result_field' : get_result_ob(flight_details['internal_path'])
                ,'resultQuality' : DQConformanceResult.objects.get(ob_id__exact=3074)
                ,'status' : MD_ProgressCode.ongoing
                ,'title' : title
                ,'timePeriod': temporal_extent_ob
                ,'updateFrequency' : up_freq
                }
    
    try:
        new_faam_obby = Observation(**faam_observation_details)
        new_faam_obby.save()        
    except:
        return
    party_dict = {}
    
    if 'ceda_officer' not in party_dict :
        party_dict['ceda_officer'] = [('Garland','Wendy')]

    
    if 'author' not in party_dict:
        party_dict['author'] = [('FAAM','')
                               ,('NERC','')
                               ,('MET OFFICE','')
                               ]



    
    # having determined our parties, throw this into the add_parties function to add the related parties 
    mbt.add_parties(party_dict, new_faam_obby)

   
    #new_faam_obby.result = 'onlineresource' : proj_onlineresources # share the same ones as on the project record
        
    # adding into the FAAM collection
    
    faam_collection_ob.member.add(new_faam_obby)
    faam_collection_ob.save()
    
    # now add into the Project's collection(s):
    

    for abbrev_counter, proj_ob in enumerate(proj_obs):
        
        new_faam_obby.projects.add(proj_ob)
        
        
        if proj_ob.observationCollection.values():
            
            for ob_col_details in proj_ob.observationCollection.values():

                ob_col = ObservationCollection.objects.get(uuid__exact=ob_col_details['uuid'])

                ob_col.member.add(new_faam_obby)
                ob_col.save()
        else:
            # OK, the Project doesn't have a collection already, so we'll create one 
            col_title_items = {'aircraft': flight_details['aircraft_name']
                              , 'flight_proj_abbrev' : flight_details['flight_proj_abbrev'][abbrev_counter]
                              , 'proj_long_title' : proj_ob.title
                              } 

            if col_title_items['flight_proj_abbrev'] not in col_title_items['proj_long_title']:
                col_title_items['proj_long_title'] = col_title_items['proj_long_title'] + ' (%s)'% col_title_items['flight_proj_abbrev']
                
            project_collection_title =  "%(flight_proj_abbrev)s: in-situ airborne observations by the FAAM %(aircraft)s aircraft" % col_title_items       
            

            project_collection_abstract ='In-situ airborne observations by the FAAM %(aircraft)s aircraft for %(proj_long_title)s.'% col_title_items

            new_ob_col_dict = {'title': project_collection_title
                              ,'abstract': project_collection_abstract
                              ,'dataPublishedTime': flight_details['creation_date']
                              ,'keywords' : flight_details['key_words']
                              ,'publicationState' : MO_PublicationStateValue.working
                              }
                              
            new_ob_col = ObservationCollection(**new_ob_col_dict)
            new_ob_col.save()
            new_ob_col.member.add(new_faam_obby)
            new_ob_col.save()

            proj_ob.observationCollection.add(new_ob_col)

            try:
                proj_logo_ob = ImageDetails.objects.get(ob_id__exact=proj_ob.imageDetails.values()[0]['ob_id'])[0]
            except:
                proj_logo_ob = flight_details['aircraft_logo'] 
            
            #new_ob_col.imageDetails = proj_logo_ob



            # having determined our parties, throw this into the add_parties function to add the related parties 
            mbt.add_parties(party_dict, new_ob_col)


    new_faam_obby.imageDetails.add(flight_details['aircraft_logo'].first())  # set to FAAM logo as standard # could change this to project logo if needed...   
    new_faam_obby.save()
    
    #now set link to Constraint object
    
    new_faam_obby.permission = Constraints.objects.get(ob_id = 2033)
    new_faam_obby.save()
    #pos.permissions_checker(new_faam_obby,0)
    
    
    new_faam_obby.procedureAcquisition = make_acquisition(flight_no, flight_details, party_dict)
    new_faam_obby.save()
    
    # Now to add in online Resources for the flight:
    
    flight_log_files  = check_for_flight_logs(flight_details['internal_path'], new_faam_obby)
    
                                         
    # add in link to EFF tool
    
    
    
    eff_info = {'linkage':'http://flight-finder.ceda.ac.uk/?index=faam'
               ,'function':'dataService'
               ,'relatedTo': new_faam_obby
               ,'name': 'FAAM flights in the EUFAR Flight Finder Tool'
                }

    eff_tool = OnlineResource(**eff_info)
    eff_tool.save()            
    
    new_faam_obby.save()
    #sys.exit()

def check_for_flight_logs(flight_path, record_ob):
    """
    does a quick search for flight log and summary files in the flight directory in the archive
    
    """

    fp = glob.glob(os.path.join(flight_path,'flight-*.html'))
    
    for flight_log in fp:
        
        
        flight_no = re.search(r'(?P<no>[a-z]{1}[0-9]{3})', flight_path).groupdict()['no'] 
        
        log.info("%r | %r |%r", flight_no, flight_log, record_ob.title)
        
        
        new_doc_info = {'linkage': 'http://data.ceda.ac.uk%s'% flight_log
                  ,'function': 'documentation'
                  ,'relatedTo': record_ob
                  }
        
        if 'sum' in flight_log:
            new_doc_info['name'] = 'Flight summary file for FAAM BAE-146 flight %s'% flight_no.upper()
            
        elif 'log' in flight_log:
            new_doc_info['name'] = 'Flight log for FAAM BAE-146 flight %s'% flight_no.upper() 
        
        elif 'track' in flight_log:
            new_doc_info['name'] = 'Flight track for FAAM BAE-146 flight %s'% flight_no.upper() 
        
        else:
            continue
            
        new_doc = OnlineResource(**new_doc_info)
        new_doc.save()
           
    return



def add_faam_mpo(flight_no, flight_details, party_dict, accy_ob):
    """
    function to create a mobile platform operation for a
    faam flight, based on:
    1) flight number
    2) geographic and temporal info obtained for obby
    3) flight log and summary files if found in the archive
    4) standard details
    """
    
     
    mpo_ob = None    

        
        
    faam_mpo_info = {'title': 'FAAM BAE-147 flight %s'% flight_no.upper()
                    ,'abstract': "Flight details for FAAM BAE-146 aircraft flight number %s. See linked documentation for further details." % flight_no.upper()
                    ,'platform_field' : Platform.objects.get(ob_id = 51)
                    ,'status' : MD_ProgressCode.completed
                    ,'operationTime' : flight_details['temportal_extent_ob']
                    ,'location': flight_details['geog_extent_ob'] 
                    }
    
    
    
    
    if MobilePlatformOperation.objects.filter(title__exact = faam_mpo_info['title']):
        faam_mpo = MobilePlatformOperation.objects.get(title = faam_mpo_info['title'])  
    else:
        faam_mpo = MobilePlatformOperation(**faam_mpo_info)
        faam_mpo.save()
   
        flight_log_files = check_for_flight_logs(flight_details['internal_path'], faam_mpo)
         
        faam_mpo.save()
    
   
    
        mpo_party_dict  = {}

            
        if 'metadata_owner' not in party_dict:
            party_dict['metadata_owner'] = [('CEDA','')]
    
        if 'point_of_contact' not in party_dict:
            party_dict['point_of_contact'] = [('CEDA','')]

        for role in ['ceda_officer', 'metadata_owner']:
            mpo_party_dict[role] = party_dict[role]

        # having determined our parties, throw this into the add_parties function to add the related parties 

        mbt.add_parties(mpo_party_dict, faam_mpo)

    
    accy_ob.mobilePlatformOperation.add(faam_mpo)

    return


def make_instrument(abbrev, party_dict):

    """
    Makes a new Instrument record based on the abbreviation given
    This will then need to be completed later on by Wendy
    """
    
    insty_details = {'title': 'New Instrument: %s'% abbrev
                    ,'abstract': 'New instrument created, more details to follow for instrument %s'% abbrev
                    }
    
    
    insty_ob = Instrument.objects.create(**insty_details)
         
    insty_party_dict  = {}
            
        
    if 'metadata_owner' not in party_dict:
        party_dict['metadata_owner'] = [('CEDA','')]
    
    if 'point_of_contact' not in party_dict:
        party_dict['point_of_contact'] = [('CEDA','')]

    for role in ['ceda_officer', 'metadata_owner']:
        insty_party_dict[role] = party_dict[role]

    # having determined our parties, throw this into the add_parties function to add the related parties 

    mbt.add_parties(insty_party_dict, insty_ob)
    
    id_details = {'relatedTo': insty_ob
                 ,'identifierType': 'ceda_abbreviation'
                 ,'url': abbrev.strip()
                 }
    id_added = Identifier.objects.create(**id_details)
    

    return insty_ob
    
def make_acquisition(flight_no, flight_details, party_dict):
    """
    now to make the necessary acquisition
    """
    
    accy_ob = None
    
    
    accy_details = {'title' : "FAAM Flight %s Acquisition" % flight_no.upper()
                   ,'abstract' : "FAAM Flight %s Acquisition" % flight_no.upper()
                   }
    
    
    # fortunatley, we know that all the instruments were mounted on the same platform, so it's just 
    # a matter of creating instrument-platform pairs..
    
    accy_ob = Acquisition.objects.create(**accy_details)
    
    #accy_ob.platform.add(flight_details['aircraft_ob'])
    #accy_ob.save()
    
    accy_ob.imageDetails.add(flight_details['aircraft_logo'].first())
    accy_ob.save()
    
    for instrument in flight_details['instrument_list']:
        
        
        
        try:
            inst_ob = Instrument.objects.get(uuid__exact=Identifier.objects.filter(identifierType__exact="ceda_abbreviation").filter(url__exact=instrument.strip()).first().relatedTo.uuid)
        
        except:
        # couldn't find a match, so we'll create the instrument record to be populated later on
        
            inst_ob = make_instrument(instrument, party_dict)        
           
        inst_plat_pair_ob = InstrumentPlatformPair.objects.create(instrument=inst_ob, platform = flight_details['aircraft_ob'], relatedTo = accy_ob)        
            
    # get a party dictionary by selecting bits from the earlier party_dict...           
            
    accy_party_dict  = {}
            
        
    if 'metadata_owner' not in party_dict:
        party_dict['metadata_owner'] = [('CEDA','')]
    
    if 'point_of_contact' not in party_dict:
        party_dict['point_of_contact'] = [('CEDA','')]

    for role in ['ceda_officer', 'metadata_owner']:
        accy_party_dict[role] = party_dict[role]

    # having determined our parties, throw this into the add_parties function to add the related parties 

    mbt.add_parties(accy_party_dict, accy_ob)

    # now to add in mobile plaform operation for the flight track
    # we'll do this by cloning the existing FAAM MPO record's details
        
    add_faam_mpo(flight_no, flight_details, party_dict, accy_ob)
    
    
          
    return accy_ob
                
def main( test_flag, year_list = [], flight_num = ''):
    """
    Controls whole process by calling the relevant pieces bit by bit
    """
    
    # so if not called from another script, then lets see is there is a command line argument to use

    
    # first gather the info from the archive directories
       
    flight_dictionary = get_info_from_dir_paths(year_list, flight_num)    
    
        
    
    # then take each flight in turn and construct the Obseration record
    
    if test_flag:
        number_of_flights_to_process = int(test_flag)
        
        
    else:
        number_of_flights_to_process = len(flight_dictionary)
    
    number_of_processed_flights = 0
    log.info("max number of new flights made in this run: %r", number_of_flights_to_process)
    log.info("starting to process flights...")


     
    for flight_number, flight_details_from_archive in flight_dictionary.items():
    
    
        log.info("attempting to do %r out of a potential %r", number_of_processed_flights+1, len(flight_dictionary))

        flight_abbrev_for_project = flight_details_from_archive['flight_proj_abbrev']
        project_records = []



        if (not Result.objects.filter(dataPath = flight_details_from_archive['internal_path'])) and flight_abbrev_for_project:


                for proj_abbrev in flight_abbrev_for_project:

                    # look up using the project abbreviation, or create an outline proj record:

                    project_records.append(get_faam_project(proj_abbrev.upper()))


                flight_observation_creator(flight_number, flight_details_from_archive, project_records)        
                number_of_processed_flights += 1
                
                

        else:

            log.info('flight already exists - not re-done')

        
        if number_of_processed_flights == number_of_flights_to_process:
            
            break

            
if __name__ == "__main__":



    arg_list = sys.argv[1:]

    try:
        opts, args = getopt.getopt(arg_list, "vt:s:e:f:")


        """
        v = verbose
        t = test only - works on just a sample set
        s = start year
        e = end year
        f = flight number
        """
    except getopt.GetoptError as ex:
        print('woops - problem with trying to call the script')
        raise ex
        sys.exit(2)

    #TO DO - add in option to get just a flight!
    
    
    verbose = 0
    test_run = 0
    start_year = ''
    end_year = ''
    flight_num = ''

    for opt,argu in opts:
        
        if "-v" in opt:
            verbose = 1
        elif "-t" in opt:
            #log.info('test run activated')
            test_run = argu
            print('will run test for %s new flights'% test_run)
        elif "-s" in opt:
            start_year = int(argu)
            
            assert 2004 <= start_year <= end_year 
        elif "-e" in opt:
            end_year = int(argu)
            assert 2004 <= start_year <= end_year

        elif "-f" in opt:
            flight_num = argu
            
            assert re.match('([a-z]{1}[0-9]{3})',flight_num)            
        
        # make a logger for this process
        log = logging.getLogger(__name__)
        if verbose:
            log.setLevel(logging.INFO)
        else:
            log.setLevel(logging.WARNING)

        log.info('Running in verbose mode')

        

    # can't have both a year and flight number selected.
    assert not (flight_num and start_year)
    
    print(flight_num)
    

    if start_year and end_year == '' :
        end_year = start_year
    elif start_year == '' and end_year == '' and flight_num == '':
        start_year = datetime.datetime.now().year
        end_year = datetime.datetime.now().year

        
    elif start_year == '' and not end_year == '':
        raise 'need start year'
                    
    if start_year:
        year_range = range(start_year, end_year + 1)
    else:
        year_range = None
    
    main(test_run, year_range, flight_num)

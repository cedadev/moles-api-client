
import click
import re
import datetime
from collections import defaultdict


from utils import get_client

from moles_api_v_3_client.api.observations import observations_list
from moles_api_v_3_client.api.projects import projects_list
from moles_api_v_3_client.api.rpis import rpis_list
from moles_api_v_3_client.models.rpis_list_role import RpisListRole
from moles_api_v_3_client.client import AuthenticatedClient, Client

PARTIES = {
    11: 'NERC',
    541: 'NCEO',
    387: 'NCAS',
}

def matchgrant(string):
    if string is None: 
        return
    m = re.search(r"(NE/\w+/\d)", string)

    if m: 
        return m.group(1)
    return None

def get_obs(pubfy):
    response = observations_list.sync_detailed(
        client=CLIENT, 
        data_published_time_gte=datetime.date(pubfy, 4, 1),
        data_published_time_lte=datetime.date(pubfy + 1, 3, 31)
        )
    if response.status_code.value == 200:
        return response.parsed.results
    return None
   
def fetch_rpis_obs_author():
    output = defaultdict(list)
    
    res = rpis_list.sync_detailed(client=CLIENT, role=RpisListRole.AUTHOR, party_ob_id_in=PARTIES)
    rpis = res.parsed.results
    
    for r in rpis:
        short_code = r.related_to.short_code
        if short_code != 'ob':
            continue
        ob_id = r.related_to.ob_id
        output[ob_id].append(r)
        
    return output

def fetch_rpis_project_funder():
    output = defaultdict(list)
    
    res = rpis_list.sync_detailed(client=CLIENT, role=RpisListRole.FUNDER, party_ob_id_in=PARTIES)
    rpis = res.parsed.results
    
    for r in rpis:
        short_code = r.related_to.short_code
        if short_code != 'proj':
            continue
        ob_id = r.related_to.ob_id
        output[ob_id].append(r)
        
    return output
    
@click.command(context_settings={'help_option_names': ['-h', '--help']})
@click.option("--pubfy", type=int)
def scanobs(pubfy):
    global CLIENT 
    
    CLIENT = get_client()
    
    obs = get_obs(pubfy)
    
    obs_authors = fetch_rpis_obs_author()
    proj_funders = fetch_rpis_project_funder()
    
    for ob in obs:
        grants = set()
        
        # Match grant pattern
        for text in [ob.title, ob.abstract, ob.keywords]:
            grant = matchgrant(text)
            if grant:
                grants.add(grant)
                
        # check authors        
        authors = obs_authors[ob.ob_id]
        for a in authors:
            party_id = a.party.ob_id 
            if party_id not in PARTIES:
                continue
            grants.add(f'Author_{PARTIES[party_id]}')

        for project in ob.projects:
            for text in [project.title, project.abstract]:
                grant = matchgrant(text)
                if grant:
                    grants.add(grant)

            funders = proj_funders[project.ob_id]
            
            # check authors        
            authors = obs_authors[ob.ob_id]
            for a in authors:
                party_id = a.party.ob_id 
                if party_id not in PARTIES:
                    continue
                grants.add(f'Funder_{PARTIES[party_id]}')


        if len(grants) > 0:
            click.secho(ob.uuid, bold=True, nl=False)
            for g in grants: click.secho(f" {g}", fg="red", nl=False)
            click.secho()
        

if __name__ == '__main__':
    scanobs()

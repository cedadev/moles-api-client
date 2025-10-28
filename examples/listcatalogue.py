import os
import sys
import click
import datetime
from collections import defaultdict


from moles_api_v_3_client.api.observations import observations_list
from moles_api_v_3_client.client import AuthenticatedClient, Client

from moles_api_v_3_client.api.rpis import rpis_list
from moles_api_v_3_client.models.rpis_list_role import RpisListRole

from moles_api_v_3_client.api.observationcollections import observationcollections_list

def get_client():
    token = os.environ.get("API_TOKEN")
    base_url = os.environ.get("API_URL")
    if token:
        return AuthenticatedClient(base_url=base_url, token=token)
    return Client(base_url=base_url)

def input2obs(fh):
    uuids = []
    for line in fh:
        line = line.strip()
        if line == "":
            continue
        uuid = line.split()[0]
        if len(uuid) != 32:
            continue
        uuids.append(uuid)
   
    response = observations_list.sync_detailed(client=CLIENT, uuid_in=uuids) 
    if response.status_code.value != 200:
        raise RuntimeError(f'API response: {response.status_code}')
    
    return response.parsed.results

def cat_filter(title, project, collection, path, state, pubfy, officer):
    """Use django filter to make an obs list."""
    params = {}
    
    if title:
        params['title_contains'] = title
    
    if project:
        params['projects_uuid'] = project
        
    if path:
        params['result_field_data_path_startswith'] = path
    
    if pubfy:
        params['data_published_time_gte'] = datetime.date(pubfy, 4, 1)
        params['data_published_time_lte'] = datetime.date(pubfy + 1, 3, 31)
    
    obs_id_filter = set()
    
    if collection:
        res = observationcollections_list.sync_detailed(client=CLIENT, uuid=collection)
        for col in res.parsed.results:
            for obs in col.member:
                obs_id_filter.add(obs.ob_id)

    if officer:
        res = rpis_list.sync_detailed(client=CLIENT, role=RpisListRole.CEDA_OFFICER, party_ob_id=officer)
        for rpi in res.parsed.results:
            obs_id_filter.add(rpi.related_to.ob_id)
    
    if obs_id_filter:
        params['ob_id_in'] = list(obs_id_filter)
    
    response = observations_list.sync_detailed(client=CLIENT, **params)

    return response.parsed.results

def fetch_authors(obs):
    ob_ids = [ob.ob_id for ob in obs]
    res = rpis_list.sync_detailed(client=CLIENT, role=RpisListRole.AUTHOR, related_to_ob_id_in=ob_ids)
    authors = res.parsed.results
    
    author_map = defaultdict(list)

    
    for author in res.parsed.results:
        ob_id = author.related_to.ob_id
        first_name = author.party.first_name
        last_name = author.party.last_name
        author_map[ob_id].append({
            'first_name': first_name,
            'last_name': last_name
        })
    
    return author_map

def show_list(obs, show_fields):
    authors = fetch_authors(obs)
    
    for ob in obs:
        click.secho(ob.uuid, bold=True, nl=False)
        for field in show_fields:
            if field == 't':
                click.secho(f" {ob.title}", fg="green", nl=False)
            if field == "p":
                for project in ob.projects:
                    click.secho(f" proj:{project.uuid}", fg="bright_yellow", nl=False)
            if field == "c":
                for collection in ob.observationcollection_set:
                    click.secho(f" coll:{collection.uuid}", fg="magenta", nl=False) 
            if field == "s":
                click.secho(f" [{ob.status}]", bg="yellow", nl=False)
            if field == "P":
                click.secho(f" [{ob.publicationState}]", reverse=True, nl=False)
            if field == "a":
                for author in authors[ob.ob_id]:
                    click.secho(f" author:{author.firstName} {author.lastName}", fg="blue", nl=False)
            if field == "r":
                if ob.result_field is not None:
                    click.secho(f" {ob.result_field.data_path}", fg="red", nl=False)
                else:
                    click.secho(" NO_RESULT_PATH", fg="red", bold=True, nl=False)
        click.echo("")


@click.command(context_settings={'help_option_names': ['-h', '--help']})
@click.option('--title', help="List observasions containing the title text.")
@click.option('--project', help="List observasions from a project.")
@click.option('--collection', help="List observasions from a collection.")
@click.option('--path', help="List observasions with paths starting <path>.")
@click.option('--state', help="List observasions from in a state.")
@click.option('--pubfy', type=int, help="List observasions publication financal year.")
@click.option('--officer',  help="List obs with CEDA officer.")
@click.option('--listing', help="""Use the listing file as source. This ignores 
                                   options like --title. The listing file must have a uuid at 
                                   the start of each line.""", type=click.File('r'))
@click.option('--show', default="t", help="""fields to show after the uuid. t=title, p=project uuid, 
                                 c=collection uuid, s=state, r=result path, a=authors, P=Publication state""")
def main(title, project, collection, path, state, listing, show, pubfy, officer):
    """Lists observations in the archive catalogue. This can be used as a UNIX style filter."""
    global CLIENT
    
    URL = os.environ.get("API_URL")
    if not URL:
        raise RuntimeError("API_URL environment variable not set.")
    
    CLIENT = get_client()
    
    if listing: 
        obs = input2obs(listing)
    else:
        if sys.stdin.isatty():
            obs = cat_filter(title, project, collection, path, state, pubfy, officer)
        else:
            obs = input2obs(click.get_text_stream('stdin'))

    show_list(obs, show)


if __name__ == '__main__':
    main()

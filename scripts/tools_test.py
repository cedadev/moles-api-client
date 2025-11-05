from moles_basic_tools import *
import click

import logging
logger = logging.getLogger(__name__)



@click.command(context_settings={'help_option_names': ['-h', '--help']})
@click.option("--source_uuid", type=str)
@click.option("--target_uuid", type=str)
def main(source_uuid, target_uuid):
    if not source_uuid:
        raise RuntimeError('No UUID')
    
    source_object = uuid_to_obj(source_uuid)
    target_object = uuid_to_obj(target_uuid)
    
    copy_online_resources(source_object, target_object)

if __name__ == '__main__':
    main()
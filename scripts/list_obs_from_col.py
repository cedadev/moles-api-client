import os
import logging
import click
import django
from cedamoles_app.models import *
from moles_basic_tools import *

# Set up Django environment
os.environ["DJANGO_SETTINGS_MODULE"] = "cedamoles_site.settings"
django.setup()

log = logging.getLogger(__name__)


@click.command()
@click.option("-v", "--verbose", is_flag=True, help="Enable verbose logging")
@click.option("-a", "--ignore-publication-level", is_flag=True, help="Ignore publication level")
@click.option("-u", "--unique-level", is_flag=True, help="Use unique level mode")
@click.option("-s", "--source", "source_obs_col_uuid", required=True, help="Source Observation Collection UUID")
def main(verbose, ignore_publication_level, unique_level, source_obs_col_uuid):
    """
    Script to extract observation list for a given observation collection UUID.
    """

    # Configure logging
    if verbose:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.WARNING)

    log.info("Running in verbose mode")

    try:
        obs_list = []
        collection = ObservationCollection.objects.get(uuid=source_obs_col_uuid)
        primary_obs = get_primary_obs_for_collection(collection, ignore_publication_level, unique_level)

        for ob in primary_obs:
            try:
                if ob.result_field:
                    obs_list.append(f"{ob.title}|{ob.uuid}|{ob.result_field.internalPath}\n")
                else:
                    obs_list.append(f"{ob.title}|{ob.uuid}|\n")
            except Exception:
                log.warning("Requested Source record does not exist in catalogue: %s", ob.uuid)
                continue

        # Output file
        os.makedirs("temporary_output_files", exist_ok=True)
        out_path = f"temporary_output_files/obs_list_for_{source_obs_col_uuid}.txt"

        with open(out_path, "w") as outFile:
            outFile.writelines(obs_list)

        log.info("Observation list written to %s", out_path)

    except Exception as ex:
        log.error("Issue with Procedure merging script: %s", ex)
        exit_nicely("Bad call!")


if __name__ == "__main__":
    main()

import click










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

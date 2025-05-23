import os


def main():
    # indicate to the environment we are starting from the CLI
    os.environ["LOCALSTACK_CLI"] = "1"

    # config profiles are the first thing that need to be loaded (especially before localstack.config!)
    from .profiles import set_and_remove_profile_from_sys_argv

    # WARNING: This function modifies sys.argv to remove the profile argument.
    set_and_remove_profile_from_sys_argv()

    # initialize CLI plugins
    from .localstack import create_with_plugins

    cli = create_with_plugins()
    cli()


if __name__ == "__main__":
    main()

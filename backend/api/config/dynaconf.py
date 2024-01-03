from dynaconf import Dynaconf  # type: ignore

settings = Dynaconf(envvar_prefix=False, load_dotenv=True)

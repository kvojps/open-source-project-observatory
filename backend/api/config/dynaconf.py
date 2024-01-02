from dynaconf import Dynaconf

settings = Dynaconf(envvar_prefix=False, load_dotenv=True)

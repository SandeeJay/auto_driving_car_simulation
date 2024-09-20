import yaml
import importlib.resources
from ..config.config import Config


def load_translations(language_code=Config.DEFAULT_LOCALIZATION_LANGUAGE):
    with importlib.resources.files('auto_driving_car_simulation.localize').joinpath(f'{language_code}.yaml').open('r') as file:
        localization = yaml.safe_load(file)
    return localization


localizations = load_translations()



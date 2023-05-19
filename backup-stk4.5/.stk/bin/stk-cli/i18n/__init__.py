from re import finditer
import yaml
import sys
from pathlib import Path

from colorama import Fore, Style

from oscli.commands import (
    RELEASE_NOTES_URL,
    AVAILABLE_STACKS_DOCS_URL,
    CREATE_TEMPLATE_DOCS_URL,
    CREATE_PLUGIN_DOCS_URL,
    CREATE_STACK_DOCS_URL,
    CREATE_STACKFILES_DOCS_URL,
    CREATE_TASKS_DOCS_URL,
    LOGIN_URL,
)
from oscli.core.config import CONFIG
from oscli import CLI_COMMAND_NAME, KEY_COMMAND_NAME
from oscli import __version__


REGEX_GET_PARAMETERS_OF_URI = r"\{(?P<parameter>[a-zA-Z]*(_[a-zA-Z]+)*?)\}"


if getattr(sys, "frozen", False):
    I18N_FOLDER = Path(sys._MEIPASS) / "i18n"
else:
    I18N_FOLDER = Path(__file__).parent

DEFAULT_LOCALE = CONFIG.locale()

FALLBACK_LOCALE = "en_US"


def build_messages_from_yamls() -> dict:
    messages = {}
    for message_bundle in I18N_FOLDER.glob("*.yaml"):
        lang = message_bundle.name.split(".")[0]
        with open(message_bundle, "r", encoding="utf-8") as fp:
            messages[lang] = yaml.safe_load(fp.read())
    return messages


MESSAGES = build_messages_from_yamls()


def __get_message_from_locale(key: str) -> str:
    locale = DEFAULT_LOCALE if DEFAULT_LOCALE in MESSAGES else FALLBACK_LOCALE
    message = MESSAGES[locale].get(key)
    if message is None:
        message = MESSAGES[FALLBACK_LOCALE].get(key, "")

        if not message:
            message = key
    return message


def get_parameters_from_message_key(key):
    message = __get_message_from_locale(key)
    occurrences = finditer(REGEX_GET_PARAMETERS_OF_URI, message)

    parameters = []
    for occurrence in occurrences:
        parameter = occurrence.group("parameter")
        parameters.append(parameter)
    return parameters


def translate(key: str, **kwargs) -> str:
    key = key.replace(CLI_COMMAND_NAME.upper(), KEY_COMMAND_NAME.upper())
    message = __get_message_from_locale(key)

    kwargs = __add_kwargs_with_constants_of_project(kwargs)

    parameter_value_contain_parameters = get_parameters_from_message_key(message)
    if parameter_value_contain_parameters:
        for parameter in parameter_value_contain_parameters:
            if parameter in kwargs:
                value = kwargs[parameter]
            else:
                value = translate(parameter, **kwargs)
            message = message.replace(f"{{{parameter}}}", str(value))

    formatted_message = message.format(**kwargs)
    return formatted_message


def __add_kwargs_with_constants_of_project(kwargs):
    kwargs["__version__"] = __version__
    kwargs["CLI_COMMAND_NAME"] = CLI_COMMAND_NAME
    kwargs["AVAILABLE_STACKS_DOCS_URL"] = AVAILABLE_STACKS_DOCS_URL
    kwargs["LOGIN_URL"] = LOGIN_URL
    kwargs["RELEASE_NOTES_URL"] = RELEASE_NOTES_URL
    kwargs["CREATE_TEMPLATE_DOCS_URL"] = CREATE_TEMPLATE_DOCS_URL
    kwargs["CREATE_PLUGIN_DOCS_URL"] = CREATE_PLUGIN_DOCS_URL
    kwargs["CREATE_STACK_DOCS_URL"] = CREATE_STACK_DOCS_URL
    kwargs["CREATE_STACKFILES_DOCS_URL"] = CREATE_STACKFILES_DOCS_URL
    kwargs["CREATE_TASKS_DOCS_URL"] = CREATE_TASKS_DOCS_URL
    kwargs["FORE_LIGHTGREEN_EX"] = Fore.LIGHTGREEN_EX
    kwargs["FORE_RED"] = Fore.RED
    kwargs["STYLE_RESET_ALL"] = Style.RESET_ALL
    return kwargs


def get_message_not_formatted(key: str) -> str:
    return __get_message_from_locale(key)


class Messages:
    def __getattr__(self, name: str):
        def translate_wrapper(**kwargs) -> str:
            return translate(name.upper(), **kwargs)

        return translate_wrapper

    def translate(self, key: str, **kwargs) -> str:
        return translate(key, **kwargs)

    def missing_param_type(self, param_type: str | None) -> str:
        if param_type == "argument":
            missing = translate("MISSING_ARGUMENT")
        elif param_type == "option":
            missing = translate("MISSING_OPTION")
        elif param_type == "parameter":
            missing = translate("MISSING_PARAMETER")
        else:
            missing = translate("MISSING_PARAM_TYPE", param_type=param_type)
        return missing


messages = Messages()

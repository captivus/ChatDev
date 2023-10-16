"""
Adapted from ChatDev/run.py
"""
import logging
import os
import sys

from ChatDev.camel.typing import ModelType
from ChatDev.chatdev.chat_chain import ChatChain

root = os.path.dirname(__file__)
sys.path.append(root)


def get_config(company):
    """
    return configuration json files for ChatChain
    user can customize only parts of configuration json files, other files will be left for default
    Args:
        company: customized configuration name under CompanyConfig/

    Returns:
        path to three configuration jsons: [config_path, config_phase_path, config_role_path]
    """
    config_dir = os.path.join(root, "CompanyConfig", company)
    default_config_dir = os.path.join(root, "CompanyConfig", "Default")

    config_files = [
        "ChatChainConfig.json",
        "PhaseConfig.json",
        "RoleConfig.json"
    ]

    config_paths = []

    for config_file in config_files:
        company_config_path = os.path.join(config_dir, config_file)
        default_config_path = os.path.join(default_config_dir, config_file)

        if os.path.exists(company_config_path):
            config_paths.append(company_config_path)
        else:
            config_paths.append(default_config_path)

    return tuple(config_paths)


# parser = argparse.ArgumentParser(description='argparse')
# parser.add_argument('--config', type=str, default="Default",
#                     help="Name of config, which is used to load configuration under CompanyConfig/")
# parser.add_argument('--org', type=str, default="DefaultOrganization",
#                     help="Name of organization, your software will be generated in WareHouse/name_org_timestamp")
# parser.add_argument('--task', type=str, default="Develop a basic Gomoku game.",
#                     help="Prompt of software")
# parser.add_argument('--name', type=str, default="Gomoku",
#                     help="Name of software, your software will be generated in WareHouse/name_org_timestamp")
# parser.add_argument('--model', type=str, default="GPT_3_5_TURBO",
#                     help="GPT Model, choose from {'GPT_3_5_TURBO','GPT_4','GPT_4_32K'}")
# args = parser.parse_args()

# Start ChatDev

PROJECT_FILE = 'projects/wod_api.txt'
PROJECT_NAME = 'word_of_the_day-01'

COMPANY = "Default"
ORG_NAME = "DefaultOrganization"
# GPT Model, choose from {'GPT_3_5_TURBO','GPT_4','GPT_4_32K'}"
MODEL = "GPT_3_5_TURBO"


# ----------------------------------------
#          Init ChatChain
# ----------------------------------------

# Open project file & load prompt
with open(PROJECT_FILE, 'r') as f:
    PROJECT = f.read()
    print(f'Project: {PROJECT}')

config_path, config_phase_path, config_role_path = get_config(COMPANY)

args2type = {'GPT_3_5_TURBO': ModelType.GPT_3_5_TURBO, 'GPT_4': ModelType.GPT_4, 'GPT_4_32K': ModelType.GPT_4_32k}

model_type = args2type[MODEL]

chat_chain = ChatChain(config_path=config_path,
                       config_phase_path=config_phase_path,
                       config_role_path=config_role_path,
                       task_prompt=PROJECT,
                       project_name=PROJECT_NAME,
                       org_name=ORG_NAME,
                       model_type=model_type)

# ----------------------------------------
#          Init Log
# ----------------------------------------
logging.basicConfig(filename=chat_chain.log_filepath, level=logging.INFO,
                    format='[%(asctime)s %(levelname)s] %(message)s',
                    datefmt='%Y-%d-%m %H:%M:%S', encoding="utf-8")



# ----------------------------------------
#          Pre Processing
# ----------------------------------------

chat_chain.pre_processing()

# ----------------------------------------
#          Personnel Recruitment
# ----------------------------------------

chat_chain.make_recruitment()

# ----------------------------------------
#          Chat Chain
# ----------------------------------------

# TODO: debug effing weird error ...
chat_chain.execute_chain()

# ----------------------------------------
#          Post Processing
# ----------------------------------------

chat_chain.post_processing()

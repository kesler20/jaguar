from random import randint
import sys
import os
import time
import json
from interfaces.os_interface import OperatingSystemInterface

osi = OperatingSystemInterface()
user_directory = osi.gcu()

argument_number = 3 # this will offset py 4 the args that you pass since arg[0] is workflow.py arg[1] is class and arg[2] is a function 

def pp(print_message: str):
    print(f"------------- {print_message}")
    time.sleep(1)

class AmplifyApplication(object):

    def __init__(self) -> None:
        self.credential_location = os.path.join(
            osi.gcu(), "Onedrive", "Documents", "new_user_credentials.csv")
        self.categories = ["notifications", 'api', 'auth', 'custom', 'storage',
                           'analytics', 'function', 'geo', 'hosting', 'interactions', 'predictions', 'xr']

    def modify_amplify_application(self, categoryIDs):
        os.system(
            r"start excel {}".format(self.credential_location))
        for categoryID in categoryIDs:
            category = self.categories[int(categoryID)]
            os.system(f"amplify add {category}")
            os.system("amplify status")
            os.system("amplify push")
            os.system("amplify pull")

    def import_amplify_application(self):
        '''read the aws config file to extract the useful information'''
        pass

    def initialize_amplify_application(self, *categoryIDs):
        os.system(
            r"start excel {}".format(self.credential_location))
        os.system("amplify init")
        for categoryID in categoryIDs:
            category = self.categories[int(categoryID)]
            os.system(f"amplify add {category}")
            os.system("amplify status")
            os.system("amplify push")
            os.system("amplify pull")

        os.system("amplify publish")

    def sync_env_variable_to_aws_exports(self):
        AWS_CONFIG_DATA = []

        source_dir = os.path.join(os.getcwd(), "src")
        print(f"----------- looking for the aws-exports.js in {source_dir} 🔎")
        time.sleep(1)
        with open(f"{source_dir}/aws-exports.js", "r") as aws_config_file, open(f"{os.getcwd()}/aws-exports.json", "w") as write_file:
            content = aws_config_file.readlines()

            print("-------------------------- aws-export.js found ✅")
            print(aws_config_file.read())
            time.sleep(1)
            # filter the first three lines
            clean_content = list(
                filter(lambda line: content.index(line) > 3, content))
            clean_content.insert(0, "[{")

            # filter the last two lines
            clean_content = list(filter(lambda line: clean_content.index(
                line) < len(clean_content) - 2, clean_content))
            clean_content.append("}]")

            print("--------------------- cleaning up the file to make a json 🧹")
            time.sleep(1)

            for index, line in enumerate(clean_content):
                write_file.write(line)

        with open(f"{os.getcwd()}/aws-exports.json", "r") as read_config_file:
            content: 'list[dict]' = json.loads(read_config_file.read())
            keys = list(content[0].keys())

            print(
                f"----------------------- converting the parsed dictionary to .env variables ⚙️")
            time.sleep(1)
            print(content[0])

            print("------------------------  ---> ")
            for k in keys:
                upper_k = k.upper()
                AWS_CONFIG_DATA.append(
                    f'REACT_APP_{upper_k} = "{content[0][k]}"')
            print(f'REACT_APP_{upper_k} = "{content[0][k]}"')

        print("------------------------------- getting the current .env file ✅")
        time.sleep(1)
        with open(".env", "r+") as env_file:
            content = env_file.readlines()
            clean_content = list(
                filter(lambda line: line.find("REACT_APP_AWS") == -1, content))
            for line in clean_content:
                print(line)

            for variable in AWS_CONFIG_DATA:
                clean_content.append(variable)

        print("---------------------------- writing to the final .env file ✏️")
        time.sleep(1)
        with open(".env", "w") as write_to_env_file:
            clean_content = list(set(clean_content))
            for line in clean_content:
                line = line.replace("\n", "")
                print(line)
                write_to_env_file.write(f'{line}\n')
            os.remove("aws-exports.json")

    def push_to_amplify(target_directory: str):
        '''
        In order to publish to amplify make sure that you have initialised the correct application
        and that the repository is bering configure

        According to the documentation after adding the hosting category you can commit by running amplify push
        ---
        ```cmd
        amplify push
        ```
        '''
        print(f"------------- cd into --> {target_directory} 🚕")
        os.chdir(target_directory)
        print("------------ running tests using npm 🧪")
        os.system("npm test")
        time.sleep(1)
        print("------------ formatting code using prettier ✨")
        os.system("prettier -w .")
        time.sleep(1)
        print("------------ the tests have passed so we can push to github ✅")
        time.sleep(1)
        os.system("git pull")
        os.system("git add . ")
        os.system('git commit -m "make it better"')
        time.sleep(1)
        os.system("git push ")
        print("------------ publishing the application to amplify ✅")
        os.system("amplify publish")
        os.system("------------ workflow completed successfully ✅")

class ReactApplication(object):

    def __init__(self) -> None:
        pass

    def initialise_env_file(self):
        with open(".env", "w") as env, open(os.path.join(osi.gcu(), "Protocol", "jaguar", "config.py", "r")) as configs:
            content = configs.read()
            env.write(content)

    def initialise_npm_process(self) -> None:
        '''signature description'''
        
        target_directory = os.getcwd()
        print(f"------------- cd into --> {target_directory} 🚕")
        os.chdir(target_directory)
        time.sleep(1)
        print("------------- pull resent changes from github ↪️")
        os.system("git pull")
        time.sleep(1)
        print("------------ making sure that the npm packages are installed ⚙️")
        os.system("npm i")
        time.sleep(1)
        print("------------ starting the application")
        os.system("npm start")
        time.sleep(1)

class GithubRepository(object):
    '''This is a representation of your directory according to github'''

    def __init__(self) -> None:
        pass

    def test_and_push_to_github(self, *args) -> None:
        '''test_and_push_to_github will:
        1. cd into target_directory
        2. git pull the latest changes from github
        3. run the tests, depending on whether is a python or javascript repo:
        - jest for javascript
        - pytest for python
        4. push the changes to github with the custom message

        you can call this method by running:
        ```bash
        python workflow.py "git" "test" "py" "t commit message for changing test code"
        ```
        ---
        Params:
        - _type - str : this can be py or js and it dictates what types of tests are run 
        - target_directory - str : this is the directory which the os will cd into

        ---
        Returns:
        - None
        '''
        _type = args[argument_number]
        commit_message = args[argument_number + 1]
        target_directory = os.getcwd() if args[argument_number + 2] != None or args[argument_number + 2] != "" else args[argument_number + 2]

        pp(f"cd into --> {target_directory} 🚕")
        os.chdir(target_directory)
        pp(f"pull recent changes from github 😼")
        os.system("git pull")

        if _type == "js":
            pp("running tests using npm ☕Script 🧪")
            os.system("npm test")

        if _type == "py":
            pp("running tests using pytest 🐍🧪")
            os.system("python -m pytest")
        
        test_result = input("have all the tests passed? (y/n):")
        if test_result == "y":
            pp("the tests have passed so we can push to github ✅")
            os.system("git add . ")
            os.system(f'git commit -m "{self.style_commit_message(commit_message)}"')
            os.system("git push ")
        else:
            pp("workflow completed without pushing ❌")

    def push_to_github(self) -> None:
        '''signature description'''

        target_directory = os.getcwd()
        pp("pushing untested code 😞")
        pp(f"cd into --> {target_directory} 🚕")
        os.chdir(target_directory)
        os.system("git pull")
        os.system("git add . ")
        os.system('git commit -m "make it better"')
        os.system("git push ")
    
    # internal function
    def style_commit_message(self, commit_message: str) -> str:
         # this is to make commit messages more interesting
        code_commit_message_emojis = ["😕","⭐","✊","🤝","👐"]
        if commit_message.startswith("t "):
            message_prefix = "test: "
            message_suffix = "🧪"
            commit_message = commit_message.replace("t ","")

        elif commit_message.startswith("d "):
            message_prefix = "documentation: "
            message_suffix = "📰"
            commit_message = commit_message.replace("d ","")

        elif commit_message.startswith("c "):
            message_prefix = "code: "
            message_suffix = code_commit_message_emojis[randint(0,len(code_commit_message_emojis) - 1)]
            commit_message = commit_message.replace("c ","")

        else:
            message_prefix = ""
            message_suffix = ""

        return message_prefix + commit_message + message_suffix
    


if __name__ == "__main__":
    amplify = AmplifyApplication()
    react = ReactApplication()
    git = GithubRepository()

    # def return_none() make the return none decorator
    git.test_and_push_to_github(*sys.argv)


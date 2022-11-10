# Jaguar Library 😼

Jaguar is a library of front-end, back-end and api components
to build applications in python and javascript fast

<div style="display:flex; justify-content:center; align-items:center; width:100%;">
  <img src="logo.png" style="width: 40%"/>
</div>

### UI Components

The library contains navigation bars and various other components ready to be edited ✏️

<div style="display:flex;border: 1px solid blue">
<img src="mycomponents.png" style="width: 40%"/>

<img src="mynav.png" style="width: 40%"/>
</div>

### Workflow.py

using the `workflow.py` file
you can push code by running:

```bash
python workflow.py p
```

One of the main use cases of the workflow.py file could be to share files across different folders
this is becasue if we update iiles which we may want to share across different projects, we could do it only in the jaguar foldr
make sure that it works and then run the following command

```bash

```

The format of the calls are:

```bash
python workflow.py class_name function_name "argument1" "argument2"
```

The last argument is usually the directoy, if you write \* this will apply a function to all directories or also if you leave it black
this will use the current working directory

> If you write "this.py That.js" etc it will apply It to the listed files
> If the function is not found it will just push untested code to github

> If you run -help this should return a list of all the commands and the doc string of the functions and classes that they call

> If you do not enter the arguments to the function, the argument that will be passed is None by default

to start using the `workflow.py` use

```bash
python workflow.py "install"
```

this will copy the current jaguar `os_interface.py` file and the `workflow.py` file in all the repositories in the root protocol folder.

the following table summarizes various commands
| command | Description | Options |
| --- | --- | --- |
| `python workflow.py p ` | push untested code to github with a default message of code: make it better | None |
| `python workflow.py "d changed documentation"` | push code using a custom message | use `"c code change message"/"d document change message"/"t test change message"` |  
| `python workflow.py "push"` | this will run "python workflow.py g" on all the directories in the protocol folder | None |
| `python workflow.py "sync"` | this command will syncronize files from jaguar | standard command `python workflow.py "f interfaces\os_interface.py" "protocol_backend"` anything starting with "f " is considered a file and if the folders preceeding it do not exist this will be created in the repositories given (args withoput the leading "f ")|
| `python workflow.py "git"` | push code to github from a target dir | `p g "target_directory"` to push a new github repo `python workflow.py "git" "init"` to push a new branch `python workflow.py "git" "init" "branch"` |
| `python workflow.py "git" t "py" "t commit message for changing test code"` | runs python tests and pushes to github after asking for permission | py/js for what tests to run - "t "/"c "/"d " for test, code, and document commit messages respectively |
| `python workflow.py aws "init" 1` | initialise an amplify application with notifications category | 1,2,3,4, -> 11 run `python workflow.py "aws" d` to check category ids |
| `python workflow.py aws "edit" 1` | add categories to an existing amplify app | you could also run `python workflow.py "aws" u 1` to remove and add categories for updates |
| `python workflow.py aws "sync" 1` | synchronize .env file with the aws-exports file | None |
| `python workflow.py aws "publish"` | run jest tests, format code, push to github, publish to amplify | None |
| `python workflow.py "aws" d` | describe the categories and best practices | None |
| `python workflow.py "react" "init"` | clone a react project, pull the latest changes, run npm i, run npm start | `python workflow.py "react" "init" "project_name"` |
| `python workflow.py "react" "config"` | create a .env file in the root dir | None |


#!/bin/bash

CLI_NAME="stk"

[ -e "${HOME}/.${CLI_NAME}" ]
if [ $? -eq 0 ]
then
    echo "A ${HOME}/.${CLI_NAME} folder is present on the machine."
    while true; do
        read -p "Do you wish to remove the ${HOME}/.${CLI_NAME} folder with all imported stacks? [y/N]?" answer
        [[ $answer == "n" || $answer == "N"  || $answer == "" ]] && exit 0
        [[ $answer == "y" || $answer == "Y" ]] && break
    echo "Please answer with 'y' or 'n'"
    done

    echo "Application uninstalling process started"

    #remove .stk folder
    [ -e "${HOME}/.${CLI_NAME}" ] && rm -rf ${HOME}/.${CLI_NAME}
    if [ $? -eq 0 ]
    then
        echo "[DONE] Successfully deleted .${CLI_NAME} folder"
    else
        echo "[WARNING] Could not delete .${CLI_NAME} folder" >&2
    fi

    echo "Application uninstall process finished"
    exit 0
fi

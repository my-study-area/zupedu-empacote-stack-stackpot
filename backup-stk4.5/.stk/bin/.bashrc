
export PATH=$HOME/.stk/bin:$PATH
_stk_completion() {
    local IFS=$'\n'
    local response

    response=$(env COMP_WORDS="${COMP_WORDS[*]}" COMP_CWORD=$COMP_CWORD _STK_COMPLETE=bash_complete ~/.stk/bin/stk-cli/stk)

    for completion in $response; do
        IFS=',' read type value <<< "$completion"

        if [[ $type == 'dir' ]]; then
            COMPREPLY=()
            compopt -o dirnames
        elif [[ $type == 'file' ]]; then
            COMPREPLY=()
            compopt -o default
        elif [[ $type == 'plain' ]]; then
            COMPREPLY+=($value)
        fi
    done

    return 0
}

_stk_completion_setup() {
    complete -o nosort -F _stk_completion stk
}

_stk_completion_setup;


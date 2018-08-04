#!/bin/bash
cd ./ui && npm run dev &
cd ./api && pipenv run python manage.py runserver &

exit_script() {
   echo -e "\nShutting down..."
   trap - SIGINT SIGTERM # clear the trap
   kill -- -$$ # Sends SIGTERM to child/sub processes
}

trap exit_script SIGINT SIGTERM
wait
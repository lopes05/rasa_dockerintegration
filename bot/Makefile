help:
	@echo "    train-core"
	@echo "        Train a dialogue model using Rasa core."
	@echo "    run"
	@echo "        Runs the bot on the command line."
	@echo "    run-core"
	@echo "        Runs the core server."
	@echo "    run-actions"
	@echo "        Runs the action server."

run:
	make run-actions&
	make run-core

run-core:
	python -m rasa_core.run --core models/dialogue -u models/nlu/default/current --endpoints endpoints.yml --debug

run-actions:
	python -m rasa_core_sdk.endpoint --actions actions

train-core:
	python train.py

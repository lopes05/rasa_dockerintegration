from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

from rasa_core.policies.fallback import FallbackPolicy



def train_dialogue(domain_file="domain.yml",
                   model_path="models/dialogue",
                   training_data_file="data/stories.md"):
    fallback = FallbackPolicy(fallback_action_name="action_default_fallback",
                          core_threshold=0.2,
                          nlu_threshold=0.2)

    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=2), KerasPolicy(), fallback])

    training_data = agent.load_data(training_data_file)
    agent.train(
            training_data,
            epochs=100,
            batch_size=100,
            validation_split=0.2
    )

    agent.persist(model_path)
    return agent


def train_nlu():
    from rasa_nlu.training_data import load_data
    from rasa_nlu import config
    from rasa_nlu.model import Trainer

    training_data = load_data('data/intents/intents.md')
    trainer = Trainer(config.load("nlu_config.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist('models/nlu/',
                                      fixed_model_name="current")

    return model_directory


if __name__ == '__main__':
    utils.configure_colored_logging(loglevel="INFO")

    train_nlu()
    train_dialogue()

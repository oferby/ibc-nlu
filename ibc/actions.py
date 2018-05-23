from rasa_core.actions import Action
from rasa_core.events import SlotSet


class ActionShowEcs(Action):
    def name(self):
        return "action_show_ecs"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("here's what I found:")
        return []


class ActionCreateEcs(Action):
    def name(self):
        return "action_create_ecs"

    def run(self, dispatcher, tracker, domain):
        tracker.get_slot("mem_size")
        return []


class ActionCheckConfirmation(Action):
    def name(self):
        return "action_check_confirmation"

    def run(self, dispatcher, tracker, domain):
        if tracker.get_slot("approve") == "yes":
            return [SlotSet("isApproved", True)]

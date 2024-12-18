from ovos_workshop.skills import OVOSSkill
from ovos_workshop.decorators import intent_handler


class IceCreamSkill(OVOSSkill):
    @intent_handler('do.you.like.intent')
    def handle_do_you_like(self):
        likes_ice_cream = self.ask_yesno('vind.jij.ijs.leker')
        if likes_ice_cream == 'yes':
            self.speak_dialog('heel.goed')
        elif likes_ice_cream == 'no':
            self.speak_dialog('dat.is.jammer')
        else:
            self.speak_dialog('dat.begrijp.ik.niet')
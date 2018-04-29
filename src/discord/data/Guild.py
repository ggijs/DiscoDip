import discord.data.member as member
import discord.data.role as role
import discord.utility as u

'''
    This represents a guild that the bot is member of, contains all relevant information for this server (i.e. roles, members, emoji's channels etc...)
'''
class Guild:

    '''
        Constructs the guild object, parsed from a peeled GUILD_CREATE event,
        autofills all optional and not-present data (may be None)
    '''
    def __init__(self, event):
        # Guaranteed values
        self.id = event["id"]
        self.name = event["name"]
        self.icon = event["icon"]
        self.splash = event["splash"]
        self.owner_id = event["owner_id"]
        self.region = event["region"]
        self.afk_timeout = event["afk_timeout"]
        self.verification_level = event["verification_level"]
        self.default_message_notifications = event["default_message_notifications"]
        self.explicit_content_filter = event["explicit_content_filter"]
        # PARSE ROLES
        self.roles = {}
        for r in event["roles"]:
            obj = role.Role(r)
            self.roles[obj.id] = obj

        # PARSE EMOJI's
        # PARSE FEATURES

        self.mfa_level = event["mfa_level"]
        self.system_channel_id = event["system_channel_id"]

        # optional values
        self.owner = u.get_safe(event, "owner")
        self.permissions = u.get_safe(event, "permissions")
        self.afk_channel_id = u.get_safe(event, "afk_channel_id")
        self.embed_enabled = u.get_safe(event, "embed_enabled")
        self.embed_channel_id = u.get_safe(event, "embed_channel_id")
        self.application_id = u.get_safe(event, "application_id")
        self.widget_enabled = u.get_safe(event, "widget_enabled")
        self.widget_channel_id = u.get_safe(event, "widget_channel_id")
        self.joined_at = u.get_safe(event, "joined_at")
        self.large = u.get_safe(event, "large")
        self.unavailable = u.get_safe(event, "unavailable")
        self.member_count = u.get_safe(event, "member_count")
        
        #PARSE VOICE STATES

        #PARSE MEMBERS
        self.members = {}
        memlist = u.get_safe(event, "members")
        if(memlist):
            for mem in memlist:
                obj = member.Member(mem, self)
                self.members[obj.id] = obj
        
        #PARSE CHANNELS
        #PARSE PRESENCES

    '''
        Returns a role by its ID
    '''
    def get_role(self, id):
        if id in self.roles:
            return self.roles[id]
        
        print('ID NOT IN ROLES...')
        return None

    '''
        to_string with indent formatting for debug output.
    '''
    def to_string(self, indent = 0):
        msg = ''
        for key, value in self.__dict__.items():
            if key == 'roles':
                msg += ('    ' * indent) + 'Roles:\r\n'
                for r in self.roles.values():
                    msg += r.to_string(indent + 1) + '\r\n'
            elif key == 'members':
                msg += ('    ' * indent) + 'Members:\r\n'
                for m in self.members.values():
                    msg += m.to_string(indent + 1) + '\r\n'
            else:
                msg += ('    ' * indent) + '{} : {}\r\n'.format(key, value)
        
        return msg
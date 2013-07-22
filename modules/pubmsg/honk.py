import irclib
import random
class honk:
    def honk(self, source, target=None):
        if not target:
            if random.randint(1, 3) == 2:
                out = "\x01ACTION fines %s $%i for honking.\x01" % (source, random.randint(1, 500))
            else:
                out = "\x01ACTION honks %s\x01" % source
        else:
            randnum = random.randint(1, 4)
            if randnum == 1:
                out = "\x01ACTION fines %s $%i for honking.\x01" % (source, random.randint(1, 500))
            elif randnum == 2:
                out = "\x01ACTION fines %s $%i for being too lewd and getting honked at.\x01" % (target.strip(), random.randint(1, 500))
            else:
                out = "\x01ACTION honks %s\x01" % target.strip()
        return out
    def on_pubmsg(self, nick, connection, event):
        message = event.arguments()[0]
        source = event.source().split('!')[0]
        custom = 0
        if message.startswith(".honk"):
            try:
                target = message.strip().split(" ")[1]
                reply = self.honk(source, target)            
            except:                
                reply = self.honk(source)
            connection.privmsg(event.target(), reply)

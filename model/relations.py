class Relations:

    def __init__(self, cid=None, gid=None):
        self.cid=cid
        self.gid=gid

    def __repr__(self):
        # representation of the object in Console
        return "Contact id: %s; Group Id: %s" % (self.cid, self.gid)

    def __eq__(self, other):
        # comparison of two objects
        return (self.cid is None or other.cid is None or self.cid == other.cid) and (self.gid is None or other.gid is None or self.gid == other.gid)
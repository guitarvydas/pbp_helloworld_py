import sys
sys.path.insert(0, './pbp/kernel')
import kernel0d as zd

# define template
def install (reg):
    def handler (eh,mev):
        try:
            zd.send (eh, "", "World", mev)
        except (e):
            zd.send (eh, "✗", "*** error in World.py ***", mev)
    def instantiate (reg,owner,name, arg, template_data):
        name_with_id = zd.gensymbol ( "World")
        return zd.make_leaf ( name_with_id, owner, None, arg, handler)

    zd.register_component (reg, zd.mkTemplate ("World", None, instantiate))



import sys
sys.path.insert(0, './pbp/kernel')
import kernel0d as zd

# define template
def install (reg):
    def handler (eh,mev):
        try:
            zd.send (eh, "", "Hello", mev)
        except (e):
            zd.send (eh, "✗", "*** error in Hello.py ***", mev)
    def instantiate (reg,owner,name, arg, template_data):
        name_with_id = zd.gensymbol ( "Hello")
        return zd.make_leaf ( name_with_id, owner, None, arg, handler)

    zd.register_component (reg, zd.mkTemplate ("Hello", None, instantiate))



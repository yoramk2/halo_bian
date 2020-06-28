
class BianPlugin():

    def ready(self):
        return True

    def run(self,core,*params):

        imports = params[0]
        base_lib= params[1]
        base_class_name= params[2]
        name= params[3]
        line3 = ""
        if name.endswith('Activation'):
            imports = imports + "from " + base_lib + " import " + 'Activation'+base_class_name + "\n\n"
            line3 = "class " + name + "Mixin(Activation" + base_class_name + "):" + \
                    "\n\tpass"
        elif name.endswith('Configuration'):
            imports = imports + "from " + base_lib + " import " + 'Configuration' + base_class_name + "\n\n"
            line3 = "class " + name + "Mixin(Configuration" + base_class_name + "):" + \
                    "\n\tpass"
        elif name.endswith('Feedback'):
            imports = imports + "from " + base_lib + " import " + 'Feedback' + base_class_name + "\n\n"
            line3 = "class " + name + "Mixin(Feedback" + base_class_name + "):" + \
                    "\n\tpass"
        elif name.endswith('Initiation'):
            line3 = "class " + name + "Mixin(" + base_class_name + "):" + \
                    "\n\tbian_action = ActionTerms.INITIATE"
        elif name.endswith('Update'):
            line3 = "class " + name + "Mixin(" + base_class_name + "):" + \
                    "\n\tbian_action = ActionTerms.UPDATE"
        elif name.endswith('Control'):
            line3 = "class " + name + "Mixin(" + base_class_name + "):" + \
                    "\n\tbian_action = ActionTerms.CONTROL"
        elif name.endswith('Exchange'):
            line3 = "class " + name + "Mixin(" + base_class_name + "):" + \
                    "\n\tbian_action = ActionTerms.EXCHANGE"
        elif name.endswith('Execution'):
            line3 = "class " + name + "Mixin(" + base_class_name + "):" + \
                    "\n\tbian_action = ActionTerms.EXECUTE"
        elif name.endswith('Requisition'):
            line3 = "class " + name + "Mixin(" + base_class_name + "):" + \
                    "\n\tbian_action = ActionTerms.REQUEST"
        else:
            line3 = "class " + name + "Mixin(" + base_class_name + "):" + \
                    "\n\tbian_action = ActionTerms.RETRIEVE"

        return {"imports":imports,"line3":line3}



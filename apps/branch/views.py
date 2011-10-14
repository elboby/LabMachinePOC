from django.http import HttpResponse

def list(request):
    return HttpResponse("list of branches")
    
def view(request, branch_id):
    
    ## branch = retrieve_object(branch_id)
    
    return HttpResponse("branch %s" % branch_id)
    
def create(request, branch_id):
    #try:
    validate_input(branch_id)
    bc = BranchCreator()
    branch = bc.run(branch_id)
    # except InvalidInput:
    #     return HttpResponse("invalid data for branch %s" % branch_id)
    # except CreationProblem:
    #     return HttpResponse("error while creating branch %s" % branch_id)
        
    return HttpResponse("creating branch %s" % branch_id)
    
    
def validate_input(id):
    return True
    
class BranchCreator(object):
    def run(self, id):
        branch = get_or_create_branch(id)
        notify(branch, 'start installation')
        self.launch_steps(branch)
        return branch
    
    def launch_steps(self, branch):
        return

def get_or_create_branch(id):
    return {'id': int(id)}
    
def notify(branch, msg):
    print "{NOTIFY} branch: %d, msg: %s" % (branch['id'], msg)
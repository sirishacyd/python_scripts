"""
testcases
This will hold a handful of functions that can be 'steps'
"""

def steps_build(project, count=10):
    """
    steps_build(project, count=10)
    """
    print("Building", project)
    print()

    if count > 20:
        return 1

    return 0

def steps_test(easy=True, speed=False):
    """
    steps_test
    run the tests
    """
    print("Testing", easy, speed)
    print()

    return 0

def steps_deploy(deployments):
    """
    steps_deploy
    dummy function
    """
    print("Deploying to the following deployments", deployments)
    print()

    return 0

def steps_clean(nuke=False):
    """
    steps_clean
    dummy function
    """
    print("Running deep clean" if nuke else "Cleaning ...")
    print()

    return 0

##########################################################
# Computer Networks course project, CS6250, Georgia Tech #
##########################################################

import commands

class LoadGenerator(object):
    """Generates artificial load for E2 hosts"""
    @staticmethod
    def src(destip, destport, num_request=0):
        nping = commands.getoutput("which nping")
        if nping:
            return "{} --tcp --rate 1 -c {} -p {} {}".format(nping, num_request, destport, destip)
        else:
            raise Exception("nping not found!")

    @staticmethod
    def dest(port):
        ncat = commands.getoutput("which ncat")
        if ncat:
            return "{} -l {} --keep-open --exec \"/bin/cat\"".format(ncat, port)
        else:
            raise Exception("ncat not found!")
